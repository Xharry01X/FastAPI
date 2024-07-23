from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
from typing import Generator
from core.config import get_settings


settings = get_settings()

engine = create_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True,
    pool_recycle=300,
    pool_size=5,
    max_overflow=0
)

sessionLocal = sessionmaker(autoCommit=False,autoflush=False,bind=engine)
Base = declarative_base

def get_db() -> Generator:
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()