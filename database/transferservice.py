from database import get_db
from database.models import Campaign, Transfer
from api.transfer_api.schemas import TransferSchema

def get_exact_transfer_db(tid):
    db = next(get_db())
    return db.query(Transfer).filter_by(id=tid).first()

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
    transfer_on_campaign = db.query(Transfer).filter_by(transfer_campaign_id=cid).all()
    return transfer_on_campaign