import streamlit as st
import pandas as pd

from extractor import extract_text
from analyzer import detect_skills
from scorer import calculate_ats_score, get_rating
from parser import (
    extract_name,
    extract_email,
    extract_phone,
    detect_education,
    detect_experience
)
from matcher import (
    extract_jd_skills,
    calculate_match_score,
    get_missing_skills
)

# ==========================================
# PAGE SETTINGS
# ==========================================

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Resume Analyzer")

# ==========================================
# FILE UPLOADS
# ==========================================

resume_file = st.file_uploader(
    "Upload Resume PDF",
    type=["pdf"]
)

jd_file = st.file_uploader(
    "Upload Job Description",
    type=["txt", "pdf"]
)

# ==========================================
# MAIN LOGIC
# ==========================================

if resume_file:

    # Save Resume
    with open("uploaded_resume.pdf", "wb") as f:
        f.write(resume_file.getbuffer())

    # Extract Resume Text
    resume_text = extract_text(
        "uploaded_resume.pdf"
    )

    # Candidate Information
    candidate_name = extract_name(
        resume_text
    )

    email = extract_email(
        resume_text
    )

    phone = extract_phone(
        resume_text
    )

    education = detect_education(
        resume_text
    )

    experience = detect_experience(
        resume_text
    )

    # Skills
    skills = detect_skills(
        resume_text
    )

    # ATS Score
    ats_score = calculate_ats_score(
        resume_text,
        skills
    )

    rating = get_rating(
        ats_score
    )

    # Default Values
    match_score = 0
    jd_skills = []
    missing_skills = []

    # ==========================================
    # JOB DESCRIPTION
    # ==========================================

    if jd_file is not None:

        jd_text = ""

        # TXT File
        if jd_file.name.endswith(".txt"):

            jd_text = jd_file.read().decode(
                "utf-8"
            )

        # PDF File
        elif jd_file.name.endswith(".pdf"):

            with open(
                "uploaded_jd.pdf",
                "wb"
            ) as f:

                f.write(
                    jd_file.getbuffer()
                )

            jd_text = extract_text(
                "uploaded_jd.pdf"
            )

        if jd_text:

            jd_skills = extract_jd_skills(
                jd_text
            )

            match_score = calculate_match_score(
                skills,
                jd_skills
            )

            missing_skills = get_missing_skills(
                skills,
                jd_skills
            )

    # ==========================================
    # SUCCESS MESSAGE
    # ==========================================

    st.success(
        "Resume Uploaded Successfully"
    )

    # ==========================================
    # DASHBOARD METRICS
    # ==========================================

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "ATS Score",
            f"{ats_score}/100"
        )

    with col2:
        st.metric(
            "Job Match",
            f"{match_score}%"
        )

    with col3:
        st.metric(
            "Skills Found",
            len(skills)
        )

    # ==========================================
    # CANDIDATE INFO
    # ==========================================

    st.header(
        "👤 Candidate Information"
    )

    st.write(
        f"**Name:** {candidate_name}"
    )

    st.write(
        f"**Email:** {email}"
    )

    st.write(
        f"**Phone:** {phone}"
    )

    st.write(
        f"**Education:** {education}"
    )

    st.write(
        f"**Experience:** {experience}"
    )

    # ==========================================
    # ATS ANALYSIS
    # ==========================================

    st.header(
        "📊 ATS Analysis"
    )

    st.subheader(
        "ATS Progress"
    )

    st.progress(
        min(int(ats_score), 100)
    )

    st.write(
        f"**Resume Rating:** {rating}"
    )

    # ==========================================
    # SKILLS
    # ==========================================

    st.header(
        "🛠 Skills Found"
    )

    if skills:

        for skill in skills:

            st.write(
                f"✅ {skill}"
            )

    else:

        st.warning(
            "No skills detected."
        )

    # ==========================================
    # SKILLS CHART
    # ==========================================

    st.subheader(
        "📈 Skills Chart"
    )

    chart_data = pd.DataFrame(
        {
            "Skills": [len(skills)]
        }
    )

    st.bar_chart(
        chart_data
    )

    # ==========================================
    # JOB MATCH ANALYSIS
    # ==========================================

    if jd_file is not None:

        st.header(
            "🎯 Job Match Analysis"
        )

        st.subheader(
            "Job Match Progress"
        )

        st.progress(
            min(int(match_score), 100)
        )

        st.write(
            f"**Match Score:** {match_score}%"
        )

        st.subheader(
            "Required Skills"
        )

        if jd_skills:

            for skill in jd_skills:

                st.write(
                    f"📌 {skill}"
                )

        st.subheader(
            "Missing Skills"
        )

        if missing_skills:

            for skill in missing_skills:

                st.write(
                    f"❌ {skill}"
                )

        else:

            st.success(
                "No missing skills found."
            )

    # ==========================================
    # RESUME TEXT
    # ==========================================

    with st.expander(
        "View Extracted Resume Text"
    ):

        st.text_area(
            "Resume Content",
            resume_text,
            height=400
        )