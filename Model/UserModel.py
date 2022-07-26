from typing import Optional

from pydantic import BaseModel


class UserModel(BaseModel):
    user: Optional[str]
    password: Optional[str]


class SessionModel(BaseModel):
    id_account: Optional[str]
    user: Optional[str]
    abilitate: Optional[str]
    accountType: Optional[str]

class ResetPasswordModel(BaseModel):
    password_employee:Optional[str]
    id_employee : Optional[str] 
    session_admin : Optional[str]