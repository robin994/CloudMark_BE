from typing import Optional
from pydantic import BaseModel

class AccountModel(BaseModel):
    id : Optional[int]
    user = Optional[str]
    password: Optional[str]
    abilitato: Optional[bool]
    tipo_acount: Optional[str]