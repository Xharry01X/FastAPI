from passlib.context import CryptContext

# Define the password context with bcrypt hashing scheme
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str) -> str:
    """Hashes the given password using bcrypt."""
    return pwd_context.hash(password)
