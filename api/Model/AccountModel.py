from typing import Optional
from pydantic import BaseModel

class AccountModel(BaseModel):
    id_account : Optional[int]
    user : Optional[str]
    password: Optional[str]
    abilitato: Optional[int]
    tipo_account: Optional[str]