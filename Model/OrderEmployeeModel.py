from datetime import date
from typing import Optional
from pydantic import BaseModel


class NewOrderEmployee(BaseModel):
    id_order: str
    id_employee: str
    rate: Optional[str]


class graphPayloadModel(BaseModel):
    id_business: str


class OrderEmployeeModel(BaseModel):
    id_order: str
    id_employee: str


class UpdateOrderEmployeeModel(BaseModel):
    old_order: NewOrderEmployee
    new_order: NewOrderEmployee


class OrderEmployJoinModel(NewOrderEmployee):
    startingDate: date
    endingDate: date
    name_emp: str
    surname_emp: str
    customer_name: str
