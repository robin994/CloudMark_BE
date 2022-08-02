from typing import Any, Optional

from pydantic import BaseModel


class CallBackResponseModel(BaseModel):
    data: Optional[Any]
    length: Optional[int]
    description: Optional[str]
    status: str
