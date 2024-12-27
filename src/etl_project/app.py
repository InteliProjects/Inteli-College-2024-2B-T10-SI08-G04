from flask import Flask, jsonify, Response, request
from ETLs.CopperETL.CopperETL import CopperETL
from config.Settings import UseSettings
from middleware.middleware import AuthMiddleware

settings = UseSettings.get_settings()

app = Flask(__name__)

app.wsgi_app = AuthMiddleware(app.wsgi_app)

etl = CopperETL()

@app.route('/ingest_data', methods=['GET'])
def full_ingest():
    try:
        result = etl.ingest_data()
    except Exception as e:
        response = jsonify({
            'code': 500,
            'error': True,
            'msg': str(e)
        })
        response.status_code = 500
        return response
    
    response = jsonify({
            'code': 200,
            'error': False,
            'msg': result
    })
    response.status_code = 200

    return response

@app.route('/ingest_file', methods=['POST'])
def ingest_one_file():
    try:
        file_path = request.form.get('file_path')
        result = etl.read_parquet_and_insert_to_clickhouse(settings.BUCKET_NAME, file_path)
    except Exception as e:
        response = jsonify({
            'status': 500,
            'error': True,
            "msg": str(e)
        })  
        response.status_code = 500
        return response

    response = jsonify({
        'status': 200,
        'error': False,
        "msg": str(result)
    })

    response.status_code = 200
    return response
     
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
