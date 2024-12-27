from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    AWS_ACCESS_KEY: str
    AWS_SECRET_KEY: str
    AWS_REGION: str
    AWS_SESSION_TOKEN: str
    CLICKHOUSE_HOST: str
    CLICKHOUSE_PORT: int
    CLICKHOUSE_USER: str
    CLICKHOUSE_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    BUCKET_NAME: str
    AUTH_TOKEN: str

    class Config:
        env_file = ".env"

class UseSettings():
    @staticmethod
    def get_settings():
        settings = Settings()
        return settings



