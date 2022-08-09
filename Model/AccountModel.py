from typing import Optional
from pydantic import BaseModel


class NewAccountModel(BaseModel):
    user: Optional[str]
    password: Optional[str]
    abilitato: Optional[int]
    id_tipo_account: str


class AccountModel(NewAccountModel):
    id_account: str

class OtherAccountModel(BaseModel):
    id_account: str
    user: str
    abilitato: int
    id_tipo_account: str