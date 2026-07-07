import PyPDF2
import io
import re
import os
import json
from google import genai
from google.genai import types

# Simple master list of skills for fallback keyword matching.
MASTER_SKILLS = [
    "python", "sql", "machine learning", "statistics", "data visualization", "pandas", "numpy",
    "deep learning", "nlp", "tensorflow", "pytorch", "computer vision", "llms",
    "java", "c++", "data structures", "algorithms", "system design", "git",
    "aws", "azure", "gcp", "docker", "kubernetes", "linux", "networking", "terraform",
    "react", "javascript", "html", "css", "node.js", "agile", "scrum"
]

def extract_text_from_pdf(file_bytes):
    """Extracts text from a PDF file."""
    try:
        reader = PyPDF2.PdfReader(io.BytesIO(file_bytes))
        text = ""
        for page in reader.pages:
            text += page.extract_text() + " "
        return text
    except Exception as e:
        print(f"Error reading PDF: {e}")
        return ""

def extract_skills_llm(text):
    """Extracts skills using Google Gemini API."""
    try:
        # Initialize client. It will automatically pick up GEMINI_API_KEY from environment
        client = genai.Client()
        
        prompt = f"""
        Extract all the technical skills, programming languages, and tools from the following resume text.
        Return ONLY a JSON list of strings, all lowercase. Do not return markdown blocks or any other text.
        Example: ["python", "machine learning", "docker"]
        
        Resume Text:
        {text[:5000]} # Limit text length for safety
        """
        
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
        )
        
        # Clean the response to ensure it's valid JSON
        result = response.text.strip()
        if result.startswith("```json"):
            result = result.split("```json")[1].split("```")[0].strip()
        elif result.startswith("```"):
            result = result.split("```")[1].split("```")[0].strip()
            
        skills = json.loads(result)
        return [skill.lower() for skill in skills if isinstance(skill, str)]
        
    except Exception as e:
        print(f"LLM Extraction failed: {e}. Falling back to keyword matching.")
        return extract_skills_from_text(text)

def extract_skills_from_text(text):
    """Fallback: Extracts skills from text using simple keyword matching."""
    text_lower = text.lower()
    text_clean = re.sub(r'[^a-z0-9\+]', ' ', text_lower)
    words = set(text_clean.split())
    
    found_skills = []
    for skill in MASTER_SKILLS:
        if " " in skill:
            if skill in text_lower:
                found_skills.append(skill)
        else:
            if skill in words:
                found_skills.append(skill)
                
    return found_skills

def parse_resume(file_bytes):
    """Main pipeline to parse resume and return skills."""
    text = extract_text_from_pdf(file_bytes)
    
    # Try LLM first if API key exists, else fallback
    if os.environ.get("GEMINI_API_KEY"):
        skills = extract_skills_llm(text)
    else:
        skills = extract_skills_from_text(text)
        
    return skills
