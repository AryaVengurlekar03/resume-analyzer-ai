from extractor import extract_text

resume_path = "resume/Arya Vengurlekar Resume.pdf"

resume_text = extract_text(resume_path)

print("=" * 50)
print("RESUME TEXT")
print("=" * 50)

print(resume_text)