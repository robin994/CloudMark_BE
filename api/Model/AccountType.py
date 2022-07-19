from typing import Optional
from pydantic import BaseModel


class AccountType(BaseModel):
    id_account_type: Optional[int]
    accountTypeName: Optional[str]
    function: Optional[str]
