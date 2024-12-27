import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

import pytest
from moto import mock_aws
from unittest.mock import Mock
from config.Connections import Connections
from botocore.exceptions import PartialCredentialsError

class TestAWSConnections:
    @pytest.fixture
    def s3_env(self, mocker):
        mock_response = Mock()
        mock_response.AWS_ACCESS_KEY = 'fake_access_key'
        mock_response.AWS_SECRET_KEY = 'fake_secret_key'
        mock_response.AWS_SESSION_TOKEN = 'fake_session_token'
        mock_response.AWS_REGION = 'us-east-1'
        
        mocker.patch('config.Settings.UseSettings.get_settings', return_value=mock_response)

    @pytest.fixture
    def s3_connection(self, s3_env):
        with mock_aws():
            client = Connections.get_s3_client()
            client.create_bucket(Bucket='my-test-bucket')
            yield client

    @pytest.fixture
    def s3_env_without_access_key(self, mocker):
        mock_response = Mock()
        mock_response.AWS_ACCESS_KEY = None
        mock_response.AWS_SECRET_KEY = 'fake_secret_key'
        mock_response.AWS_SESSION_TOKEN = 'fake_session_token'
        mock_response.AWS_REGION = 'us-east-1'
        
        mocker.patch('config.Settings.UseSettings.get_settings', return_value=mock_response)


    def test_s3_connection_with_all_data(self, s3_connection):
        assert s3_connection is not None
        assert hasattr(s3_connection, 'list_buckets')
        
        response = s3_connection.list_buckets()
        buckets = [bucket['Name'] for bucket in response['Buckets']]
        assert 'my-test-bucket' in buckets

    def test_s3_connection_without_access_key(self, s3_env_without_access_key):
        with pytest.raises(PartialCredentialsError):
            Connections.get_s3_client()