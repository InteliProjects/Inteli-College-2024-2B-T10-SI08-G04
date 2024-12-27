PCD_HORA_LINHA = '''
CREATE VIEW IF NOT EXISTS grupo4.pcd_hora_linha AS WITH pcd_linha_hora AS (
    SELECT DISTINCT
        JSONExtractInt(data_content, 'nr_qtde_pcd') AS nr_qtde_pcd,
        JSONExtractString(data_content, 'tx_descr_linha') AS tx_descr_linha, 
        toDateTime(toInt64OrNull(JSONExtractString(data_content, 'dt_origem'))) AS dt_origem,
        data_path
    FROM grupo4.data_ingestion
    WHERE data_tag = 'acompanhamento_pcd'
) 
SELECT
    HOUR(dt_origem) AS horario,
    toDate(dt_origem) AS data, 
    CASE 
        WHEN formatDateTime(dt_origem, '%w') = '0' THEN 'Domingo'
        WHEN formatDateTime(dt_origem, '%w') = '1' THEN 'Segunda-feira'
        WHEN formatDateTime(dt_origem, '%w') = '2' THEN 'Terça-feira'
        WHEN formatDateTime(dt_origem, '%w') = '3' THEN 'Quarta-feira'
        WHEN formatDateTime(dt_origem, '%w') = '4' THEN 'Quinta-feira'
        WHEN formatDateTime(dt_origem, '%w') = '5' THEN 'Sexta-feira'
        WHEN formatDateTime(dt_origem, '%w') = '6' THEN 'Sábado'
    END AS semana,
    tx_descr_linha,
    SUM(nr_qtde_pcd) AS total_qtde_pcd
FROM pcd_linha_hora
GROUP BY
    horario,
    data,
    semana,
    tx_descr_linha
ORDER BY
    data,
    horario,
    semana,
    tx_descr_linha;
    '''