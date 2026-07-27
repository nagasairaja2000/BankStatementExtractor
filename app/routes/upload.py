from fastapi import APIRouter, UploadFile, File
import shutil
import os

router = APIRouter()


@router.post("/upload")
async def upload_file(bank_statement: UploadFile = File(...)):
    upload_dir = "uploads"
    os.makedirs(upload_dir, exist_ok=True)

    file_path = os.path.join(upload_dir, bank_statement.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(bank_statement.file, buffer)

    return {
        "message": "File uploaded successfully",
        "filename": bank_statement.filename
    }