# 🚀 AI Skill Gap Analyzer

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Gemini API](https://img.shields.io/badge/Google_Gemini-4285F4?style=for-the-badge&logo=google&logoColor=white)

A breathtaking, modern web application that uses Artificial Intelligence to analyze your resume, identify missing technical skills for your dream job, and generate a highly detailed, personalized learning roadmap complete with real-world Capstone Projects.

## ✨ Features

- 📄 **Smart Resume Analysis:** Upload your resume (PDF or TXT) and let the system parse and understand your background.
- 🎯 **Advanced Skill Extraction:** Uses NLP (via Google Gemini or fallback pattern matching) to extract core technical competencies.
- 💼 **Job Role Matching:** Select your dream role (e.g., Data Scientist, Backend Engineer) and instantly calculate your compatibility score.
- ❌ **Gap Analysis:** Identifies the exact technical skills you are missing for your desired career path.
- 🗺️ **Dynamic Learning Roadmap:** Generates a tailored curriculum featuring estimated timelines, core concepts, direct course links, and deep, highly detailed Capstone Projects with real-world problem statements for 30+ technologies.
- 📈 **Progress Tracking:** Gamified UI with animated progress bars visualizing your path to mastery.
- 🎨 **Premium UI/UX:** Features a stunning, custom-built interface with glassmorphism, glowing mesh gradients (`BorderGlow`), and interactive mouse-tracking backgrounds (`BlobCursor`).

## 🛠️ Technology Stack

- **Frontend:** Streamlit (with heavily customized Vanilla JS / CSS injections)
- **Backend:** Python
- **AI/NLP:** Google Gemini API (fallback to Regex mapping)
- **PDF Parsing:** PyPDF2

## 🚀 Getting Started

### Prerequisites
Make sure you have Python 3.8+ installed on your machine.

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/adhikaribidita/ai-skill-gap-analyzer.git
   cd ai-skill-gap-analyzer
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   # On Windows:
   .\venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **(Optional) Configure Gemini API:**
   For the best skill extraction results, get a free Google Gemini API key and set it as an environment variable:
   ```bash
   # On Windows:
   set GEMINI_API_KEY="your_api_key_here"
   # On macOS/Linux:
   export GEMINI_API_KEY="your_api_key_here"
   ```

5. **Run the application:**
   ```bash
   streamlit run app.py
   ```

## 📸 Usage
1. Open the local Streamlit URL in your browser.
2. Click the glowing **GET STARTED** button on the cover page.
3. Upload your resume and select your target role from the dropdown.
4. Click **GENERATE ROADMAP** and explore your beautifully animated AI analysis!

## 📄 License
This project is open-source and available for personal and educational use.
