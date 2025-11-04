from fastapi import FastAPI, Request
from api.user_api.main import user_router
from api.campaign_api.main import campaign_router
from api.transfer_api.main import transfer_router
from api.comment_api.main import comment_router
from api.photo_api.main import photo_router
from database import Base, engine
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from database.userservice import *
from database.commentservice import *
from database.campaignservice import *
from database.transferservice import *
from database.photoservice import *


app = FastAPI(docs_url='/docs', redoc_url='/redoc', title="Tipa_Kickstarter_API")
app.include_router(user_router)
app.include_router(campaign_router)
app.include_router(transfer_router)
app.include_router(comment_router)
app.include_router(photo_router)
templates = Jinja2Templates(directory="templates")
Base.metadata.create_all(engine)

@app.get('/profile/{uid}', response_class=HTMLResponse)
async def main(request: Request, uid: int):
    exact_user = get_all_or_exact_user_db(uid=uid)
    return templates.TemplateResponse("profile.html", {"request": request, "exact_user": exact_user})