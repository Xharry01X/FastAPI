from sqlalchemy.orm import Session
from .models import UserModel
from .schemas import UserCreate

def create_user_account(data: UserCreate, db: Session):
    user = db.query(UserModel).filter(UserModel.username == data.username).first()
    if user:
        raise ValueError("Username already exists")
    new_user = UserModel(
        username=data.username,
        password=data.password,
        created_at=data.created_at,
        updated_at=data.updated_at
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
