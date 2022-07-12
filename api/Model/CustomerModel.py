from pydantic import BaseModel

class CustomerModel(BaseModel):
    id: int
    name = str
    p_iva: str
    iban: str
    address: str
    phone: str
    email: str
    pec: str
    fax: str