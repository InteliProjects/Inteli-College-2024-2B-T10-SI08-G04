from flask import Flask, jsonify, Response, request
from config.Settings import UseSettings
from config.Clickhouse import Clickhouse
from middleware.middleware import AuthMiddleware

settings = UseSettings.get_settings()

app = Flask(__name__)

app.wsgi_app = AuthMiddleware(app.wsgi_app)

@app.route('/query', methods=['POST'])
def ingest_one_file():
    try:
        data = request.get_json()
        query = data.get('query')
        clickhouse_obj = Clickhouse.query(query=query)
        result = {
            "result_rows": clickhouse_obj.result_rows, 
            "column_names": clickhouse_obj.column_names
        }
    except Exception as e:
        response = jsonify({
            "status": 500,
            "error": True,
            "msg": str(e)
        })  
        response.status_code = 500
        return response

    response = jsonify({
        "status": 200,
        "error": False,
        "msg": result
    })

    response.status_code = 200
    return response
     
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7000, debug=True)
