from typing import Optional
from pydantic import BaseModel
from uuid import UUID


class NewEmployeeModel(BaseModel):
    nome: Optional[str]
    cognome: Optional[str]
    cf: Optional[str]
    iban: Optional[str]
    id_tipoContratto: Optional[int]
    email: Optional[str]
    telefono: Optional[str]


class EmployeeModel(NewEmployeeModel):
    id_employee: UUID
