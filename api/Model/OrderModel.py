from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class OrderModel(BaseModel):
    id : Optional[int]
    descrizione : Optional[str]
    id_cliente : Optional[int]
    id_azienda : Optional[int]
    data_inizio : Optional[datetime]
    data_fine : Optional[datetime]