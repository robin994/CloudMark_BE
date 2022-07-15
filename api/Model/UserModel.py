from typing import Optional
from pydantic import BaseModel

class UserModel(BaseModel):
    user : Optional[str]
    password: Optional[str]
    
class SessionModel(BaseModel):
    id_account:Optional[int]
    user:Optional[str]
    abilitato:Optional[str]
    tipo_account:Optional[str]