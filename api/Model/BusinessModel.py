from pydantic import BaseModel

class BusinessModel(BaseModel):
    id: int
    name = str
    p_iva: str
    iban: str
    address: str
    phone: str
    email: str
    cap:str
    pec:str
    fax:str