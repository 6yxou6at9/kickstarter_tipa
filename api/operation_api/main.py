from fastapi import APIRouter
from database.operationservice import (get_all_campaign_db, get_all_comments_under_post_db, get_all_campaign_by_user_db, create_comment_db, create_campaign_db, add_sum_on_campaign_db)
from api.operation_api.schemas import (CampaignSchema, CommentSchema, TransferSchema, SchemaRead)

operation_router = APIRouter(prefix='/operation', tags=["Operation API"])

def response_result(result):
    if result:
        return {"status": 1, 'message': result}
    return {'status': 0, 'message': result}

@operation_router.get('/get_all_campaign')
async def get_all_campaign():
    result = get_all_campaign_db()
    return response_result(result)

@operation_router.get('/get_all_comments_under_post')
async def get_all_comments_under_post(campaign_id):
    result = get_all_comments_under_post_db(campaign_id=campaign_id)
    return response_result(result)

@operation_router.get('/get_all_campaign_by_user')
async def get_all_campaign_by_user(user_id):
    result = get_all_campaign_by_user_db(user_id=user_id)
    return response_result(result)

@operation_router.post('/create_comment', response_model=SchemaRead)
async def create_comment(comment: CommentSchema):
    result = create_comment_db(comment)
    return response_result(result)

@operation_router.post('/create_campaign', response_model=SchemaRead)
async def create_campaign(campaign: CampaignSchema):
    result = create_campaign_db(campaign)
    return response_result(result)


@operation_router.post('/add_sum_on_campaign', response_model=SchemaRead)
async def add_sum_on_campaign(transfer: TransferSchema):
    result = add_sum_on_campaign_db(transfer)
    return response_result(result)