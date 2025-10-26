from database import get_db
from database.models import User, Campaign, Comment


def get_all_campaign_db():
    db = next(get_db())
    return db.query(Campaign).all()

def get_all_comments_under_post_db(campaign_id):
    db = next(get_db())
    return db.query(Comment).filter_by(comment_campaign_id=campaign_id).all()

def get_all_campaign_by_user_db(user_id):
    db = next(get_db())
    return db.query(Campaign).filter_by(campaign_owner_user_id=user_id).all()

def create_comment_db(user_id, campaign_id, text):
    db = next(get_db())
    new_comment = Comment(comment_user_id=user_id, comment_campaign_id=campaign_id, text=text)
    db.add(new_comment)
    db.commit()
    return True

def create_campaign_db(name, campaign_owner_user_id, description, expected_sum=0):
    db = next(get_db())
    new_campaign = Campaign(name=name, description=description, campaign_owner_user_id=campaign_owner_user_id, expected_sum=expected_sum)
    db.add(new_campaign)
    db.commit()
    return True

def add_sum_on_campaign_db(campaign_id, summ):
    db = next(get_db())
    if summ:
        campaign = db.query(Campaign).filter_by(id=campaign_id).first()
        campaign.sum_now = campaign.sum_now + summ
        db.commit()
        return True
    return False