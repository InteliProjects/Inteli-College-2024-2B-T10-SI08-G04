from abc import ABC, abstractmethod

class ETLBaseModel(ABC):
    @abstractmethod
    def get_parquet_files(self, bucket_name):
        pass

    @abstractmethod
    def read_parquet_and_insert_to_clickhouse(self, bucket_name, file_key):
        pass

    @abstractmethod
    def ingest_data(self):
        pass