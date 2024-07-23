from pydantic import BaseModel
from datetime import datetime

class UserCreate(BaseModel):
    username: str
    password: str
    created_at: datetime
    updated_at: datetime

class User(BaseModel):
    id: int
    username: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
