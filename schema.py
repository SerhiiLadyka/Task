from pydantic import BaseModel
from datetime import date


class UserBase(BaseModel):
    username: str
    email: str
    password: str

    class Config:
        orm_mode = True


class User(UserBase):
    id: int
    register_date: date

    class Config:
        orm_mode = True


class UserAdd(UserBase):
    register_date: date

    class Config:
        orm_mode = True


class UpdateUser(BaseModel):
    password: str

    class Config:
        orm_mode = True
