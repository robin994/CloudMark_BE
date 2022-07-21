from typing import Optional

from pydantic import BaseModel


class CallBackResponse(BaseModel):
    outcome: str
    resultsNum: int
    error: Optional[str]
