
from datetime import date
from typing import Optional
from pydantic import BaseModel

class CommessaModel(BaseModel):
    id_order : Optional[int]
    descrizione : Optional[str]
    id_cliente : Optional[int]
    id_azienda : Optional[int]
    data_inizio : Optional[date]
    data_fine : Optional[date]