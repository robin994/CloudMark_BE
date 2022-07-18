from typing import Optional
from pydantic import BaseModel

class TipoAccount(BaseModel):
    id_tipoAccount: Optional[int]
    nomeTipoAccount : Optional[str]
    funzioneProfilo : Optional[str]