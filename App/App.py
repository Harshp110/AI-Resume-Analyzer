# Built with 🤍 by Harsh S. Pandav
# AI Resume Analyzer – Streamlit Cloud Safe Version

import streamlit as st
import pandas as pd
import base64, random, time, datetime
import io
import plotly.express as px
from pdfminer.high_level import extract_text
from streamlit_tags import st_tags
from PIL import Image

# ---------------- CONFIG ----------------
st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

# ---------------- DUMMY PARSER ----------------
def dummy_resume_parser(text):
    skills_db = [
        "python","machine learning","data analysis","sql","java","c++",
        "react","django","flask","streamlit","html","css","javascript",
        "android","kotlin","flutter","ios","swift","figma","ui","ux"
    ]
    found_skills = [s.title() for s in skills_db if s in text.lower()]
    return {
        "name": "Demo User",
        "email": "demo@email.com",
        "skills": list(set(found_skills)) if found_skills else ["Python"],
        "pages": 1
    }

# ---------------- PDF FUNCTIONS ----------------
def read_pdf(file):
    return extract_text(file)

def show_pdf(file_bytes):
    b64 = base64.b64encode(file_bytes).decode()
    st.markdown(
        f'<iframe src="data:application/pdf;base64,{b64}" width="700" height="900"></iframe>',
        unsafe_allow_html=True
    )

# ---------------- COURSES ----------------
ds_courses = [
    ("Machine Learning", "https://www.coursera.org/learn/machine-learning"),
    ("Data Science", "https://www.coursera.org/professional-certificates/ibm-data-science"),
]

web_courses = [
    ("Full Stack Web Dev", "https://www.udemy.com/course/the-web-developer-bootcamp/"),
    ("React JS", "https://react.dev/learn"),
]

# ---------------- UI ----------------
st.title("🌴 AI RESUME ANALYZER 🌴")
st.markdown("**Upload your resume and get instant insights & recommendations**")

menu = st.sidebar.selectbox("Choose Section", ["User", "About"])
st.sidebar.markdown(
    "<b>Built with 🤍 by <a href='https://github.com/Harshp110'>Harsh S. Pandav</a></b>",
    unsafe_allow_html=True
)

# ---------------- USER ----------------
if menu == "User":
    name = st.text_input("Your Name")
    email = st.text_input("Email")

    pdf_file = st.file_uploader("Upload Resume (PDF only)", type=["pdf"])

    if pdf_file:
        st.success("Resume uploaded successfully!")
        show_pdf(pdf_file.getvalue())

        text = read_pdf(pdf_file)
        resume_data = dummy_resume_parser(text)

        st.header("📊 Resume Analysis")

        st.write("**Name:**", resume_data["name"])
        st.write("**Email:**", resume_data["email"])

        st.subheader("🧠 Skills Found")
        st_tags(
            label="Your Skills",
            value=resume_data["skills"],
            text="Extracted from resume"
        )

        # Recommendations
        reco_field = "Data Science" if "Python" in resume_data["skills"] else "Web Development"

        st.subheader("🎯 Predicted Field")
        st.success(reco_field)

        st.subheader("📚 Course Recommendations")
        courses = ds_courses if reco_field == "Data Science" else web_courses
        for c, link in courses:
            st.markdown(f"- [{c}]({link})")

        # Resume Score
        score = min(100, len(resume_data["skills"]) * 10)
        st.subheader("📝 Resume Score")
        st.progress(score)
        st.success(f"Score: {score}/100")

        st.balloons()

# ---------------- ABOUT ----------------
elif menu == "About":
    st.header("About AI Resume Analyzer")
    st.markdown("""
    AI Resume Analyzer is a smart tool that analyzes resumes,
    extracts skills, predicts job roles, and recommends learning paths.

    **Key Features**
    - Resume upload & PDF parsing
    - Skill extraction
    - Job role prediction
    - Course recommendations
    - Resume scoring

    **Built by:** Harsh S. Pandav  
    **Tech:** Streamlit, Python, NLP basics
    """)

# ---------------- END ----------------
