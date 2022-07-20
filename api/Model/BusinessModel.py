from typing import Optional
from pydantic import BaseModel
from uuid import UUID


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
