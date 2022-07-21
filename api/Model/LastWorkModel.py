from datetime import date
from typing import Optional

from pydantic import BaseModel


class LastWorkModel(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    matricola: Optional[str]
    cf: Optional[str]
    intakeDate: Optional[date]
