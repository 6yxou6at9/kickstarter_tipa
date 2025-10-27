from pydantic import BaseModel, EmailStr
from typing import Optional, Union


class UserSchema(BaseModel):
    name: str
    surname: Optional[str]
    username: str
    email: EmailStr
    password: str
    phone_number: str
    birthday: Optional[str]
    city: Optional[str]


class UserRead(BaseModel):
    status: int
    message: Union[str | int | bool | list | dict]