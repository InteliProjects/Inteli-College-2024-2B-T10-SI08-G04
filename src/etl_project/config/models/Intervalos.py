import time
from pydantic import BaseModel, field_validator, field_serializer
from datetime import datetime
from typing import Optional

class Intervalos(BaseModel):
    dt_hora_minuto: str
    id_dt_hora_minuto: int
    hora_ini: datetime
    hora_fim: datetime
    duration_minutes: float

    @field_validator('hora_ini', 'hora_fim')
    def parse_optional_datetime(cls, value):
        if value is None or value == '':
            return None
        if isinstance(value, str):
            try:
                return datetime.strptime(value, '%Y-%m-%d %H:%M:%S')  # Formato ISO 8601 comum
            except ValueError as e:
                raise ValueError(f"Invalid datetime format: {e}")
        return value

    @field_serializer('hora_ini', 'hora_fim')
    def serialize_optional_datetime(self, value: Optional[datetime], _info):
        value = value.replace(year=datetime.now().year)
        return time.mktime(value.timetuple()) if value else None
