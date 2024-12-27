import sys
import os
from unittest.mock import Mock, patch
from datetime import datetime
import pytest
from config.Logger import Logger

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

@pytest.fixture
def mock_use_settings():
    mock_response = Mock()
    mock_response.POSTGRES_HOST = "localhost"
    mock_response.POSTGRES_PORT = "5432"
    mock_response.POSTGRES_DB = "test_db"
    mock_response.POSTGRES_USER = "test_user"
    mock_response.POSTGRES_PASSWORD = "test_password"
    with patch("config.Settings.UseSettings.get_settings", return_value=mock_response):
        yield mock_response

@pytest.fixture
def postgres_connection(mock_use_settings):
    with patch("config.Connections.Connections.get_postgres_connection") as mock_conn:
        mock_cursor = Mock()
        mock_conn.return_value.cursor.return_value = mock_cursor
        mock_conn.return_value.commit = Mock()
        mock_cursor.close = Mock()
        yield mock_conn

@pytest.fixture
def mock_logger():
    logger_instance = Mock()
    with patch("prefect.logging.get_run_logger", return_value=logger_instance):
        yield logger_instance

def test_logger_observability_creates_and_inserts_correctly(postgres_connection):
    mock_cursor = postgres_connection.return_value.cursor.return_value

    metric_name = "test_metric"
    start_time = datetime(2024, 12, 9, 10, 0, 0)
    end_time = datetime(2024, 12, 9, 10, 5, 0)
    details = "Test details"

    Logger.observability.fn(metric_name, start_time, end_time, details)

    create_table_sql = '''
        CREATE TABLE IF NOT EXISTS modulo8si.observability_g4 (
            id SERIAL PRIMARY KEY,
            metric_name VARCHAR(255),
            start_time TIMESTAMP,
            end_time TIMESTAMP,
            duration INTERVAL,
            details TEXT
        )
    '''
    insert_sql = '''
        INSERT INTO modulo8si.observability_g4 (metric_name, start_time, end_time, duration, details)
        VALUES (%s, %s, %s, %s, %s)
    '''

    normalize = lambda sql: ''.join(sql.split()).lower()

    executed_create_sql = normalize(mock_cursor.execute.mock_calls[0][1][0])
    expected_create_sql = normalize(create_table_sql)
    assert executed_create_sql == expected_create_sql, f"Expected: {expected_create_sql}, Got: {executed_create_sql}"

    executed_insert_sql = normalize(mock_cursor.execute.mock_calls[1][1][0])
    expected_insert_sql = normalize(insert_sql)
    assert executed_insert_sql == expected_insert_sql, f"Expected: {expected_insert_sql}, Got: {executed_insert_sql}"

    insert_args = mock_cursor.execute.mock_calls[1][1][1]
    expected_args = (metric_name, start_time, end_time, end_time - start_time, details)
    assert insert_args == expected_args, f"Expected args: {expected_args}, Got: {insert_args}"

    postgres_connection.return_value.commit.assert_called_once()
    mock_cursor.close.assert_called_once()

def test_logger_observability_raises_exception_on_connection_error(postgres_connection):
    postgres_connection.return_value.cursor.side_effect = Exception("Connection error")

    metric_name = "test_metric"
    start_time = datetime(2024, 12, 9, 10, 0, 0)
    end_time = datetime(2024, 12, 9, 10, 5, 0)
    details = "Test details"

    with pytest.raises(Exception, match="Connection error"):
        Logger.observability.fn(metric_name, start_time, end_time, details)

def test_logger_msg_logs_info_message_correctly():
    msg = "Test log message"
    log_type = "info"

    with patch("config.Logger.get_run_logger") as mock_get_logger:
        mock_logger = mock_get_logger.return_value
        mock_logger.info = Mock()

        Logger.msg.fn(msg, log_type)

        mock_logger.info.assert_called_once_with(msg)

def test_logger_msg_raises_exception_on_invalid_log_type():
    msg = "Test log message"
    log_type = "invalid"

    with patch("config.Logger.get_run_logger") as mock_get_logger:
        mock_logger = mock_get_logger.return_value

        with pytest.raises(KeyError, match="invalid"):
            Logger.msg.fn(msg, log_type)
