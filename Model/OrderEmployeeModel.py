from typing import Optional
from pydantic import BaseModel


class NewOrderEmployee(BaseModel):
    id_order: str
    id_employee: str
    rate: Optional[str]


class graphPayloadModel(BaseModel):
    id_business: str
    month: int
    year: int


class OrderEmployeeModel(BaseModel):
    id_order: str
    id_employee: str


class UpdateOrderEmployeeModel(BaseModel):
    old_order: NewOrderEmployee
    new_order: NewOrderEmployee
