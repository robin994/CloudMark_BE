from typing import Optional

from pydantic import BaseModel

from Model.EmployeeModel import AccountEmployeeModel


class UserModel(BaseModel):
    user: Optional[str]
    password: Optional[str]


class SessionModel(BaseModel):
    id_account: str
    user: str
    abilitate: str
    accountType: str
    accountTypeName: str
    accountListFunction: Optional[str]
    id_employee: str
    employee: object


class ResetPasswordModel(BaseModel):
    password_employee: Optional[str]
    id_employee: Optional[str]
    session_admin: Optional[str]
