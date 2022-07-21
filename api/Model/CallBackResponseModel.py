from typing import Any, Optional

from pydantic import BaseModel


class CallBackResponseModel(BaseModel):
    data: Optional[dict]
    length: Optional[int]
    description: Optional[str]
    error: Optional[str]
    