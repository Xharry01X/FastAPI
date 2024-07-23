from fastapi import APIRouter, status, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from core.database import get_db
from users.schemas import CreateUserRequest
from users.services import create_user_account

router = APIRouter(
    prefix="/users",
    tags=["User"],
    responses={404: {"description": "Not found"}}
)

@router.post('', status_code=status.HTTP_201_CREATED)
async def create_user(data: CreateUserRequest, db: Session = Depends(get_db)):
    await create_user_account(data=data, db=db)  # Ensure this function is async if using await
    payload = {"Message": "User created successfully"}
    return JSONResponse(content=payload)
