import os
from dotenv import load_dotenv
from pathlib import Path
from urllib.parse import quote_plus
from pydantic_settings import BaseSettings

# Load environment variables from .env file
env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)

# Define the Settings class
class Settings(BaseSettings):
    DB_USER: str = os.getenv('DB_USER')
    DB_PASSWORD: str = os.getenv('DB_PASSWORD')
    DB_HOST: str = os.getenv('DB_HOST')
    DB_PORT: str = os.getenv('DB_PORT')
    DB_NAME: str = os.getenv('DB_NAME')
    
    @property
    def database_url(self):
        return f'postgresql+psycopg2://{self.DB_USER}:{quote_plus(self.DB_PASSWORD)}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'

def get_settings() -> Settings:
    return Settings()

# Usage example
settings = get_settings()

# Print out the loaded environment variables for debugging
print(f"DB_USER: {settings.DB_USER}")
print(f"DB_PASSWORD: {settings.DB_PASSWORD}")
print(f"DB_HOST: {settings.DB_HOST}")
print(f"DB_PORT: {settings.DB_PORT}")
print(f"DB_NAME: {settings.DB_NAME}")

DATABASE_URL = settings.database_url
print(DATABASE_URL)  # This will print the constructed DATABASE_URL
