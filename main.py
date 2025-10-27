from fastapi import FastAPI, Request
from api.user_api.main import user_router
from api.operation_api.main import operation_router
from database import Base, engine


app = FastAPI(docs_url='/docs', redoc_url='/redoc', title="Tipa_Kickstarter_API")
app.include_router(user_router)
app.include_router(operation_router)
Base.metadata.create_all(engine)

@app.get('/')
async def main(request: Request):
    return 'Привет'