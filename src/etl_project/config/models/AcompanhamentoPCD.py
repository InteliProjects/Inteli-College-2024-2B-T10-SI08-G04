import time
from pydantic import BaseModel, field_validator, field_serializer
from datetime import datetime
from typing import Optional

class AcompanhamentoPCD(BaseModel):
    dt_destino: Optional[datetime]
    dt_operacional: Optional[datetime]
    dt_origem: Optional[datetime]
    fl_alerta: Optional[float]
    grupos_pcd: str
    id_carro: int
    id_estacao_alerta: int
    id_estacao_destino: int
    id_estacao_origem: int
    id_registro: int
    id_tipo_pcd: int
    nr_ordem: int
    nr_posicao_carro: int
    nr_qtde_pcd: int
    tx_cor_linha: str
    tx_descr_linha: str
    tx_estacao_destino: str
    tx_linha: int
    tx_obs: str
    tx_porta: int
    tx_prefixo: str
    tx_tipo_pcd: str
    tx_trem: str
    tx_username_destino: str
    tx_username_origem: str

    @field_validator('dt_destino', 'dt_operacional', 'dt_origem')
    def parse_optional_datetime(cls, value):
        if value is None or value == '':
            return None
        if isinstance(value, str):
            try:
                return datetime.strptime(value, '%m/%d/%y %H:%M:%S')
            except ValueError as e:
                raise ValueError(f"Invalid datetime format: {e}")
        return value

    @field_serializer('dt_destino', 'dt_operacional', 'dt_origem')
    def serialize_optional_datetime(self, value: Optional[datetime], _info):
        return time.mktime(value.timetuple()) if value else None