from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from starlette import status

from schemas import Create_User
from crud import fetch_by_email, create_user
from auth import verify_password, encode_user
from dependencies import get_db

router = APIRouter()
@router.post("/register")
def register_user(user: Create_User, db: Session = Depends(get_db)):
    existing =  fetch_by_email(db, email=user.email)
    if existing:
        HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Email already registered")
    create_user(db, user)
    return {"message": "User registered"}
@router.post("/login")
def login_user(form_data: OAuth2PasswordRequestForm = Depends(),db: Session = Depends(get_db)):
    email =  fetch_by_email(db, email=form_data.username)
    if not email or not verify_password(form_data.password, email.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,)
    token = encode_user(data={"sub": email.email})
    return {"access_token": token, "token_type": "bearer"}
