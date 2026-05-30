from fastapi import FastAPI
from routes.resume import router as resume_router

app = FastAPI(
    title="AI Resume Analyzer API",
    description="Backend API for Resume Analysis and Interview Coaching",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "Backend Working"
        }

app.include_router(
    resume_router,
    prefix="/resume",
    tags=["Resume"]
)