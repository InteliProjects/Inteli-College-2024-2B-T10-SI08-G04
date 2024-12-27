INTERVALOS_VIEW = '''
CREATE VIEW IF NOT EXISTS grupo4.intervalo AS WITH intervalo AS (
    SELECT DISTINCT
        JSONExtractString(data_content, 'dt_hora_minuto') AS dt_hora_minuto,
        JSONExtractInt(data_content, 'id_dt_hora_minuto') AS id_dt_hora_minuto,
        JSONExtractFloat(data_content, 'hora_ini') AS hora_ini,
        JSONExtractFloat(data_content, 'hora_fim') AS hora_fim,
        JSONExtractFloat(data_content, 'duration_minutes') AS duration_minutes,
        data_path
    FROM
        grupo4.data_ingestion
    WHERE
        data_tag = 'intervalos'
)
SELECT
    AVG(duration_minutes) AS avg_duration_minutes
FROM
    intervalo;
'''