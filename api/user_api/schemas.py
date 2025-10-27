from pydantic import BaseModel, EmailStr
from typing import Optional, Union


class UserSchema(BaseModel):
    username: str
    email: EmailStr
    phone_number: Optional[str]
    password: str

class UserRead(BaseModel):
    status: int
    message: Union[str | int | bool | list | dict]