import boto3
import psycopg2
from clickhouse_driver import Client
from config.Settings import UseSettings

class Connections():
    @staticmethod
    def get_s3_client():
        settings = UseSettings.get_settings()
        return boto3.client(
            's3',
            aws_access_key_id=settings.AWS_ACCESS_KEY,
            aws_secret_access_key=settings.AWS_SECRET_KEY,
            aws_session_token=settings.AWS_SESSION_TOKEN,
            region_name=settings.AWS_REGION
        )

    @staticmethod
    def get_clickhouse_client():
        settings = UseSettings.get_settings()
        return Client(
            host=settings.CLICKHOUSE_HOST,
            port=settings.CLICKHOUSE_PORT,
            user=settings.CLICKHOUSE_USER,
            password=settings.CLICKHOUSE_PASSWORD
        )

    @staticmethod
    def get_postgres_connection():
        settings = UseSettings.get_settings()
        return psycopg2.connect(
            host=settings.POSTGRES_HOST,
            port=settings.POSTGRES_PORT,
            dbname=settings.POSTGRES_DB,
            user=settings.POSTGRES_USER,
            password=settings.POSTGRES_PASSWORD
        )