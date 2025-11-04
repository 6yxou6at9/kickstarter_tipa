from fastapi import APIRouter
from database.commentservice import create_comment_db, get_all_comments_under_campaign_db, get_exact_comment_db, get_all_comments_by_user_db
from api.comment_api.schemas import CommentSchema, CommentRead

comment_router = APIRouter(prefix='/comment', tags=["Comment API"])

def response_result(result):
    if result:
        return {"status": 1, 'message': result}
    return {'status': 0, 'message': result}

@comment_router.post('/create_comment', response_model=CommentRead)
async def create_comment(comment: CommentSchema):
    result = create_comment_db(comment)
    return response_result(result)

@comment_router.get('/get_all_comments_under_campaign')
async def get_all_comments_under_post(pid):
    result = get_all_comments_under_campaign_db(campaign_id=pid)
    return response_result(result)

@comment_router.get('/get_exact_comment')
async def get_exact_comment(com_id):
    result = get_exact_comment_db(com_id=com_id)
    return response_result(result)

@comment_router.get('/get_all_comments_by_user')
async def get_all_comments_by_user(uid):
    result = get_all_comments_by_user_db(user_id=uid)
    return response_result(result)