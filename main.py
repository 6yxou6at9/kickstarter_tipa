from fastapi import FastAPI, Request
from api.user_api.main import user_router
from api.operation_api.main import operation_router
from database import Base, engine
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


app = FastAPI(docs_url='/docs', redoc_url='/redoc', title="Tipa_Kickstarter_API")
app.include_router(user_router)
app.include_router(operation_router)
templates = Jinja2Templates(directory="templates")
Base.metadata.create_all(engine)

@app.get('/', response_class=HTMLResponse)
async def main(request: Request):
    return templates.TemplateResponse(request, name='index.html')