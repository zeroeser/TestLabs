from fastapi import FastAPI
from scheme.post import router, db

app = FastAPI()
app.include_router(router)


@app.on_event("startup")
async def startup():
    await db.connect()


@app.on_event("shutdown")
async def shutdown():
    await db.disconnect()





