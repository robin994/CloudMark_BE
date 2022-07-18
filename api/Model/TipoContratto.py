from typing import Optional
from pydantic import BaseModel


class TipoContratto(BaseModel):
    id_tipoContratto: Optional[int]
    name: Optional[str]
    info: Optional[str]
