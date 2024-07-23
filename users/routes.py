from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .services import create_user_account
from .schemas import UserCreate, User
from core.database import get_db

router = APIRouter()

@router.post("/users", response_model=User)
async def create_user(data: UserCreate, db: Session = Depends(get_db)):
    try:
        user = await create_user_account(data=data, db=db)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return user
