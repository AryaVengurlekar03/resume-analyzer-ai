import re


# ==========================================
# Extract Email
# ==========================================

def extract_email(text):

    pattern = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'

    emails = re.findall(pattern, text)

    if emails:
        return emails[0]

    return "Not Found"


# ==========================================
# Extract Phone Number
# ==========================================

def extract_phone(text):

    pattern = r'(\+?\d[\d\s\-]{8,15})'

    phones = re.findall(pattern, text)

    if phones:
        return phones[0]

    return "Not Found"


# ==========================================
# Extract Candidate Name
# ==========================================

def extract_name(text):

    lines = text.split("\n")

    for line in lines:

        line = line.strip()

        if line:

            words = line.split()

            return " ".join(words[:2])

    return "Not Found"


# ==========================================
# Detect Education
# ==========================================

def detect_education(text):

    text = text.lower()

    if "bachelor of engineering" in text:
        return "Bachelor of Engineering"

    elif "b.e" in text:
        return "B.E."

    elif "b.tech" in text:
        return "B.Tech"

    elif "engineering" in text:
        return "Engineering Degree"

    elif "master" in text:
        return "Master Degree"

    return "Education Not Found"


# ==========================================
# Detect Experience
# ==========================================

def detect_experience(text):

    text = text.lower()

    if "internship" in text:
        return "Internship Found"

    elif "developer" in text:
        return "Developer Experience Found"

    elif "engineer" in text:
        return "Engineering Experience Found"

    elif "analyst" in text:
        return "Analyst Experience Found"

    return "No Experience Found"