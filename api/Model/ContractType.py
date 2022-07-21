from typing import Optional
from pydantic import BaseModel

class NewContractTypeModel(BaseModel):
    name: Optional[str]
    info: Optional[str]

class ContractTypeModel(NewContractTypeModel):
    id_contract_type: Optional[str]
