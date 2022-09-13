
from datetime import date
from typing import Optional
from pip import List

from pydantic import BaseModel


class NewOrderModel(BaseModel):
    description: Optional[str]
    id_customer: Optional[str]
    id_business: Optional[str]
    startDate: Optional[date]
    endDate: Optional[date]


class OrderModel(NewOrderModel):
    id_order: str

class CustomerIDBusinessIDModel(BaseModel):
    id_customer: str
    id_business: str

class OrderEmployeeModel(BaseModel):
    id_order: str
    id_employee: str
    rate: Optional[int]
    