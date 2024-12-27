import time
from pydantic import BaseModel, field_serializer, field_validator
from datetime import datetime


class BilhTipoDia(BaseModel):
    tipo_bilhete: str
    data: datetime
    total_uso: int

    @field_validator('data', mode="before")
    def parse_dt_validacao(cls, value):
        if isinstance(value, str):
            try:
                return datetime.strptime(value, '%m/%d/%y %H:%M:%S')
            except ValueError as e:
                raise ValueError(f"Invalid date format: {e}")
        return value

    @field_serializer('data')
    def serialize_dt(self, data: datetime, _info):
        return time.mktime(data.timetuple())