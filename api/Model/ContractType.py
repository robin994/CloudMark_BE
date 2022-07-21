from typing import Optional

from pydantic import BaseModel


class ContractType(BaseModel):
    id_contractType: Optional[int]
    name: Optional[str]
    info: Optional[str]
