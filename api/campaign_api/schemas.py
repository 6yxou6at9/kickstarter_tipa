from pydantic import BaseModel
from typing import Union

class CampaignSchema(BaseModel):
    name: str
    description: str
    expected_sum: int = 0
    campaign_owner_user_id: int

class CampaignRead(BaseModel):
    status: int
    message: Union[str | int | bool | list | dict]