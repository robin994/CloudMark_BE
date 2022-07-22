from typing import Optional
from pydantic import BaseModel


class NewPresenceType(BaseModel):
    name: Optional[str]
    percentage_increase: Optional[int]
    hourly_pay: Optional[int]

class PresenceType(NewPresenceType):
    id_presence_type: str