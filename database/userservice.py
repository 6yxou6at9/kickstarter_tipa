from database import get_db
from database.models import User
from api.user_api.schemas import UserSchema


def get_all_or_exact_user_db(uid=0):
    db = next(get_db())
    if uid:
        exact_user = db.query(User).filter_by(id=uid).first()
        if exact_user:
            return db.query(User).filter_by(id=uid).all()
        return db.query(User).all()
    return False

def create_user_db(user: UserSchema):
    db = next(get_db())
    user_data = user.model_dump()
    new_user = User(**user_data)
    db.add(new_user)
    db.commit()
    return new_user.id

def add_phone_number_db(user_id, new_phone_number):
    db = next(get_db())
    exact_user = db.query(User).filter_by(id=user_id).first()
    exact_user.phone_number = new_phone_number
    db.commit()
    return True