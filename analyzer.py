def load_skills():

    with open("skills.txt", "r") as file:

        skills = []

        for line in file:

            skills.append(line.strip().lower())

    return skills
def detect_skills(resume_text):

    skills_db = load_skills()

    found_skills = []

    resume_text = resume_text.lower()

    for skill in skills_db:

        if skill in resume_text:

            found_skills.append(skill)

    return found_skills