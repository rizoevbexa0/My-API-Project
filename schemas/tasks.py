from pydantic import BaseModel, Field, ConfigDict

class STransactionAdd(BaseModel):
    amount: float
    type: str
    description: str = Field(default="")

class STransaction(STransactionAdd):
    id: int
    model_config = ConfigDict(from_attributes=True)