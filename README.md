# 📄 AI-Powered ATS Resume Intelligence Platform

## About the Project

The AI-Powered ATS Resume Intelligence Platform is a web application built to help job seekers evaluate and improve their resumes. It analyzes resumes against job descriptions, calculates an ATS score, identifies missing skills, and provides recommendations to improve the chances of passing Applicant Tracking Systems (ATS).

The application also generates downloadable PDF reports and stores previous analyses using a SQLite database.

---

## Features

* Upload Resume (PDF)
* Upload Job Description (PDF/TXT)
* Extract candidate information (Name, Email, Phone)
* Detect skills, education, experience, projects, and certifications
* Calculate ATS Score
* Compare resume with a job description
* Identify missing skills
* Generate resume improvement recommendations
* Interactive Streamlit dashboard
* Download analysis as a PDF report
* Store previous analyses using SQLite

---

## Tech Stack

* Python
* Streamlit
* Pandas
* SQLite
* PDFPlumber
* FPDF
* Regular Expressions (Regex)

---

## Project Structure

```text
resume_analyzer/

├── app.py
├── analyzer.py
├── extractor.py
├── parser.py
├── matcher.py
├── scorer.py
├── report.py
├── database.py
├── requirements.txt
└── README.md
```

---

## How to Use

1. Clone this repository to your local machine.

```bash
git clone https://github.com/your-username/your-repository-name.git
```

2. Install the required dependencies.

```bash
pip install -r requirements.txt
```

3. Start the application.

```bash
streamlit run app.py
```

4. Open the application in your browser.

5. Upload a resume in **PDF** format.

6. (Optional) Upload a **PDF** or **TXT** job description.

7. View the generated ATS score, job match score, detected skills, recommendations, and resume analysis.

8. Download the generated PDF report or review previous analyses stored in the database.

---

## Workflow

```text
Resume + Job Description
          │
          ▼
   Text Extraction
          │
          ▼
   Resume Parsing
          │
          ▼
Skills • Education • Experience
Projects • Certifications
          │
          ▼
 ATS Score Calculation
          │
          ▼
 Job Match Analysis
          │
          ▼
 Recommendations
          │
          ▼
 Dashboard + PDF Report + Database
```

---

## Future Improvements

Planned features include:

* AI Semantic Resume Matching
* AI Resume Rewriter
* AI Interview Question Generator
* Resume Ranking System
* Career Recommendation System

---

## Author

**Arya Vengurlekar**

If you have any suggestions or feedback, feel free to connect or open an issue on GitHub.
