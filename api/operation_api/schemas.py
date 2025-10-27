from pydantic import BaseModel

class CampaignSchema(BaseModel):
    name: str
    description: str
    expected_sum: int
    sum_now: int
    campaign_owner_user_id: int
    expected_sum_achieved: bool

class CommentSchema(BaseModel):
    comment_user_id: int
    comment_campaign_id: int
    text: str

class TransferSchema(BaseModel):
    transfer_campaign_id: int
    transfer_user_id: int
    summ: int