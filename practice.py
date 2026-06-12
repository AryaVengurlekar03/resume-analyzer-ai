resume_text = """
I know Python, SQL and Git.
"""

skills = [
    "Python",
    "SQL",
    "AWS",
    "Docker",
    "Git"
]

for skill in skills:

    if skill.lower() in resume_text.lower():

        print(skill, "Found")