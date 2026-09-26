from fastapi import APIRouter
from database import SessionDep
from schemas.tasks import STransaction, STransactionAdd
from repository.tasks import RepositoryTransaction


router = APIRouter(prefix="/transactions", tags=["Банк"])

@router.post("")
async def post_transaction(data: STransactionAdd, session: SessionDep) -> STransaction:
    return await RepositoryTransaction.add_one(data, session)

@router.get("")
async def get_transaction(session: SessionDep) -> list[STransaction]:
    return await RepositoryTransaction.find_all(session)