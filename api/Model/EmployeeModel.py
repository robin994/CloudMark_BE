from typing import Optional
from pydantic import BaseModel

class EmployeeModel(BaseModel):
    id_employee : Optional[int]
    nome : Optional[str]
    cognome : Optional[str]
    cf : Optional[str]
    iban : Optional[str]
    tipo_contratto: Optional[str]
    email : Optional[str]
    telefono : Optional[str]