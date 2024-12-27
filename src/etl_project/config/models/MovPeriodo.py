import time
from pydantic import BaseModel, field_serializer, field_validator
from datetime import datetime

class MovPeriodo(BaseModel):
    cod_bilh: int
    cd_estac_bu: int
    dt_validacao: datetime
    total_validacoes: int
    tipo_dia: str

    @field_validator('dt_validacao', mode="before")
    def parse_dt_validacao(cls, value):
        if isinstance(value, str):
            try:
                return datetime.strptime(value, '%m/%d/%y %H:%M:%S')
            except ValueError as e:
                raise ValueError(f"Invalid date format: {e}")
        return value

    @field_serializer('dt_validacao')
    def serialize_dt(self, dt_valicao: datetime, _info):
        return time.mktime(dt_valicao.timetuple())

