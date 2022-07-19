
from datetime import date
from typing import Optional
from pydantic import BaseModel
from uuid import UUID


class NewOrderModel(BaseModel):
    description: Optional[str]
    id_customer: Optional[str]
    id_business: Optional[str]
    startDate: Optional[date]
    endDate: Optional[date]


class OrderModel(NewOrderModel):
    id_order: str
