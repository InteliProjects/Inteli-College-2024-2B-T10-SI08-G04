ACOMPANHAMENTO_PCD = '''
CREATE VIEW IF NOT EXISTS grupo4.pcd AS WITH pcd AS (
    SELECT DISTINCT
        JSONExtractInt(data_content, 'nr_qtde_pcd') AS nr_qtde_pcd,
        JSONExtractString(data_content, 'tx_descr_linha') AS tx_descr_linha, 
        JSONExtractString(data_content, 'grupos_pcd') AS grupos_pcd,
        data_path
    FROM grupo4.data_ingestion
    WHERE data_tag = 'acompanhamento_pcd'
) 
SELECT 
    tx_descr_linha,
    grupos_pcd,
    SUM(nr_qtde_pcd) AS total_qtde_pcd
FROM pcd
GROUP BY 
    tx_descr_linha, 
    grupos_pcd
ORDER BY 
    tx_descr_linha, 
    grupos_pcd;
    
    '''