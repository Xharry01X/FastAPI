from users.models import UserModel
from fastapi.exceptions import HTTPException
from core.security import get_password_hash
from datetime import datetime
from sqlalchemy.orm import Session

async def create_user_account(data, db: Session):
    # Check if the email is already registered
    user = db.query(UserModel).filter(UserModel.email == data.email).first()
    if user:
        raise HTTPException(status_code=422, detail="Email is already registered with us.")
    
    # Create a new user instance
    new_user = UserModel(
        email=data.email,
        password=get_password_hash(data.password),
        created_at=datetime.utcnow(),  # Use utcnow() for consistency
        updated_at=datetime.utcnow()   # Use utcnow() for consistency
    )
    
    # Add and commit the new user to the database
    try:
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
    except Exception as e:
        db.rollback()  # Rollback in case of error
        raise HTTPException(status_code=500, detail="An error occurred while creating the user.")
    
    return new_user
