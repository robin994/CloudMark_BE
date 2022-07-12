from typing import Optional
from pydantic import BaseModel

class TipoAccount(BaseModel):
    nomeTipoAccount : Optional[str]
    funzioneProfilo : Optional[str]