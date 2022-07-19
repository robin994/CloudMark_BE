from typing import Optional
from pydantic import BaseModel


class NewAccountModel(BaseModel):
    user: Optional[str]
    password: Optional[str]
    abilitate: Optional[int]
    id_accountType: Optional[int]


class AccountModel(NewAccountModel):
    id_account: str
