from datetime import date
from typing import Optional

from pydantic import BaseModel


class NewBusinessModel(BaseModel):
    name: Optional[str]
    p_iva: Optional[str]
    address: Optional[str]
    cap: Optional[str]
    iban: Optional[str]
    phone: Optional[str]
    email: Optional[str]
    pec: Optional[str]
    fax: Optional[str]


class BusinessModel(NewBusinessModel):
    id_business: Optional[str]

class BusinessStartEnd(BaseModel):
    id_business: str
    start_date: Optional[date]
    end_date: Optional[date]
    serial_num: Optional[int]