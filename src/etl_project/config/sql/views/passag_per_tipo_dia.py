PASSAG_PER_TIPO_DIA = '''
CREATE VIEW IF NOT EXISTS grupo4.passag_per_tipo_dia AS WITH periodo AS (
    SELECT DISTINCT 
		JSONExtractInt(data_content, 'cd_estac_bu') AS cd_estac_bu,
		JSONExtractInt(data_content, 'total_validacoes') AS total_validacoes,
		JSONExtractInt(data_content, 'cod_bilh') AS cod_bilh,
		JSONExtractInt(data_content, 'dt_validacao') AS dt_validacao,
		JSONExtractString(data_content, 'tipo_dia') AS tipo_dia
    FROM 
		grupo4.data_ingestion
    WHERE 
		data_tag = 'dmo_anl_vw_tot_mov_periodo'
)
SELECT 
    SUM(periodo.total_validacoes) AS total_validacoes,
    periodo.tipo_dia
FROM 
    periodo
GROUP BY
	periodo.tipo_dia
'''