from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.orm import Session
from dependencies import get_db, get_current_user
from gemini import extract_receipt

router = APIRouter()

@router.post("/expense/upload")
async def upload_receipt(file: UploadFile = File(...), db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    contents = await file.read()
    with open(f"receipts/{file.filename}", "wb") as buffer:
        buffer.write(contents)
    result = extract_receipt(contents)
    return {"filename": file.filename, "extracted_data": result}


