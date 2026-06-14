from extractor import extract_text
from analyzer import detect_skills
from scorer import calculate_ats_score, get_rating, get_recommendations
from matcher import read_job_description, extract_jd_skills, calculate_match_score, get_missing_skills


# ==========================================
# STEP 1: Load Resume
# ==========================================
resume_path = "resume/Arya Vengurlekar Resume.pdf"

resume_text = extract_text(resume_path)

# ==========================================
# STEP 2: Detect Skills
# ==========================================
skills = detect_skills(resume_text)

# ==========================================
# STEP 3: Calculate ATS Score
# ==========================================
ats_score = calculate_ats_score(resume_text, skills)

# ==========================================
# STEP 4: Get Rating
# ==========================================
rating = get_rating(ats_score)

# ==========================================
# STEP 5: Display Results
# ==========================================
print("=" * 50)
print("         RESUME ANALYSIS REPORT")
print("=" * 50)

print("\nSkills Found:")

if skills:
    for skill in skills:
        print(f"✓ {skill}")
else:
    print("No skills detected.")

print("\nTotal Skills Found:", len(skills))

print("\nATS Score:", ats_score, "/100")

print("\nResume Rating:")
print(rating)

print("\n" + "=" * 50)

# recommendation

recommendations = get_recommendations(
    ats_score
)

print("\nRecommendations:")

for item in recommendations:
    print("-", item)

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

print("\nJob Match Score:")
print(match_score, "%")

print("\nMissing Skills:")

for skill in missing_skills:
    print("-", skill)