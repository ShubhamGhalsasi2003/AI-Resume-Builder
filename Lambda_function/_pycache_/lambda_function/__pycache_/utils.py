# utils.py
import openai
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

openai.api_key = os.getenv("OPENAI_API_KEY")  # ✅ Perfect placement

def optimize_resume(resume_text, job_description):
    prompt = f"""
    You are a professional resume optimizer. 
    Optimize the following resume to better match the job description.

    Resume:
    {resume_text}

    Job Description:
    {job_description}

    Return only the optimized resume text.
    """

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # ✅ You chose this model
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    return response.choices[0].message["content"].strip()
