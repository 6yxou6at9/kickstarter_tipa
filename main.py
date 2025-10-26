from fastapi import FastAPI, Request
from api import user_api, operation_api
from api.user_api import user_router
from api.operation_api import operation_router
from database import Base, engine


app = FastAPI(docs_url='/docs', redoc_url='/redoc', title="MyFirstAPI")
app.include_router(user_router)
app.include_router(operation_router)
Base.metadata.create_all(engine)

@app.get('/')
async def main(request: Request):
    return 'Привет'