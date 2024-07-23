from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from users.models import Base

DATABASE_URL = 'postgresql+psycopg2://postgres:admin123@localhost:5433/connect'

engine = create_engine(DATABASE_URL)
Base.metadata.create_all(bind=engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Test the setup
db = SessionLocal()
print("Database initialized successfully")
