import os
import PyPDF2
from fastapi import FastAPI, Query
from typing import List, Optional
import google.generativeai as genai

app = FastAPI()

# Function to extract text from a PDF file
def extract_text_from_pdf(file_path):
    with open(file_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        text = " ".join(page.extract_text() for page in reader.pages)
    return text

# Loop through the PDF files and extract the text
def get_resumes_context(directory="Resume"):
    resumes = []
    for file_name in os.listdir(directory):
        if file_name.endswith(".pdf"):
            file_path = os.path.join(directory, file_name)
            text = extract_text_from_pdf(file_path)
            resumes.append(text)
    # Combine all resumes into a single string, separated by '-----'
    return "\n-----\n".join(resumes)

context = get_resumes_context()

genai.configure(api_key="AIzaSyAVp4xDf4LIqJciJ2JwZBUqbUdnTrhpdaI")
model = genai.GenerativeModel('gemini-1.5-flash')

@app.get("/query")
def query_resumes(
    experience: Optional[str] = Query(None, description="Experience level"),
    job_role: Optional[str] = Query(None, description="Job role"),
    skills: Optional[List[str]] = Query(None, description="List of skills")
):
    query = f"Experience: {experience}, Job Role: {job_role}, Skills: {', '.join(skills) if skills else ''}"
    
    ranked_candidates = model.generate_content(
        f"Using the context provided only without any text generation answer the questions asked. context: {context}, query: {query}", 
        stream=True
    )
    
    result = "".join(chunk.text for chunk in ranked_candidates)
    return {"response": result}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=6000)