from sqlalchemy.orm import Mapped, mapped_column
from database import Model

class Transaction(Model):
    __tablename__ = "transaction" 
    id: Mapped[int] = mapped_column(primary_key=True)
    amount: Mapped[float]
    type: Mapped[str]
    description: Mapped[str]
