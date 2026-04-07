import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-pro")

def summarize_text(text: str):
    prompt = f"Summarize this text in 3 sentences:\n{text}"
    response = model.generate_content(prompt)
    return response.text