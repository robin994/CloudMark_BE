from typing import Any, Optional

from pydantic import BaseModel


class CallBackResponseModel(BaseModel):
    data: Optional[dict]
    lenght: Optional[int]
    description: Optional[str]
    error: Optional[str]
