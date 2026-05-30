from fastapi import FastAPI
from routes.resume import router as resume_router

app = FastAPI()

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