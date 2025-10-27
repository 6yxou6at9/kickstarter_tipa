from fastapi import APIRouter
from database.operationservice import (get_all_campaign_db, get_all_comments_under_post_db, get_all_campaign_by_user_db, create_comment_db, create_campaign_db, add_sum_on_campaign_db)

operation_router = APIRouter(prefix='/operation', tags=["Operation API"])

@operation_router.get('/get_all_campaign')
async def get_all_campaign():
    result = get_all_campaign_db()
    return {'status': 1, "message": result}

@operation_router.get('/get_all_comments_under_post')
async def get_all_comments_under_post(campaign_id):
    result = get_all_comments_under_post_db(campaign_id=campaign_id)
    return {'status': 1, "message": result}

@operation_router.get('/get_all_campaign_by_user')
async def get_all_campaign_by_user(user_id):
    result = get_all_campaign_by_user_db(user_id=user_id)
    return {'status': 1, "message": result}

@operation_router.post('/create_comment')
async def create_comment(user_id, campaign_id, text):
    result = create_comment_db(user_id=user_id, campaign_id=campaign_id, text=text)
    return {'status': 1, "message": f'Комментарий {result} создан'}

@operation_router.post('/create_campaign')
async def create_campaign(name, campaign_owner_user_id, description, expected_sum=0):
    result = create_campaign_db(name=name, campaign_owner_user_id=campaign_owner_user_id, description=description, expected_sum=expected_sum)
    return {'status': 1, "message": f'Кампэйн {result} создан'}

@operation_router.post('/add_sum_on_campaign')
async def add_sum_on_campaign(campaign_id: int, summ: int):
    result = add_sum_on_campaign_db(campaign_id=campaign_id, summ=summ)
    return {'status': 1, "message": f'Сумма {result} добавлена'}