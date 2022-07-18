from typing import Optional
from pydantic import BaseModel


class TipoAccount(BaseModel):
    id_tipo_account: Optional[int]
    nomeTipoAccount: Optional[str]
    funzioneProfilo: Optional[str]
