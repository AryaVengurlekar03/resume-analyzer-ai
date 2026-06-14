def read_job_description(path):

    with open(path, "r", encoding="utf-8") as file:

        return file.read()

#reads job desription


def calculate_match_score(
        resume_skills,
        jd_skills
):

    matched = 0

    for skill in jd_skills:

        if skill in resume_skills:

            matched += 1

    if len(jd_skills) == 0:
        return 0

    return round(
        (matched / len(jd_skills)) * 100,
        2
    )


def get_missing_skills(
        resume_skills,
        jd_skills
):

    missing = []

    for skill in jd_skills:

        if skill not in resume_skills:

            missing.append(skill)

    return missing

#finding missing skills


from analyzer import load_skills


def extract_jd_skills(jd_text):

    skills_db = load_skills()

    found_skills = []

    jd_text = jd_text.lower()

    for skill in skills_db:

        if skill in jd_text:

            found_skills.append(skill)

    return found_skills