from users.models import UserModel
from fastapi.exceptions import HTTPException
from core.security import get_password_hash
from datetime import datetime


async def create_user_account(data, db):
    user = db.query(UserModel).filter(UserModel.email == data.email).first()
    if user:
        raise HTTPException(status_code=422, detail="Email is already registered with us.")

    new_user = UserModel(
        
        email=data.email,
        password=get_password_hash(data.password),
        
        updated_at=datetime.now()
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user