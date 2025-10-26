from fastapi import APIRouter
from database.userservice import (get_all_or_exact_user_db, create_user_db, add_phone_number_db)

user_router = APIRouter(prefix='/user', tags=["User API"])

@user_router.get('/get_all_or_exact_user_db')
async def get_all_or_exact_user(uid):
    result = get_all_or_exact_user_db(uid=uid)
    return {'status': 1, 'message': result}

@user_router.post('/create_user')
async def create_user(username, password):
    result = create_user_db(username=username, password=password)
    return {'status': 1, 'message': f'Пользователь {result} создан'}

@user_router.post('/add_phone_number')
async def add_phone_number(user_id, phone_number):
    result = add_phone_number_db(user_id=user_id, new_phone_number=phone_number)
    return {'status': 1, "message": f'Номер телефона {result} добавлен'}