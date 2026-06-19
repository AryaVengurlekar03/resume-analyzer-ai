from fpdf import FPDF


def generate_report(
    name,
    email,
    phone,
    ats_score,
    rating,
    skills,
    missing_skills
):

    pdf = FPDF()

    pdf.add_page()

    pdf.set_font(
        "Arial",
        size=12
    )

    pdf.cell(
        200,
        10,
        "Resume Analysis Report",
        ln=True
    )

    pdf.ln(5)

    pdf.cell(
        200,
        10,
        f"Name: {name}",
        ln=True
    )

    pdf.cell(
        200,
        10,
        f"Email: {email}",
        ln=True
    )

    pdf.cell(
        200,
        10,
        f"Phone: {phone}",
        ln=True
    )

    pdf.ln(5)

    pdf.cell(
        200,
        10,
        f"ATS Score: {ats_score}",
        ln=True
    )

    pdf.cell(
        200,
        10,
        f"Rating: {rating}",
        ln=True
    )

    pdf.ln(5)

    pdf.cell(
        200,
        10,
        "Skills Found:",
        ln=True
    )

    for skill in skills:

        pdf.cell(
            200,
            10,
            f"- {skill}",
            ln=True
        )

    pdf.ln(5)

    pdf.cell(
        200,
        10,
        "Missing Skills:",
        ln=True
    )

    for skill in missing_skills:

        pdf.cell(
            200,
            10,
            f"- {skill}",
            ln=True
        )

    pdf.output(
        "Resume_Report.pdf"
    )