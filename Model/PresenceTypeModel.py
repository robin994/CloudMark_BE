from typing import Optional
from pydantic import BaseModel


class NewPresenceTypeModel(BaseModel):
    name: Optional[str]
    percentage_increase: Optional[int]
    hourly_pay: Optional[int]

class PresenceTypeModel(NewPresenceTypeModel):
    id_presence_type: str