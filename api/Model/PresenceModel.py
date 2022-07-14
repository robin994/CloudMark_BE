from typing import Optional
from pydantic import BaseModel

class PresenceModel(BaseModel):
    id: Optional[int]
    name = Optional[str]
    p_iva: Optional[str]
    iban: Optional[str]
    address: Optional[str]
    phone: Optional[str]
    email: Optional[str]
    pec: Optional[str]
    fax: Optional[str]