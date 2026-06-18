from parser import (
    detect_education,
    detect_experience,
    detect_projects,
    detect_certifications
)


def calculate_ats_score(
    resume_text,
    skills
):

    score = 0

    # Skills (30 marks)
    skill_score = min(
        len(skills) * 3,
        30
    )

    score += skill_score

    # Education (15 marks)
    if detect_education(
        resume_text
    ) != "Education Not Found":

        score += 15

    # Experience (25 marks)
    if detect_experience(
        resume_text
    ) != "No Experience Found":

        score += 25

    # Projects (20 marks)
    if detect_projects(
        resume_text
    ):

        score += 20

    # Certifications (10 marks)
    if detect_certifications(
        resume_text
    ):

        score += 10

    return min(score, 100)


def get_rating(score):

    if score >= 85:
        return "EXCELLENT"

    elif score >= 70:
        return "GOOD"

    elif score >= 50:
        return "AVERAGE"

    else:
        return "NEEDS IMPROVEMENT"


def get_recommendations(score):

    recommendations = []

    if score < 80:

        recommendations.append(
            "Add more technical skills"
        )

        recommendations.append(
            "Include more projects"
        )

        recommendations.append(
            "Mention internships or experience"
        )

    else:

        recommendations.append(
            "Resume looks strong"
        )

    return recommendations