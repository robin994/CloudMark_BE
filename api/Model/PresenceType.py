from typing import Optional

from pydantic import BaseModel


class PresenceType(BaseModel):
    id_presenceType: Optional[int]
    name: Optional[str]
    percentageIncrease: Optional[int]
    hourlyPay: Optional[int]
