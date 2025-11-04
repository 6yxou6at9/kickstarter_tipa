from pydantic import BaseModel
from typing import Union

class CommentSchema(BaseModel):
    comment_user_id: int
    comment_campaign_id: int
    text: str

class CommentRead(BaseModel):
    status: int
    message: Union[str | int | bool | list | dict]