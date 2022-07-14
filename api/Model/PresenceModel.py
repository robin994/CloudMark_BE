from datetime import date
from typing import Optional
from pydantic import BaseModel

class PresenceModel(BaseModel):
    id_employee: Optional[int]
    date_presence: Optional[date]
    typeof_presence: Optional[str]
    id_order: Optional[int]
    hours: Optional[int]