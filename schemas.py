from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class CarCreate(BaseModel):
    make: str
    model: str
    year: int
    description: str

class CarSchema(CarCreate):
    id: int
    created_at: datetime
    updated_at: datetime
    owner_id: int


class CarUpdate(BaseModel):
    make: Optional[str] = None
    model: Optional[str] = None
    year: Optional[int] = None
    description: Optional[str] = None


class CommentCreate(BaseModel):
    content: str


class Comment(CommentCreate):
    id: int
    created_at: datetime
    car_id: int
    author_id: int


class UserCreate(BaseModel):
    username: str
    password: str


class UserSchema(BaseModel):
    id: int
    username: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str

