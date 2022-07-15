from typing import Optional
from pydantic import BaseModel

class TipoContratto(BaseModel):
    name: Optional[str]
    info: Optional[str]