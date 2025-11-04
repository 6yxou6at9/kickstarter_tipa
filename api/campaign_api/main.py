from fastapi import APIRouter
from database.campaignservice import (get_all_campaign_db, get_all_campaign_by_user_db, create_campaign_db, get_exact_campaign_db, redact_campaign_db)
from api.campaign_api.schemas import CampaignSchema, CampaignRead

campaign_router = APIRouter(prefix='/campaign', tags=["Campaign API"])

def response_result(result):
    if result:
        return {"status": 1, 'message': result}
    return {'status': 0, 'message': result}

@campaign_router.get('/get_exact_campaign')
async def get_exact_campaign(cid):
    result = get_exact_campaign_db(cid=cid)
    return response_result(result)

@campaign_router.get('/get_all_campaign')
async def get_all_campaign():
    result = get_all_campaign_db()
    return response_result(result)

@campaign_router.get('/get_all_campaign_by_user')
async def get_all_campaign_by_user(user_id):
    result = get_all_campaign_by_user_db(user_id=user_id)
    return response_result(result)

@campaign_router.post('/create_campaign', response_model=CampaignRead)
async def create_campaign(campaign: CampaignSchema):
    result = create_campaign_db(campaign)
    return response_result(result)

@campaign_router.put('/redact_campaign')
def redact_campaign(cid, change_info, new_info):
    result = redact_campaign_db(cid=cid, change_info=change_info, new_info=new_info)
    return response_result(result)