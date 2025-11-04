from pydantic import BaseModel
from typing import Union


class TransferSchema(BaseModel):
    transfer_campaign_id: int
    transfer_user_id: int
    summ: int

class TransferRead(BaseModel):
    status: int
    message: Union[str | int | bool | list | dict]