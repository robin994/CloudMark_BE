from typing import Optional
from pydantic import BaseModel
from uuid import UUID


class NewAccountModel(BaseModel):
    user: Optional[str]
    password: Optional[str]
    abilitato: Optional[int]
    id_tipoAccount: Optional[int]


class AccountModel(NewAccountModel):
    id_account: UUID
