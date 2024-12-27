from pydantic_settings import BaseSettings
from typing import Dict

class Settings(BaseSettings):
    CLICKHOUSE_HOST: str
    CLICKHOUSE_PORT: int
    CLICKHOUSE_USER: str
    CLICKHOUSE_PASSWORD: str
    AUTH_TOKEN: str
    BACKEND_SERVER_ADDRESS: str
    USERS: Dict[str, dict] 
    
    class Config:
        env_file = ".env"

class UseSettings():
    @staticmethod
    def get_settings():
        settings = Settings()
        return settings



