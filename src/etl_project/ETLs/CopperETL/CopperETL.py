import os
import io
import pyarrow.parquet as pq
from prefect import flow, task
from config.Settings import UseSettings
from datetime import datetime, timezone
from config.Logger import Logger
from config.GetModels import GetModels
from config.Connections import Connections
from ETLs.ETLBaseModel import ETLBaseModel
from config.sql.tables.data_ingestion import data_ingestion
from config.sql.inserts.insert_data_ingestion import insert_data_ingestion

class CopperETL(ETLBaseModel):
    def __init__(self):
        self.settings = UseSettings.get_settings() 

    @task(name="get_parquet_files")
    def get_parquet_files(self, bucket_name):
        s3 = Connections.get_s3_client()
        response = s3.list_objects_v2(Bucket=bucket_name)
        return [obj['Key'] for obj in response.get('Contents', []) if obj['Key'].endswith('.parquet')]

    @task(name="read_parquet_and_insert_to_clickhouse")
    def read_parquet_and_insert_to_clickhouse(self, bucket_name, file_key):
        start_time = datetime.now(timezone.utc)
        s3 = Connections.get_s3_client()
        obj = s3.get_object(Bucket=bucket_name, Key=file_key)
        buffer = io.BytesIO(obj['Body'].read())
        parquet_data = pq.ParquetFile(buffer)

        client = Connections.get_clickhouse_client()

        client.execute(data_ingestion)

        tag = os.path.dirname(file_key).split('/')[-1]

        response = []

        try:
            [model_class, view_commands] = GetModels.get_model_by_path(tag)
        except:
            end_time = datetime.now(timezone.utc)
            details = (
                f"Error! Pydantic {tag} model class not found"
            )
            Logger.observability("read_parquet_and_insert_to_clickhouse", start_time, end_time, details)
            Logger.msg(details, "error")
            return details

        for view_command in view_commands:
            client.execute(view_command)

        rows = []

        for batch in parquet_data.iter_batches():
            for row in batch.to_pylist():
                try:
                    validated_row = model_class(**row)
                    data_content = validated_row.model_dump_json()
                    data_path = file_key
                    data_tag = tag

                    data_key = str(data_content) + str(data_path)

                    rows.append((data_content, data_path, data_tag, data_key))
            
                except Exception as e:
                    msg = f"Erro de validacao na linha {row}: {e}"
                    Logger.msg(f"Erro de validacao na linha {row}: {e}", "error")
                    Logger.msg(f"caminho do arquivo {file_key}", "error")
                    response.append(msg)
        
        if rows:
            client.execute(
                insert_data_ingestion,
                rows
            )

        end_time = datetime.now(timezone.utc)
        details = (
            f"Processed {len(rows)} records of {tag} from {file_key} in bucket {bucket_name}."
        )
        Logger.observability("read_parquet_and_insert_to_clickhouse", start_time, end_time, details)
        Logger.msg(details, "info")
        response.append(details)
        return response

    @flow(name="ingest data", log_prints=True)
    def ingest_data(self):
        start_time = datetime.now(timezone.utc)
        parquet_files = self.get_parquet_files(self.settings.BUCKET_NAME)
        response = []
        for file_key in parquet_files:
            result = self.read_parquet_and_insert_to_clickhouse(self.settings.BUCKET_NAME, file_key)
            response.append(result)
        end_time = datetime.now(timezone.utc)
        details = f"Ingested data from all Parquet files in all buckets"
        response.append(details)
        
        Logger.msg(details, "info")
        Logger.observability("ingest_data", start_time, end_time, details)
        return response