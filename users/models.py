from sqlalchemy import Boolean, Column, Integer, String, DateTime, func
from datetime import datetime

from core.database import Base


class UserModel(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255),unique=True,index=True)
    password = Column(String(100))
    updatedAt = Column(DateTime,nullable=True,default=None, onupdate=datetime.now)
    createdAt = Column(DateTime,nullable=False,server_default=func.now)