from datetime import date, datetime
from typing import Optional

from pydantic import BaseModel

from Model.AccountModel import AccountModel, NewAccountModel
from Model.BusinessModel import BusinessStartEnd


class NewEmployeeModel(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    cf: Optional[str]
    iban: Optional[str]
    id_contractType: Optional[str]
    email: Optional[str]
    phoneNumber: Optional[str]


class EmployeeModel(NewEmployeeModel):
    id_employee: str


class NewAccountEmployeeModel(BaseModel):
    new_employee: NewEmployeeModel
    new_account: NewAccountModel
    id_business: str
    start_date: date
    end_date: Optional[date]
    serial_num: Optional[int]


class AccountEmployeeModel(BaseModel):
    employee: EmployeeModel
    account: AccountModel
    id_business: str
    start_date: date
    end_date: Optional[date]
    serial_num: Optional[int]
    
class AccountEmployeeBusiness(BaseModel):
    employee: EmployeeModel
    account: AccountModel
    business: BusinessStartEnd

class EmlpoyeeOrderModel(BaseModel):
    id_employee : Optional[str]
    first_name : Optional[str]
    email : Optional[str]
    phone_number : Optional[str]
    last_name : Optional[str]
    cf : Optional[str]
    id_order: Optional[str]
