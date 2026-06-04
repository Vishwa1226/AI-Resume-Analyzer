from fastapi import APIRouter, UploadFile, File
import os # Imports Python's built-in Operating System module.
from services.resume_parser import extract_text
from services.ai_service import (analyze_resume, get_ats_feedback)

router = APIRouter() # It creates a router object (container) that stores route definitions.All resume-related APIs will be stored inside it.

UPLOAD_FOLDER = "uploads"

@router.get("/")
def resume_home():
    return {
        "message" : "Resume Route Working"
    }

# rout definition 
   # URL : /
   # Method : GET 
   # Function : resume_home()


@router.post("/upload")
async def upload_resume( # async : (Asynchronous function) Allows FastAPI to handle multiple requests efficiently.
    file: UploadFile = File(...)
    # file: UploadFile -> represents uploaded file
    # File(...) -> (3 dots means This field is required) user needs to upload file
):

    allowed_extensions = [".pdf" , ".docx"]
    extension = os.path.splitext(file.filename)[1].lower()
    if extension not in allowed_extensions:
        return {
            "error":
            "Only PDF and DOCX files are allowed"
        }

    file_path = os.path.join(UPLOAD_FOLDER,file.filename)

    with open(file_path, "wb") as buffer:
        content = await file.read()
        buffer.write(content)

    resume_text = extract_text(file_path)

    from services.ats_service import (calculate_ats_score)

    ats_result = calculate_ats_score(resume_text)

    ai_feedback = get_ats_feedback(resume_text)
       
    analysis = analyze_resume(resume_text)
        
    return {
       "filename": file.filename,
       "ats_result": ats_result,
       "ai_feedback": ai_feedback
    }