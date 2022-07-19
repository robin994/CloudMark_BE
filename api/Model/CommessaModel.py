
from datetime import date
from typing import Optional
from pydantic import BaseModel
from uuid import UUID


class NewCommessaModel(BaseModel):
    description: Optional[str]
    id_customer: Optional[UUID]
    id_business: Optional[UUID]
    startDate: Optional[date]
    endDate: Optional[date]


class CommessaModel(NewCommessaModel):
    id_order: UUID
