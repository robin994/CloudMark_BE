from datetime import date
from typing import List, Optional

from pydantic import BaseModel


class NewPresenceModel(BaseModel):
    id_employee: Optional[str]
    date_presence: Optional[date]
    id_tipoPresenza: Optional[str]
    id_order: Optional[str]
    hours: Optional[int]


class PresenceModel(NewPresenceModel):
    id_presence: str


class LoadPresenceModel(BaseModel):
    id_employee: str
    year: str
    month: str


class NewPresencesModel(BaseModel):
    presences: List[NewPresenceModel]


class PresenceFirstNameLastName(BaseModel):
    id_order: str
    id_business: str
    id_type_presence: str
    id_employee: str
    id_presence: str
    first_name: Optional[str]
    last_name: Optional[str]
    date_presence: Optional[date]
    tipoPresenza: Optional[str]
    nome_azienda: Optional[str]
    hours: Optional[int]
