from typing import Optional

from pydantic import BaseModel


class NewAccountType(BaseModel):
    accountTypeName: Optional[str]
    function: Optional[str]

class AccountType(NewAccountType):
    id_account_type: str