from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import jwt
from config import SECRET_KEY, ALGORITHM
context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hashed_password(password):
    return context.hash(password)
def verify_password(plain_password, hashed_password):
    return context.verify(plain_password, hashed_password)
def encode_user(data: dict):
    data = data.copy()
    expire_time = datetime.utcnow() + timedelta(minutes=15)
    data.update({"exp": expire_time})
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
