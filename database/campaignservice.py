from database import get_db
from database.models import Campaign
from api.campaign_api.schemas import CampaignSchema

def campaign_with_id(cid):
    with next(get_db()) as db:
        campaign = db.query(Campaign).filter_by(id=cid).first()
        return campaign

def get_exact_campaign_db(cid):
    db = next(get_db())
    return db.query(Campaign).filter_by(id=cid).first()

def get_all_campaign_db():
    db = next(get_db())
    return db.query(Campaign).all()

def get_all_campaign_by_user_db(user_id):
    db = next(get_db())
    return db.query(Campaign).filter_by(campaign_owner_user_id=user_id).all()

def create_campaign_db(campaign: CampaignSchema):
    db = next(get_db())
    new_campaign = Campaign(**campaign.model_dump())
    db.add(new_campaign)
    db.commit()
    return True

def redact_campaign_db(cid, change_info, new_info):
    db = next(get_db())
    redact_campaign = db.query(Campaign).filter_by(id=cid).first()
    if redact_campaign:
        if change_info == 'name':
            redact_campaign.name = new_info
            db.commit()
            return True
        elif change_info == 'description':
            redact_campaign.description = new_info
            db.commit()
            return True
        elif change_info == 'expected_sum':
            if int(new_info):
                redact_campaign.expected_sum = new_info
                if redact_campaign.sum_now < redact_campaign.expected_sum:
                    redact_campaign.expected_sum_achieved = 0
                elif redact_campaign.sum_now > redact_campaign.expected_sum:
                    redact_campaign.expected_sum_achieved = 1
                db.commit()
                return True
            else:
                return False
    return False

def delete_campaign(cid):
    db = next(get_db())
    deleting_campaign = db.query(Campaign).filter_by(id=cid).first()
    db.delete(deleting_campaign)
    db.commit()
    return True