from typing import Optional
from pydantic import BaseModel

class NewOrderEmployee(BaseModel):
    id_order: Optional[str]
    id_employee: Optional[str]
    rate: Optional[str]