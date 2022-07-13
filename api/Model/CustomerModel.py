from pydantic import BaseModel

class CustomerModel(BaseModel):
    id: int
    name = str
    p_iva: str
    iban: str
    cap:str
    address: str
    phone: str
    email: str
    pec: str
    fax: str