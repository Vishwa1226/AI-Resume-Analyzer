from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.resume import router as resume_router

app = FastAPI(
    title="AI Resume Analyzer API",
    description="Backend API for Resume Analysis and Interview Coaching",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
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