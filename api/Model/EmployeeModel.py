from typing import Optional

from pydantic import BaseModel


class NewEmployeeModel(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    cf: Optional[str]
    iban: Optional[str]
    id_contractType: Optional[int]
    email: Optional[str]
    phoneNumber: Optional[str]


class EmployeeModel(NewEmployeeModel):
    id_employee: str
