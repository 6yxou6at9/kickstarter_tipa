from fastapi import APIRouter
from database.userservice import (get_all_or_exact_user_db, create_user_db, change_phone_number_db)
from api.user_api.schemas import UserSchema, UserRead

user_router = APIRouter(prefix='/user', tags=["User API"])

def response_result(result):
    if result:
        return {"status": 1, 'message': result}
    return {'status': 0, 'message': result}

@user_router.get('/get_all_or_exact_user_db')
async def get_all_or_exact_user(uid):
    result = get_all_or_exact_user_db(uid=uid)
    return {'status': 1, 'message': result}

@user_router.post('/create_user', response_model=UserRead)
async def create_user_api(user: UserSchema):
    result = create_user_db(user)
    return response_result(result)

@user_router.post('/change_phone_number')
async def change_phone_number(user_id, phone_number):
    result = change_phone_number_db(user_id=user_id, new_phone_number=phone_number)
    return response_result(result)