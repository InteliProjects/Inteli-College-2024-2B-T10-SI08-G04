import clickhouse_connect
import pandas as pd
from config.Settings import UseSettings

class Clickhouse():
    @staticmethod
    def __get_clickhouse_client():
        try:
            settings = UseSettings.get_settings()
            client = clickhouse_connect.get_client(
                host=settings.CLICKHOUSE_HOST,
                port=settings.CLICKHOUSE_PORT,
                username=settings.CLICKHOUSE_USER,
                password=settings.CLICKHOUSE_PASSWORD
            )
            return client
        except Exception as e:
            print(f"Erro ao conectar ao ClickHouse: {e}")
            raise e
    
    @staticmethod
    def query(query):
        try:
            client = Clickhouse.__get_clickhouse_client()
            result = client.query(query)
            return result
        finally:
            if 'client' in locals() and client:
                client.close()
    