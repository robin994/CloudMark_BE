from pydantic import BaseModel
from typing import Optional


class PresenceType(BaseModel):
    id_presenceType: Optional[int]
    name: Optional[str]
    percentageIncrease: Optional[int]
    hourlyPay: Optional[int]
