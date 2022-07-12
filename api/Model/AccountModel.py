from pydantic import BaseModel

class AccountModel(BaseModel):
    id: int
    user = str
    password: str
    abilitato: bool
    tipo_acount: str