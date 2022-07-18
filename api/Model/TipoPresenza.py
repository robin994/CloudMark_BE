from pydantic import BaseModel
from typing import Optional

class TipoPresenza(BaseModel):
    id_tipoPresenza: Optional[int]
    nomeTipoPresenza :Optional[str]
    percentualeMaggiorazione :Optional[int]
    pagaOraria :Optional[int]