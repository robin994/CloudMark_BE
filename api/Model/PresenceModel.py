from datetime import date
from typing import Optional
from pydantic import BaseModel
from uuid import UUID


class NewPresenceModel(BaseModel):
    date_presence: Optional[date]
    id_tipoPresenza: Optional[int]
    id_order: UUID
    hours: Optional[int]


class PresenceModel(NewPresenceModel):
    id_employee: UUID
