import requests
import pandas as pd
import json
from config.Settings import UseSettings

class RequestsToBackend():
    @staticmethod
    def __get_base_request():
        settings = UseSettings.get_settings()
        url = settings.BACKEND_SERVER_ADDRESS + '/query'
        headers = {
            "Authorization": f"Bearer {settings.AUTH_TOKEN}",
            "Content-Type": "application/json"
        }
        return url, headers
    
    @staticmethod
    def query(query):
        try:
            url, headers = RequestsToBackend.__get_base_request()
            data = {
                "query": query
            }
            response = requests.post(url, headers=headers, json=data)
            if response.status_code == 200:
                result = response.json()['msg']
                return result
            else:
                raise Exception("Erro ao realizar a requisição ao backend", response.json())       
        except Exception as e:
            print("Erro ao tentar conectar ao backend")
            raise e
            
        
    def get_view_data(view_table, view_filter=""):
        query = f"SELECT * FROM grupo4.{view_table} {view_filter} LIMIT 100"
        result = RequestsToBackend.query(query)
        return pd.DataFrame(result['result_rows'], columns=result['column_names'])
    