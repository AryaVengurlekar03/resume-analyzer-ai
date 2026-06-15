from extractor import extract_text
from analyzer import detect_skills
from scorer import calculate_ats_score, get_rating, get_recommendations
from matcher import (
    read_job_description,
    extract_jd_skills,
    calculate_match_score,
    get_missing_skills
)
from parser import (
    extract_email,
    extract_phone,
    extract_name,
    detect_education,
    detect_experience
)

# ==========================================
# STEP 1: Load Resume
# ==========================================

resume_path = "resume/Arya Vengurlekar Resume.pdf"
resume_text = extract_text(resume_path)

# ==========================================
# STEP 2: Extract Candidate Information
# ==========================================

candidate_name = extract_name(resume_text)
email = extract_email(resume_text)
phone = extract_phone(resume_text)

education = detect_education(resume_text)
experience = detect_experience(resume_text)

# ==========================================
# STEP 3: Detect Skills
# ==========================================

skills = detect_skills(resume_text)

# ==========================================
# STEP 4: ATS Score
# ==========================================

ats_score = calculate_ats_score(
    resume_text,
    skills
)

rating = get_rating(ats_score)

recommendations = get_recommendations(
    ats_score
)

# ==========================================
# STEP 5: Job Description Matching
# ==========================================

jd_text = read_job_description(
    "job_description.txt"
)

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
# STEP 6: Display Report
# ==========================================

print("=" * 60)
print("              RESUME ANALYSIS REPORT")
print("=" * 60)

print(f"\nCandidate Name : {candidate_name}")
print(f"Email          : {email}")
print(f"Phone          : {phone}")

print(f"\nEducation      : {education}")
print(f"Experience     : {experience}")

print(f"\nATS Score      : {ats_score}/100")
print(f"Resume Rating  : {rating}")
print(f"Job Match      : {match_score}%")

print("\nSkills Found:")

if skills:
    for skill in skills:
        print(f"✓ {skill}")
else:
    print("No skills found")

print(f"\nTotal Skills Found: {len(skills)}")

print("\nMissing Skills:")

if missing_skills:
    for skill in missing_skills:
        print(f"- {skill}")
else:
    print("No missing skills")

print("\nRecommendations:")

if recommendations:
    for item in recommendations:
        print(f"- {item}")
else:
    print("Resume looks good!")

print("\n" + "=" * 60)
print("                 REPORT COMPLETE")
print("=" * 60)