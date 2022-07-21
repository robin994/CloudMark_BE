from typing import Optional

from pydantic import BaseModel


class PresenceType(BaseModel):
    id_presence_type: Optional[int]
    name: Optional[str]
    percentage_increase: Optional[int]
    hourly_pay: Optional[int]
