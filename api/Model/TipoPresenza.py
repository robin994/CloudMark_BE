from pydantic import BaseModel
from typing import Optional

class TipoPresenza(BaseModel):
    nomeTipoPresenza :Optional[str]
    percentualeMaggiorazione :Optional[int]
    pagaOraria :Optional[int]