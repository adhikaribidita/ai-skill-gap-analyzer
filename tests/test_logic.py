import pytest
from core.extractor import extract_skills_from_text
from core.analyzer import analyze_gap

def test_extract_skills():
    text = "I am a software engineer with 5 years of experience in Python and Java. I also know SQL."
    skills = extract_skills_from_text(text)
    
    assert "python" in skills
    assert "java" in skills
    assert "sql" in skills
    assert "c++" not in skills

def test_extract_multi_word_skills():
    text = "I have experience with Machine Learning and Data Visualization."
    skills = extract_skills_from_text(text)
    
    assert "machine learning" in skills
    assert "data visualization" in skills

def test_analyze_gap():
    user_skills = ["python", "sql", "java"]
    required_skills = ["python", "sql", "machine learning", "pandas"]
    
    result = analyze_gap(user_skills, required_skills)
    
    assert "python" in result["matched_skills"]
    assert "sql" in result["matched_skills"]
    assert "machine learning" in result["missing_skills"]
    assert "pandas" in result["missing_skills"]
    assert "java" not in result["matched_skills"] # Not required
    
    # Match percentage: 2 out of 4 required = 50%
    assert result["match_percentage"] == 50.0
