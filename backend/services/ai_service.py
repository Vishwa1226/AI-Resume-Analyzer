import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)


def analyze_resume(resume_text):

    prompt = f"""
    Analyze this resume.

    Give:

    1. Summary
    2. Strengths
    3. Weaknesses
    4. Missing Skills
    5. ATS Improvement Tips

    Resume:

    {resume_text}
    """

    response = model.generate_content(prompt)

    return response.text
