import streamlit as st
import re
import uuid
import base64
import os
from db.database import get_job_roles, get_required_skills, save_user_progress
from core.extractor import parse_resume
from core.analyzer import analyze_gap, generate_roadmap
import streamlit.components.v1 as components
from strands import STRANDS_HTML
from blob_cursor import BLOB_CURSOR_HTML
from border_glow import BORDER_GLOW_HTML

# Set page config for better appearance
st.set_page_config(page_title="SKILLORA", layout="wide", page_icon="🎯", initial_sidebar_state="collapsed")

# Initialize session state for pagination and data
if 'page' not in st.session_state:
    st.session_state.page = 1
if 'analysis_results' not in st.session_state:
    st.session_state.analysis_results = None
if 'extracted_skills' not in st.session_state:
    st.session_state.extracted_skills = None

# Base CSS styling
import random

# Generate global background particles for Pages 2 & 3
global_particles_html = ""
for _ in range(30):
    left = random.randint(0, 100)
    delay = random.uniform(0, 15)
    duration = random.uniform(10, 25)
    size = random.uniform(2, 6)
    global_particles_html += f'<div class="global-particle" style="left: {left}%; animation-delay: {delay:.1f}s; animation-duration: {duration:.1f}s; width: {size:.1f}px; height: {size:.1f}px;"></div>'

import os, base64
def get_base64_image(image_path):
    if os.path.exists(image_path) and os.path.isfile(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    return None

if st.session_state.page == 1:
    app_bg = "background: #000;"
    
    import textwrap
    cover_page_html = textwrap.dedent("""
    <style>
        /* Target the Strands iframe explicitly to make it fullscreen */
        iframe[height="1234"] {
            position: fixed;
            top: 0; left: 0;
            width: 100vw !important;
            height: 100vh !important;
            z-index: 0;
            border: none;
            pointer-events: none;
        }
        
        @keyframes zoomOutFadeIn {
            0% { transform: translate(-50%, -50%) scale(2.0); opacity: 0; filter: brightness(2) blur(10px); }
            100% { transform: translate(-50%, -50%) scale(1.0); opacity: 1; filter: brightness(1) blur(0px); }
        }
        .skillora-wrapper {
            animation: zoomOutFadeIn 1.5s cubic-bezier(0.16, 1, 0.3, 1) forwards;
            opacity: 0;
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            z-index: 100001;
        }
        
        .skillora-text {
            font-size: 6rem;
            font-weight: 900;
            letter-spacing: 15px;
            color: transparent;
            background: linear-gradient(90deg, #ffffff 0%, #a5f3fc 20%, #ffffff 40%, #c4b5fd 60%, #ffffff 80%, #a5f3fc 100%);
            background-size: 200% auto;
            -webkit-background-clip: text;
            background-clip: text;
            text-shadow: 0 0 30px rgba(139, 92, 246, 0.5), 0 0 60px rgba(59, 130, 246, 0.5);
            transition: all 0.5s ease;
            animation: glitterSweep 4s linear infinite, pulseText 3s infinite alternate;
            text-align: center;
            user-select: none;
            pointer-events: none;
        }

        @keyframes glitterSweep {
            to { background-position: 200% center; }
        }

        @keyframes pulseText {
            0% { text-shadow: 0 0 20px rgba(139, 92, 246, 0.5); }
            100% { text-shadow: 0 0 40px rgba(59, 130, 246, 0.9); }
        }
        
        /* Position the GET STARTED button directly under the SKILLORA word */
        div[data-testid="stButton"] {
            position: fixed;
            top: 62%;
            left: 50%;
            transform: translateX(-50%);
            z-index: 100002;
        }
        
        button[kind="secondary"] {
            background: rgba(6, 182, 212, 0.1) !important;
            border: 1px solid rgba(6, 182, 212, 0.5) !important;
            color: #a5f3fc !important;
            border-radius: 30px !important;
            padding: 15px 50px !important;
            font-size: 1.2rem !important;
            font-weight: 800 !important;
            letter-spacing: 4px !important;
            backdrop-filter: blur(10px) !important;
            box-shadow: 0 0 15px rgba(6, 182, 212, 0.3) !important;
            transition: all 0.3s ease !important;
        }
        button[kind="secondary"]:hover {
            background: rgba(6, 182, 212, 0.3) !important;
            box-shadow: 0 0 30px rgba(6, 182, 212, 0.8) !important;
            transform: scale(1.05) !important;
            color: white !important;
            border: 1px solid rgba(6, 182, 212, 1) !important;
        }
    </style>
    
    <div class="skillora-wrapper">
        <div class="skillora-text">SKILLORA</div>
    </div>
    """)
else:
    app_bg = "background: radial-gradient(circle at 50% 40%, #06b6d4 0%, #082f49 20%, #020617 100%);"
    cover_page_html = ""

st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;700;900&display=swap');
    
    html, body, [class*="css"] {{
        font-family: 'Outfit', sans-serif;
    }}

    /* Hide Streamlit Top Bar and Deploy Button */
    [data-testid="stHeader"] {{
        display: none !important;
    }}
    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}

    /* Cinematic Gradient Background for generic pages */
    .stApp {{
        {app_bg}
        background-size: cover;
        background-attachment: fixed;
        color: #f8fafc;
    }}

    /* Global Particles for live background */
    .global-particle {{
        position: fixed;
        bottom: -10vh;
        background: rgba(6, 182, 212, 0.4);
        box-shadow: 0 0 10px rgba(6, 182, 212, 0.6);
        border-radius: 50%;
        animation: floatUpGlobal linear infinite;
        pointer-events: none;
        z-index: 0;
    }}
    @keyframes floatUpGlobal {{
        0% {{ transform: translateY(0) scale(1); opacity: 0; }}
        10% {{ opacity: 1; }}
        90% {{ opacity: 1; }}
        100% {{ transform: translateY(-120vh) scale(1.5); opacity: 0; }}
    }}

    /* Cinematic Slide-up Animation & Minimalist Container */
    @keyframes slideUpFade {{
        from {{ opacity: 0; transform: translateY(100vh); }}
        to {{ opacity: 1; transform: translateY(0); }}
    }}
    .main .block-container {{
        background: transparent !important;
        border: none !important;
        box-shadow: none !important;
        backdrop-filter: none !important;
        -webkit-backdrop-filter: none !important;
        padding: 3rem !important;
        animation: slideUpFade 1.2s cubic-bezier(0.16, 1, 0.3, 1) forwards;
        z-index: 10;
        position: relative;
    }}

    /* Glassmorphism for inputs and containers */
    .stTextInput > div > div > input, 
    .stSelectbox > div > div {{
        background: rgba(255, 255, 255, 0.03) !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        backdrop-filter: blur(10px);
        color: white !important;
        border-radius: 30px !important;
        padding-left: 20px !important;
        transition: all 0.3s ease;
    }}
    
    /* Neon Uploader */
    [data-testid="stFileUploadDropzone"] {{
        background: rgba(255, 255, 255, 0.02) !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        border-radius: 20px !important;
        transition: all 0.3s ease;
    }}
    [data-testid="stFileUploadDropzone"]:hover, .stSelectbox > div > div:hover {{
        background: rgba(255, 255, 255, 0.05) !important;
        border-color: rgba(6, 182, 212, 0.8) !important;
        box-shadow: 0 0 20px rgba(6, 182, 212, 0.3) !important;
        transform: translateY(-2px);
    }}

    /* Standard Button */
    .stButton>button {{
        background: transparent !important;
        color: white !important;
        border-radius: 30px !important;
        border: 1px solid rgba(255, 255, 255, 0.5) !important;
        padding: 10px 40px !important;
        font-weight: 400 !important;
        letter-spacing: 2px !important;
        text-transform: uppercase !important;
        transition: all 0.4s ease !important;
        box-shadow: none !important;
    }}
    .stButton>button:hover {{
        background: rgba(255, 255, 255, 1) !important;
        color: black !important;
        border: 1px solid white !important;
        transform: translateY(-2px) !important;
    }}

    /* Skill Tags with Glow */
    .skill-tag {{
        display: inline-block;
        padding: 6px 14px;
        border-radius: 20px;
        margin: 6px;
        font-size: 14px;
        font-weight: 500;
        backdrop-filter: blur(5px);
        animation: fadeInUp 0.5s ease-out backwards;
    }}
    .skill-tag.match {{
        background: rgba(16, 185, 129, 0.15);
        color: #34d399;
        border: 1px solid rgba(16, 185, 129, 0.4);
        box-shadow: 0 0 10px rgba(16, 185, 129, 0.2);
    }}
    .skill-tag.missing {{
        background: rgba(239, 68, 68, 0.15);
        color: #f87171;
        border: 1px solid rgba(239, 68, 68, 0.4);
        box-shadow: 0 0 10px rgba(239, 68, 68, 0.2);
    }}
    
    h1, h2, h3 {{
        color: #f8fafc !important;
        text-shadow: 0 2px 10px rgba(255,255,255,0.1);
    }}
</style>
{global_particles_html}
{cover_page_html}
""", unsafe_allow_html=True)

# ==========================================
# PAGE 1: CINEMATIC COVER PAGE
# ==========================================
if st.session_state.page == 1:
    
    components.html(STRANDS_HTML, height=1234)

    if st.button("GET STARTED", key="enter_app"):
        st.session_state.page = 2
        st.rerun()

# ==========================================
# PAGE 2: UPLOAD PAGE
# ==========================================
elif st.session_state.page == 2:
    components.html(BLOB_CURSOR_HTML, height=0)
    
    st.markdown("""
    <style>
        @keyframes slideUpFade {
            0% { transform: translateY(50vh); opacity: 0; }
            100% { transform: translateY(0); opacity: 1; }
        }
        
        /* Apply slide up animation to the main Streamlit container */
        .block-container {
            animation: slideUpFade 0.3s cubic-bezier(0.16, 1, 0.3, 1) forwards !important;
            padding-top: 6rem !important;
        }

        /* Glassmorphism Theme for Input Widgets */
        div[data-testid="stFileUploader"], div[data-testid="stSelectbox"] > div {
            background: rgba(15, 23, 42, 0.5) !important;
            backdrop-filter: blur(15px);
            -webkit-backdrop-filter: blur(15px);
            border: 1px solid rgba(139, 92, 246, 0.3) !important;
            border-radius: 20px !important;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4) !important;
            transition: all 0.4s ease !important;
        }
        
        div[data-testid="stFileUploader"] {
            padding: 25px !important;
        }
        
        div[data-testid="stFileUploader"]:hover, div[data-testid="stSelectbox"] > div:hover {
            border: 1px solid rgba(6, 182, 212, 0.8) !important;
            box-shadow: 0 10px 40px rgba(6, 182, 212, 0.25) !important;
            transform: translateY(-3px);
        }

        /* Typography */
        h1, h2, h3, p, label {
            color: #f8fafc !important;
        }
        h3 {
            font-size: 1.6rem !important;
            font-weight: 800 !important;
            letter-spacing: 2px;
            text-shadow: 0 0 15px rgba(139, 92, 246, 0.5);
            margin-bottom: 1.5rem !important;
        }
        
        /* Generate Button */
        button[kind="primary"] {
            background: linear-gradient(90deg, #06b6d4, #8b5cf6) !important;
            color: white !important;
            border: none !important;
            border-radius: 30px !important;
            padding: 15px 40px !important;
            font-size: 1.2rem !important;
            font-weight: 800 !important;
            letter-spacing: 2px !important;
            box-shadow: 0 0 20px rgba(139, 92, 246, 0.4) !important;
            transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1) !important;
            width: 100% !important;
        }
        button[kind="primary"]:hover {
            transform: translateY(-4px) scale(1.02) !important;
            box-shadow: 0 0 40px rgba(6, 182, 212, 0.8) !important;
            color: white !important;
        }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    col1, col2 = st.columns([1, 1], gap="large")
    
    with col1:
        st.markdown("### UPLOAD PROFILE")
        uploaded_file = st.file_uploader("Upload your resume (PDF only)", type=["pdf"], label_visibility="collapsed")
    
    with col2:
        st.markdown("### SELECT DREAM ROLE")
        roles = get_job_roles()
        selected_role = st.selectbox("Choose a job role:", roles, label_visibility="collapsed")
    
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    _, col_btn, _ = st.columns([1, 1.5, 1])
    with col_btn:
        if st.button("GENERATE ROADMAP", type="primary"):
            if uploaded_file is None:
                st.warning("Please upload a resume first.")
            else:
                with st.spinner("Our AI is analyzing your resume..."):
                    file_bytes = uploaded_file.read()
                    extracted_skills = parse_resume(file_bytes)
                    required_skills = get_required_skills(selected_role)
                    analysis = analyze_gap(extracted_skills, required_skills)
                    
                    # Save progress (using a random session ID for demo purposes)
                    if 'user_id' not in st.session_state:
                        st.session_state.user_id = str(uuid.uuid4())
                    save_user_progress(st.session_state.user_id, extracted_skills, analysis['missing_skills'], analysis['match_percentage'])
                    
                    # Store in session state and move to page 3
                    st.session_state.analysis_results = analysis
                    st.session_state.extracted_skills = extracted_skills
                    st.session_state.page = 3
                    st.rerun()

# ==========================================
# PAGE 3: OUTPUT PAGE
# ==========================================
elif st.session_state.page == 3:
    components.html(BORDER_GLOW_HTML, height=0)
    
    analysis = st.session_state.analysis_results
    
    st.markdown("""
    <style>
        .block-container {
            animation: slideUpFade 0.8s cubic-bezier(0.16, 1, 0.3, 1) forwards !important;
            padding-top: 3rem !important;
        }
        h1.title {
            text-align: center;
            font-size: 3.5rem !important;
            font-weight: 900 !important;
            letter-spacing: 5px;
            color: transparent;
            background: linear-gradient(90deg, #06b6d4, #c4b5fd, #8b5cf6);
            -webkit-background-clip: text;
            background-clip: text;
            margin-bottom: 3rem !important;
            text-shadow: 0 0 40px rgba(139, 92, 246, 0.4);
        }
        
        /* Custom progress bar */
        .progress-track {
            background: rgba(15, 23, 42, 0.8);
            border-radius: 20px;
            height: 25px;
            overflow: hidden;
            border: 1px solid rgba(6, 182, 212, 0.3);
            margin: 10px 0 20px 0;
            box-shadow: inset 0 0 10px rgba(0,0,0,0.5);
        }
        .progress-fill {
            background: linear-gradient(90deg, #06b6d4, #8b5cf6);
            height: 100%;
            transition: width 1.5s cubic-bezier(0.16, 1, 0.3, 1);
            box-shadow: 0 0 15px rgba(139, 92, 246, 0.8);
        }
        
        button[kind="primary"] {
            background: linear-gradient(90deg, #06b6d4, #8b5cf6) !important;
            color: white !important;
            border: none !important;
            border-radius: 30px !important;
            padding: 15px 40px !important;
            font-size: 1.2rem !important;
            font-weight: 800 !important;
            letter-spacing: 2px !important;
            box-shadow: 0 0 20px rgba(139, 92, 246, 0.4) !important;
            transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1) !important;
            width: 100% !important;
        }
        button[kind="primary"]:hover {
            transform: translateY(-4px) scale(1.02) !important;
            box-shadow: 0 0 40px rgba(6, 182, 212, 0.8) !important;
        }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown("<h1 class='title'>ANALYSIS COMPLETE</h1>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1], gap="large")
    
    with col1:
        match_html = "".join([f"<span class='skill-tag match' style='margin:5px; padding:10px 20px; border-radius:20px; background:rgba(6,182,212,0.15); border:1px solid rgba(6,182,212,0.5); display:inline-block; font-weight:bold; box-shadow: 0 0 10px rgba(6,182,212,0.2); backdrop-filter: blur(5px);'>{skill.title()}</span>" for skill in analysis['matched_skills']]) if analysis['matched_skills'] else "<p>No matching skills found.</p>"
        st.markdown(f"""
<div class='border-glow-card' style='height: 100%;'>
    <span class='edge-light'></span>
    <div class='border-glow-inner'>
        <h3 style='color: #06b6d4; font-weight: 900; letter-spacing: 2px; text-shadow: 0 0 10px rgba(6,182,212,0.5); margin-bottom: 25px; border-bottom: 1px solid rgba(6,182,212,0.3); padding-bottom: 15px;'>✅ EXTRACTED SKILLS</h3>
        <div>{match_html}</div>
    </div>
</div>
""", unsafe_allow_html=True)

    with col2:
        missing_html = "".join([f"<span class='skill-tag missing' style='margin:5px; padding:10px 20px; border-radius:20px; background:rgba(139,92,246,0.15); border:1px solid rgba(139,92,246,0.5); display:inline-block; font-weight:bold; box-shadow: 0 0 10px rgba(139,92,246,0.2); backdrop-filter: blur(5px);'>{skill.title()}</span>" for skill in analysis['missing_skills']]) if analysis['missing_skills'] else "<p>You have all required skills!</p>"
        st.markdown(f"""
<div class='border-glow-card' style='height: 100%;'>
    <span class='edge-light'></span>
    <div class='border-glow-inner'>
        <h3 style='color: #8b5cf6; font-weight: 900; letter-spacing: 2px; text-shadow: 0 0 10px rgba(139,92,246,0.5); margin-bottom: 25px; border-bottom: 1px solid rgba(139,92,246,0.3); padding-bottom: 15px;'>❌ GAP ANALYSIS</h3>
        <div>{missing_html}</div>
    </div>
</div>
""", unsafe_allow_html=True)
        
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    roadmap_html = ""
    roadmap_steps = generate_roadmap(analysis['missing_skills'])
    for step in roadmap_steps:
        # Parse headings
        if step.startswith("#### "):
            title = step.replace("#### ", "").strip()
            roadmap_html += f"<h4 style='color:#38bdf8; margin-top:30px; margin-bottom:15px; font-size:1.3rem; font-weight:900; text-transform:uppercase; letter-spacing:1px;'>{title}</h4>\n"
        # Parse timeline
        elif "Estimated Timeline:" in step:
            clean_step = step.replace("**", "").replace("*", "")
            roadmap_html += f"<div style='display:inline-block; background:rgba(244,114,182,0.15); border:1px solid rgba(244,114,182,0.4); padding:5px 15px; border-radius:20px; color:#f472b6; font-weight:bold; margin-bottom:15px; font-size:0.9rem;'>{clean_step}</div><br>\n"
        # Parse core concepts
        elif "Core Concepts to Master:" in step:
            clean_step = step.replace("**", "").replace("*", "")
            roadmap_html += f"<div style='color:#cbd5e1; margin-bottom:20px; font-size:1.05rem; line-height:1.6;'>{clean_step}</div>\n"
        # Parse recommended courses/actions and parse markdown links
        elif "Recommended" in step or "Action" in step:
            step_html = re.sub(r'\[([^\]]+)\]\(([^\)]+)\)', r"<a href='\2' style='color:#c4b5fd; text-decoration:underline; font-weight:bold;' target='_blank'>\1</a>", step)
            step_html = step_html.replace("- ", "").replace("*", "")
            roadmap_html += f"<div style='background:rgba(255,255,255,0.05); padding:20px; border-radius:10px; margin-bottom:15px; border-left:4px solid #8b5cf6; box-shadow:0 4px 6px rgba(0,0,0,0.1);'>👉 <span style='color:#f8fafc; font-size:1.1rem;'>{step_html}</span></div>\n"
        # Parse capstone projects
        elif "Capstone Project:" in step:
            step_html = step.replace("Capstone Project:", "").replace("- ", "").replace("*", "").strip()
            roadmap_html += f"<div style='background:rgba(6,182,212,0.05); padding:20px; border-radius:10px 10px 0 0; margin-top:10px; border-left:4px solid #06b6d4; border-bottom:1px solid rgba(6,182,212,0.2);'>🛠️ <span style='color:#f8fafc; font-size:1.15rem; font-weight:bold;'>{step_html}</span></div>\n"
        # Parse project abstract
        elif "Project Abstract:" in step:
            step_html = step.replace("Project Abstract:", "").replace("- ", "").replace("*", "").strip()
            step_html = step_html.replace("\n\n", "<br><br>")
            roadmap_html += f"<div style='background:rgba(6,182,212,0.02); padding:15px 20px; border-radius:0 0 10px 10px; margin-bottom:25px; border-left:4px solid #06b6d4; color:#94a3b8; font-size:1.05rem; line-height:1.6; box-shadow:0 4px 6px rgba(0,0,0,0.1);'>{step_html}</div>\n"
        # Parse standard text
        else:
            clean_step = step.replace("**", "").replace("*", "").replace("- ", "")
            if clean_step.strip():
                 roadmap_html += f"<p style='color:#94a3b8; margin-bottom:15px; font-size:1.1rem;'>{clean_step}</p>\n"

    st.markdown(f"""
<div class='border-glow-card' style='margin-bottom: 2rem;'>
<span class='edge-light'></span>
<div class='border-glow-inner'>
<h3 style='color: #f472b6; font-weight: 900; letter-spacing: 2px; text-shadow: 0 0 10px rgba(244,114,182,0.5); margin-bottom: 25px; border-bottom: 1px solid rgba(244,114,182,0.3); padding-bottom: 15px;'>📈 PROGRESS TRACKING</h3>
<div style='padding: 25px; background: rgba(0,0,0,0.3); border-radius: 15px; border: 1px solid rgba(255,255,255,0.1);'>
<div style='display: flex; justify-content: space-between; font-weight: 900; font-size: 1.3rem; margin-bottom: 15px; letter-spacing: 1px;'>
<span style='color: #cbd5e1;'>OVERALL ROLE MATCH</span>
<span style='color: #38bdf8; text-shadow: 0 0 10px rgba(56,189,248,0.5);'>{analysis['match_percentage']}%</span>
</div>
<div class='progress-track'>
<div class='progress-fill' style='width: {analysis['match_percentage']}%;'></div>
</div>
<p style='color: #94a3b8; font-size: 1rem; margin-top: 15px; text-align: center;'>Complete the roadmap below to reach 100% mastery.</p>
</div>
</div>
</div>

<div class='border-glow-card'>
<span class='edge-light'></span>
<div class='border-glow-inner'>
<h3 style='color: #a5f3fc; font-weight: 900; letter-spacing: 2px; text-shadow: 0 0 10px rgba(165,243,252,0.5); margin-bottom: 25px; border-bottom: 1px solid rgba(165,243,252,0.3); padding-bottom: 15px;'>🗺️ DETAILED LEARNING ROADMAP</h3>
<div>
{roadmap_html}
</div>
</div>
</div>
""", unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)
    
    _, col_btn, _ = st.columns([1, 1.5, 1])
    with col_btn:
        if st.button("← START OVER", type="primary"):
            st.session_state.page = 1
            st.session_state.analysis_results = None
            st.session_state.extracted_skills = None
            st.rerun()
