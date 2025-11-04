from database import get_db
from database.models import CampaignPhoto, UserPhoto
from database.campaignservice import campaign_with_id
from database.userservice import user_with_id


def add_user_photo_db(uid, photo_path):
    db = next(get_db())
    if user_with_id(uid):
        new_photo = UserPhoto(uid=uid, photo_path=photo_path)
        db.add(new_photo)
        db.commit()
        return True
    return False

def add_campaign_photo_db(cid, photo_path):
    db = next(get_db())
    if campaign_with_id(cid):
        new_photo = CampaignPhoto(cid=cid, photo_path=photo_path)
        db.add(new_photo)
        db.commit()
        return True
    return False