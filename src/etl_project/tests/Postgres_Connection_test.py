import pytest
from unittest.mock import Mock, patch
from psycopg2 import OperationalError
from config.Connections import Connections

class TestPostgresConnections:
    """
    Classe de testes para verificar as conexões com o banco de dados Postgres.

    Métodos:
    --------
    postgres_env(mocker):
        Fixture que configura um ambiente de teste com configurações válidas para o Postgres.
    
    postgres_env_invalid(mocker):
        Fixture que configura um ambiente de teste com configurações inválidas para o Postgres.

    test_postgres_connection_successful(mock_connect, postgres_env):
        Testa se a conexão com o Postgres é bem-sucedida usando configurações válidas.
        - Mocka a função de conexão do psycopg2 para retornar uma conexão simulada.
        - Verifica se a conexão retornada não é None.
        - Verifica se a função de conexão foi chamada com os parâmetros corretos.

    test_postgres_connection_failure(mock_connect, postgres_env_invalid):
        Testa se a conexão com o Postgres falha ao usar configurações inválidas.
        - Mocka a função de conexão do psycopg2 para lançar uma exceção OperationalError.
        - Verifica se a exceção OperationalError é levantada com a mensagem esperada.
        - Verifica se a função de conexão foi chamada com os parâmetros corretos.
    """
    @pytest.fixture
    def postgres_env(self, mocker):
        mock_response = Mock()
        mock_response.POSTGRES_HOST = 'localhost'
        mock_response.POSTGRES_PORT = 5432
        mock_response.POSTGRES_DB = 'test_db'
        mock_response.POSTGRES_USER = 'test_user'
        mock_response.POSTGRES_PASSWORD = 'test_password'
        mocker.patch('config.Settings.UseSettings.get_settings', return_value=mock_response)

    @pytest.fixture
    def postgres_env_invalid(self, mocker):
        mock_response = Mock()
        mock_response.POSTGRES_HOST = 'invalid_host'
        mock_response.POSTGRES_PORT = 5432
        mock_response.POSTGRES_DB = 'test_db'
        mock_response.POSTGRES_USER = 'test_user'
        mock_response.POSTGRES_PASSWORD = 'test_password'
        mocker.patch('config.Settings.UseSettings.get_settings', return_value=mock_response)

    @patch('config.Connections.psycopg2.connect')
    def test_postgres_connection_successful(self, mock_connect, postgres_env):
        mock_connect.return_value = Mock()
        connection = Connections.get_postgres_connection()
        assert connection is not None
        mock_connect.assert_called_once_with(
            host='localhost',
            port=5432,
            dbname='test_db',
            user='test_user',
            password='test_password'
        )

    @patch('config.Connections.psycopg2.connect')
    def test_postgres_connection_failure(self, mock_connect, postgres_env_invalid):
        mock_connect.side_effect = OperationalError("Unable to connect to database")
        with pytest.raises(OperationalError, match="Unable to connect to database"):
            Connections.get_postgres_connection()
        mock_connect.assert_called_once_with(
            host='invalid_host',
            port=5432,
            dbname='test_db',
            user='test_user',
            password='test_password'
        )
