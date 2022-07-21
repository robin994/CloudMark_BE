from datetime import date
from typing import Optional

from pydantic import BaseModel


class EmployeeBusinessModel(BaseModel):
    firstName: Optional[str]
    lastName: Optional[str]
    cf: Optional[str]
    matricola: Optional[str]
    startRelationshipDate: Optional[date]
