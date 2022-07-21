from typing import Optional

from pydantic import BaseModel


class NewAccountModel(BaseModel):
    user: Optional[str]
    password: Optional[str]
    abilitato: Optional[int]
    id_tipo_account: Optional[int]


class AccountModel(NewAccountModel):
    id_account: str
