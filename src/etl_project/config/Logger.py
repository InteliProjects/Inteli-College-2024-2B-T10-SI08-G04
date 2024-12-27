from prefect import task
from prefect.logging import get_run_logger
from config.Connections import Connections

class Logger():
    @staticmethod
    @task(name="logger_observability")
    def observability(metric_name, start_time, end_time, details):

        conn = Connections.get_postgres_connection()
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS modulo8si.observability_g4 (
                id SERIAL PRIMARY KEY,
                metric_name VARCHAR(255),
                start_time TIMESTAMP,
                end_time TIMESTAMP,
                duration INTERVAL,
                details TEXT
            )
        ''')

        duration = end_time - start_time
        cursor.execute('''
            INSERT INTO modulo8si.observability_g4 (metric_name, start_time, end_time, duration, details)
            VALUES (%s, %s, %s, %s, %s)
        ''', (metric_name, start_time, end_time, duration, details))

        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    @task(name="logger")
    def msg(msg, log_type, *args, **kwargs):
        logger = get_run_logger()
        types = {
            "info": logger.info,
            "debug": logger.debug,
            "warning": logger.warning,
            "error": logger.error,
            "exception": logger.exception,
            "critical": logger.critical
        }
        log_func = types[log_type]
        log_func(msg, *args, **kwargs)