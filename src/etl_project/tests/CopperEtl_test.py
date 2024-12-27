import pytest
from unittest.mock import Mock, patch, MagicMock
from datetime import datetime, timezone
from ETLs.CopperETL.CopperETL import CopperETL
from config.Connections import Connections
from config.Logger import Logger
import io
import pyarrow as pa

class TestCopperETL:

    @pytest.fixture
    def mock_settings(self):
        return {
            "AWS_ACCESS_KEY": "fake_access_key",
            "AWS_SECRET_KEY": "fake_secret_key",
            "AWS_REGION": "us-east-1",
            "AWS_SESSION_TOKEN": "fake_session_token",
            "CLICKHOUSE_HOST": "localhost",
            "CLICKHOUSE_PORT": 9000,
            "CLICKHOUSE_USER": "default",
            "CLICKHOUSE_PASSWORD": "password",
            "POSTGRES_HOST": "localhost",
            "POSTGRES_PORT": 5432,
            "POSTGRES_DB": "testdb",
            "POSTGRES_USER": "testuser",
            "POSTGRES_PASSWORD": "testpassword",
            "BUCKET_NAME": "test-bucket",
            "AUTH_TOKEN": "fake_auth_token"
        }

    @pytest.fixture
    def mock_s3_client(self):
        mock_s3 = MagicMock()
        Connections.get_s3_client = MagicMock(return_value=mock_s3)
        return mock_s3

    @pytest.fixture
    def mock_clickhouse_client(self):
        mock_clickhouse = MagicMock()
        Connections.get_clickhouse_client = MagicMock(return_value=mock_clickhouse)
        return mock_clickhouse

    @pytest.fixture
    def copper_etl(self, mock_settings):
        with patch('config.Settings.UseSettings.get_settings', return_value=Mock(**mock_settings)):
            return CopperETL()

    # Caminho Feliz
    @patch('config.Logger.Logger.msg')
    @patch('config.Logger.Logger.observability')
    def test_read_parquet_and_insert_to_clickhouse_success(
        self, mock_observability, mock_msg, copper_etl, mock_s3_client, mock_clickhouse_client
    ):
        # Arrange
        mock_s3_client.get_object.return_value = {
            'Body': io.BytesIO(b"mock parquet content")
        }

        with patch('pyarrow.parquet.ParquetFile') as mock_parquet_file:
            mock_parquet = MagicMock()
            mock_parquet.iter_batches.return_value = [
                pa.Table.from_pydict({
                    'col1': ['value1'],
                    'col2': ['value2']
                }).to_batches()[0]
            ]
            mock_parquet_file.return_value = mock_parquet

            mock_model = MagicMock()
            mock_model(**{'col1': 'value1', 'col2': 'value2'}).model_dump_json.return_value = "mocked_json"
            with patch('config.GetModels.GetModels.get_model_by_path', return_value=[mock_model, ""]):
                # Act
                result = copper_etl.read_parquet_and_insert_to_clickhouse("test-bucket", "file1.parquet")

                # Assert
                assert len(result) == 1
                assert "Processed 1 records" in result[0]
                mock_s3_client.get_object.assert_called_once_with(Bucket="test-bucket", Key="file1.parquet")
                mock_clickhouse_client.execute.assert_any_call(
                    "INSERT INTO grupo4.data_ingestion (data_content, data_path, data_tag, id) VALUES",
                    [("mocked_json", "file1.parquet", "", "mocked_jsonfile1.parquet")]
                )

    # Caminho Triste
    @patch('config.Logger.Logger.msg')
    @patch('config.Logger.Logger.observability')
    def test_read_parquet_and_insert_to_clickhouse_failure(
        self, mock_observability, mock_msg, copper_etl, mock_s3_client, mock_clickhouse_client
    ):
        # Arrange
        mock_s3_client.get_object.side_effect = Exception("S3 Error")  # Simula erro no acesso ao S3

        # Act & Assert
        with pytest.raises(Exception, match="S3 Error"):
            copper_etl.read_parquet_and_insert_to_clickhouse("test-bucket", "file1.parquet")

        # Verifica se o S3 foi chamado com os parâmetros corretos
        mock_s3_client.get_object.assert_called_once_with(Bucket="test-bucket", Key="file1.parquet")

        # Certifique-se de que o logger não foi chamado neste fluxo
        mock_msg.assert_not_called()
