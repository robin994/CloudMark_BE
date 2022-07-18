from datetime import date
from typing import Optional
from pydantic import BaseModel

class EmployeeBusinessModel(BaseModel):
    nome : Optional[str]
    cognome : Optional[str]
    cf : Optional[str]
    matricola : Optional[str]
    inizio_data_rapporto : Optional[date]