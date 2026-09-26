from fastapi import FastAPI
from database import engine, Model
from routers.tasks import router as router_transaction

app = FastAPI()
app.include_router(router_transaction)

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)

    print("База данных готова к работе !")