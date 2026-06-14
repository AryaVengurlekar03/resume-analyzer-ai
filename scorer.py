def calculate_ats_score(resume_text, skills):

    score = 0

    # Skills Score
    skills_score = min(len(skills) * 4, 40)
    score += skills_score

    # Education
    if "education" in resume_text.lower():
        score += 20

    # Projects
    if "project" in resume_text.lower():
        score += 20

    # Experience
    if "experience" in resume_text.lower():
        score += 20

    return score
def get_rating(score):

    if score >= 80:
        return "EXCELLENT"

    elif score >= 60:
        return "GOOD"

    elif score >= 40:
        return "AVERAGE"

    else:
        return "NEEDS IMPROVEMENT"
    

#recommendation

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

    return recommendations