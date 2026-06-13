from extractor import extract_text
from analyzer import detect_skills

resume_path = "resume/Arya Vengurlekar Resume.pdf"

resume_text = extract_text(resume_path)

skills = detect_skills(resume_text)

print("\nSkills Found:\n")

for skill in skills:

    print("-", skill)
    
    print("\nTotal Skills Found:", len(skills))

    all_skills = [
    "python",
    "sql",
    "aws",
    "docker",
    "kubernetes"
]

missing = []

for skill in all_skills:

    if skill not in skills:

        missing.append(skill)

print("\nMissing Skills:")

for skill in missing:

    print("-", skill)


    print("=" * 50)
print("RESUME ANALYSIS")
print("=" * 50)

print("\nSkills Found:")

for skill in skills:
    print("✓", skill)

print("\nTotal Skills:", len(skills))