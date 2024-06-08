import os
import PyPDF2
import google.generativeai as genai

# Function to extract text from a PDF file
def extract_text_from_pdf(file_path):
    with open(file_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        text = " ".join(page.extract_text() for page in reader.pages)
    return text

# Loop through the PDF files and extract the text
resumes = []
for file_name in os.listdir("Resumes"):
    if file_name.endswith(".pdf"):
        file_path = os.path.join("Resumes", file_name)
        text = extract_text_from_pdf(file_path)
        resumes.append(text)

# Combine all resumes into a single string, separated by '-----'
context = "\n-----\n".join(resumes)

genai.configure(api_key="AIzaSyAVp4xDf4LIqJciJ2JwZBUqbUdnTrhpdaI")
model = genai.GenerativeModel('gemini-1.5-flash')

query = input("Enter your query: ")

# Pass the context to the generative model
ranked_candidates = model.generate_content(f"Using the context provided only without any text genration answer the questions asked. context: {context}, query: {query}", stream=True)

for chunk in ranked_candidates:
  print(chunk.text)