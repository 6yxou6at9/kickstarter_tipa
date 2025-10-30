from database import get_db
from database.models import Campaign, Comment, Transfer
from api.operation_api.schemas import CampaignSchema, CommentSchema, TransferSchema


def get_all_campaign_db():
    db = next(get_db())
    return db.query(Campaign).all()

def get_all_comments_under_post_db(campaign_id):
    db = next(get_db())
    return db.query(Comment).filter_by(comment_campaign_id=campaign_id).all()

def get_all_campaign_by_user_db(user_id):
    db = next(get_db())
    return db.query(Campaign).filter_by(campaign_owner_user_id=user_id).all()

def create_comment_db(comment: CommentSchema):
    db = next(get_db())
    new_comment = Comment(**comment.model_dump())
    db.add(new_comment)
    db.commit()
    return True

def create_campaign_db(campaign: CampaignSchema):
    db = next(get_db())
    new_campaign = Campaign(**campaign.model_dump())
    db.add(new_campaign)
    db.commit()
    return True

def add_sum_on_campaign_db(transfer: TransferSchema):
    db = next(get_db())
    transfer_data = transfer.model_dump()
    new_transfer = Transfer(**transfer_data)
    if new_transfer.summ:
        db.add(new_transfer)
        campaign = db.query(Campaign).filter_by(id=new_transfer.transfer_campaign_id).first()
        if campaign:
            campaign.sum_now += new_transfer.summ
            if campaign.expected_sum <= campaign.sum_now:
                campaign.expected_sum_achieved = True
            db.commit()
            return True
    return False

def get_all_user_transfer_db(uid):
    db = next(get_db())
    user_transfer = db.query(Transfer).filter_by(transfer_user_id=uid).all()
    return user_transfer

def get_all_campaign_transfer_db(cid):
    db = next(get_db())
    transfer_on_campaign = db.query(Transfer).filter_by(transfer_campaign_id=cid)
    return transfer_on_campaign