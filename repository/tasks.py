from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from schemas.tasks import STransactionAdd
from models.tasks import Transaction

class RepositoryTransaction:
    @classmethod
    async def add_one(cls, data: STransactionAdd, session: AsyncSession):
        transaction = Transaction(**data.model_dump())
        session.add(transaction)
        await session.commit()
        return transaction
    
    @classmethod
    async def find_all(cls, session: AsyncSession):
        query = select(Transaction)
        result = await session.execute(query)
        transaction = result.scalars().all()
        return transaction