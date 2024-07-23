import os

from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL","postgresql://postgres:admin123@localhost/connect")
SECRET_KEY = os.getenv("SECRET_KEY","harryDB")

ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30