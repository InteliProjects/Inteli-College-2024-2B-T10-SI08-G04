import pytest
from config.Settings import UseSettings
from pydantic_core import ValidationError

class TestSettings:
    @pytest.fixture
    def successful_env(self, monkeypatch):
        monkeypatch.setenv('AWS_ACCESS_KEY', 'valid_access_key')
        monkeypatch.setenv('AWS_SECRET_KEY', 'valid_secret_key')
        monkeypatch.setenv('AWS_SESSION_TOKEN', 'valid_session_token')
        monkeypatch.setenv('AWS_REGION', 'us-east-1')
        monkeypatch.setenv('CLICKHOUSE_HOST', 'valid_clickhouse_host')
        monkeypatch.setenv('CLICKHOUSE_PORT', 9000)
        monkeypatch.setenv('CLICKHOUSE_USER', 'valid_user')
        monkeypatch.setenv('CLICKHOUSE_PASSWORD', 'valid_password')
        monkeypatch.setenv('POSTGRES_HOST', 'valid_postgres_host')
        monkeypatch.setenv('POSTGRES_PORT', 5432)
        monkeypatch.setenv('POSTGRES_DB', 'valid_db')
        monkeypatch.setenv('POSTGRES_USER', 'valid_user')
        monkeypatch.setenv('POSTGRES_PASSWORD', 'valid_password')
        monkeypatch.setenv('BUCKET_NAME', 'valid_user')
        monkeypatch.setenv('AUTH_TOKEN', 'valid_password')

    @pytest.fixture
    def incomplete_env(self, monkeypatch):
        monkeypatch.setenv('AWS_ACCESS_KEY', 'valid_access_key')
        monkeypatch.setenv('AWS_SECRET_KEY', 'valid_secret_key')
        monkeypatch.setenv('AWS_SESSION_TOKEN', 'valid_session_token')
        monkeypatch.setenv('AWS_REGION', 'us-east-1')
        monkeypatch.setenv('CLICKHOUSE_HOST', 'valid_clickhouse_host')
        monkeypatch.setenv('CLICKHOUSE_PORT', '9000')
        monkeypatch.setenv('CLICKHOUSE_USER', 'valid_user')
        monkeypatch.setenv('CLICKHOUSE_PASSWORD', 'valid_password')
        monkeypatch.setenv('POSTGRES_HOST', 'valid_postgres_host')
        monkeypatch.setenv('POSTGRES_PORT', '5432')
        monkeypatch.setenv('POSTGRES_DB', 'valid_db')
        monkeypatch.setenv('POSTGRES_USER', 'valid_user')
        monkeypatch.setenv('POSTGRES_PASSWORD', None)
        monkeypatch.setenv('BUCKET_NAME', 'valid_user')

    def test_get_settings_success(self, successful_env):
        settings = UseSettings.get_settings()
        
        assert settings.AWS_ACCESS_KEY == 'valid_access_key'
        assert settings.AWS_SECRET_KEY == 'valid_secret_key'
        assert settings.AWS_SESSION_TOKEN == 'valid_session_token'
        assert settings.AWS_REGION == 'us-east-1'
        assert settings.CLICKHOUSE_HOST == 'valid_clickhouse_host'
        assert settings.CLICKHOUSE_PORT == 9000
        assert settings.CLICKHOUSE_USER == 'valid_user'
        assert settings.CLICKHOUSE_PASSWORD == 'valid_password'
        assert settings.POSTGRES_HOST == 'valid_postgres_host'
        assert settings.POSTGRES_PORT == 5432
        assert settings.POSTGRES_DB == 'valid_db'
        assert settings.POSTGRES_USER == 'valid_user'
        assert settings.POSTGRES_PASSWORD == 'valid_password'
        assert settings.BUCKET_NAME == 'valid_user'
        assert settings.AUTH_TOKEN == 'valid_password'

    def test_get_settings_failure(self, incomplete_env):
        with pytest.raises(ValidationError):
            settings = UseSettings.get_settings()
