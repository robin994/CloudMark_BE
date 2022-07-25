from datetime import date
from typing import Optional

from pydantic import BaseModel


class NewPresenceModel(BaseModel):
    id_employee: Optional[str]
    date_presence: Optional[date]
    id_tipoPresenza: Optional[str]
    id_order: Optional[str]
    hours: Optional[int]
    
class PresenceModel(NewPresenceModel):
    id_presence : Optional[str]

class LoadPresenceModel(BaseModel):
  id_employee: str
  year: str
  month: str
    
