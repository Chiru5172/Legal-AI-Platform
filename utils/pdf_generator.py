"""
pdf_generator.py
----------------
Utility to convert complaint letter text into a formatted PDF.
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.units import inch


def generate_complaint_pdf(text: str, output_path: str):
    """
    Generate a properly formatted PDF for a police complaint letter.
    """

    doc = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        rightMargin=50,
        leftMargin=50,
        topMargin=50,
        bottomMargin=50
    )

    styles = getSampleStyleSheet()
    style = styles["Normal"]
    style.spaceAfter = 12

    story = []

    for line in text.split("\n"):
        if line.strip() == "":
            story.append(Spacer(1, 0.2 * inch))
        else:
            story.append(Paragraph(line.replace("&", "&amp;"), style))

    doc.build(story)
