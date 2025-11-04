from fastapi import APIRouter, UploadFile, File
from database.photoservice import add_user_photo_db, add_campaign_photo_db
import random

photo_router = APIRouter(prefix='/photo', tags=['PhotoAPI'])

@photo_router.post('/add_campaign_photo')
async def main(cid: int, photo_file: UploadFile=File(...)):
    file_id = random.randint(1, 1000000)
    if photo_file:
        try:
            with open(f'database/images/campaign_photo/photo_{file_id}_{cid}.jpg', 'wb') as photo:
                photo_to_save = await photo_file.read()
                photo.write(photo_to_save)
                result = add_campaign_photo_db(cid = cid, photo_path=photo.name)
                if result:
                    return {'status': 1, "message": result}
                return {'status': 0, "message": "Проблема с бд"}

        except Exception as e:
            return {'status': 0, "message": False}
    return False

@photo_router.post('/add_user_photo')
async def main(uid: int, photo_file: UploadFile=File(...)):
    file_id = random.randint(1, 1000000)
    if photo_file:
        try:
            with open(f'database/images/user_photo/photo_{file_id}_{uid}.jpg', 'wb') as photo:
                photo_to_save = await photo_file.read()
                photo.write(photo_to_save)
                result = add_user_photo_db(uid = uid, photo_path=photo.name)
                if result:
                    return {'status': 1, "message": result}
                return {'status': 0, "message": "Проблема с бд"}

        except Exception as e:
            return {'status': 0, "message": False}
    return False