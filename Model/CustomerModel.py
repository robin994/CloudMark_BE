from datetime import date
from typing import Optional

from pydantic import BaseModel


class NewCustomerModel(BaseModel):
    name: Optional[str]
    p_iva: Optional[str]
    address: Optional[str]
    cap: Optional[str]
    iban: Optional[str]
    phone: Optional[str]
    email: Optional[str]
    pec: Optional[str]
    fax: Optional[str]
    id_business: Optional[str]


class CustomerModel(NewCustomerModel):
    id_customer: str


class CustomerHybridOrder(BaseModel):
    customer_name: str
    start_date: date
    end_date: date
    order_id: str
    rate: float
    id_customer: str
