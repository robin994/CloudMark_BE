from typing import Optional
from typing_extensions import Self
from pydantic import BaseModel
from pydantic.json import pydantic_encoder


class CallBackResponse(BaseModel):
    esitoChiamata: str
    numeroRisultati : int
    error: Optional[str]
    

