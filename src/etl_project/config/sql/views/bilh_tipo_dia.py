BILH_TIPO_DIA = '''
CREATE VIEW IF NOT EXISTS grupo4.bilh_tipo_dia AS WITH bilh_tipo_dia AS (
    SELECT 
		  tipo_bilhete,
		  data,
		  total_uso
    FROM 
		  grupo5.view_tipos_bilhete_por_dia 
)
SELECT 
    tipo_bilhete,
    data,
    total_uso
from
	bilh_tipo_dia
'''