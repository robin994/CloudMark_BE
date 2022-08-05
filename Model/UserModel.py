from typing import Optional

from pydantic import BaseModel

from Model.EmployeeModel import AccountEmployeeModel


class UserModel(BaseModel):
    user: Optional[str]
    password: Optional[str]


class SuperModel(BaseModel):
    id_account: str
    user: str
    abilitate: str
    accountType: str
    accountTypeName: str
    accountListFunction: Optional[str]


class SessionModel(SuperModel):
    id_employee: str
    employee_first_name: str
    employee_last_name: str
    employee_email: str
    employee_phone_number: str
    business_name: str
    business_p_iva: str
    business_address: str
    business_cap: str
    business_iban: str
    business_phone: str
    business_email: str
    business_pec: str
    business_fax: str


class ResetPasswordModel(BaseModel):
    password_employee: Optional[str]
    id_employee: Optional[str]
    session_admin: Optional[str]
