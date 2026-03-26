from jose import jwt, JWTError
from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from starlette import status

from config import ALGORITHM, SECRET_KEY
from database import SessionLocal

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def decode_auth_token(auth_token: str):
    try:
        payload = jwt.decode(auth_token, SECRET_KEY, algorithms=[ALGORITHM])
        email = payload.get("sub")
        if email is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail="Could not validate credentials",)
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Could not validate credentials",)
    return payload

def get_current_user(token: str = Depends(oauth2_scheme)):
    return decode_auth_token(token)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()