from datetime import date
from typing import Optional
from pydantic import BaseModel


class LastWorkModel(BaseModel):
    nome: Optional[str]
    cognome: Optional[str]
    matricola: Optional[str]
    cf: Optional[str]
    data_assunzione: Optional[date]
