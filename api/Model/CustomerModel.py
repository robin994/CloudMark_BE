from typing import Optional
from pydantic import BaseModel
import uuid

class CustomerModel(BaseModel):
    id_customer: Optional[uuid.UUID]
    name: Optional[str]
    p_iva: Optional[str]
    address: Optional[str]
    cap: Optional[str]
    iban: Optional[str]
    phone: Optional[str]
    email: Optional[str]
    pec: Optional[str]
    fax: Optional[str]