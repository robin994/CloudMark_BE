from typing import Optional
from pydantic import BaseModel


class CallBackResponse(BaseModel):
    esitoChiamata: str
    numeroRisultati: int
    error: Optional[str]
