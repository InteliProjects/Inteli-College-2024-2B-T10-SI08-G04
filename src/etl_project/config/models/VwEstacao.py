from pydantic import BaseModel

class VwEstacao(BaseModel):
    id_estacao: int
    tx_prefixo: str
    tx_nome: str
    cd_estacao_bu: int