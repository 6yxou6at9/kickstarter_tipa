from pydantic import BaseModel
from typing import Union

class CampaignSchema(BaseModel):
    name: str
    description: str
    expected_sum: int = 0
    campaign_owner_user_id: int

class CommentSchema(BaseModel):
    comment_user_id: int
    comment_campaign_id: int
    text: str

class TransferSchema(BaseModel):
    transfer_campaign_id: int
    transfer_user_id: int
    summ: int

class SchemaRead(BaseModel):
    status: int
    message: Union[str | int | bool | list | dict]