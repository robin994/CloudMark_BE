from datetime import date
from typing import Optional
from pydantic import BaseModel
from uuid import UUID


class PresenceModel(BaseModel):
    id_employee: Optional[str]
    date_presence: Optional[date]
    id_tipoPresenza: Optional[int]
    id_order: Optional[str]
    hours: Optional[int]


    
