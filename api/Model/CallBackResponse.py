from typing import Optional
from fastapi import Response
from pydantic import BaseModel


class CallBackResponse(BaseModel):
    esitoChiamata: str
    numeroRisultati : int
    error : Optional[str]
    
