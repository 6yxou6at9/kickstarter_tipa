from database import get_db
from database.models import Comment
from api.comment_api.schemas import CommentSchema

def get_exact_comment_db (com_id):
    db = next(get_db())
    return db.query(Comment).filter_by(id=com_id).first()

def get_all_comments_by_user_db(user_id):
    db = next(get_db())
    return db.query(Comment).filter_by(comment_user_id=user_id).all()

def get_all_comments_under_campaign_db(campaign_id):
    db = next(get_db())
    return db.query(Comment).filter_by(comment_campaign_id=campaign_id).all()

def create_comment_db(comment: CommentSchema):
    db = next(get_db())
    new_comment = Comment(**comment.model_dump())
    db.add(new_comment)
    db.commit()
    return True

