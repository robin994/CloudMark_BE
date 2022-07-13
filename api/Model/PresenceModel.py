from pydantic import BaseModel

class PresenceModel(BaseModel):
    id: int
    name = str
    p_iva: str
    iban: str
    address: str
    phone: str
    email: str
    pec: str
    fax: str