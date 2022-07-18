from typing import Optional
from uuid import UUID
from pydantic import BaseModel


class UserModel(BaseModel):
    user: Optional[str]
    password: Optional[str]


class SessionModel(BaseModel):
    id_account: Optional[str]
    user: Optional[str]
    abilitato: Optional[str]
    tipo_account: Optional[str]
