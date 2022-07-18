
from datetime import date
from typing import Optional
from pydantic import BaseModel
from uuid import UUID


class NewCommessaModel(BaseModel):
    id_order: UUID
    descrizione: Optional[str]
    id_cliente: Optional[UUID]
    id_azienda: Optional[UUID]
    data_inizio: Optional[date]
    data_fine: Optional[date]


class CommessaModel(NewCommessaModel):
    id_order: UUID
