"""
3_Complaint_Generator.py
-----------------------
Legal Advice:
- Get Legal Advice
- Generate a professionally formatted complaint letter
"""

import os
import sys
import streamlit as st
import textwrap

st.markdown(
    """
    <div style="padding:10px 0;">
        <h1 style="color:#1E3A8A;">⚖️ Legal Intelligence System</h1>
        <p style="color:#475569;">
            AI-powered legal research, advice, and complaint drafting
        </p>
    </div>
    """,
    unsafe_allow_html=True
)
st.markdown("---")


PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.append(PROJECT_ROOT)
from utils.pdf_generator import generate_complaint_pdf
import tempfile

from llm_services.crime_explainer import explain_crime
from legal_library.section_classifier import find_relevant_sections
from legal_library.library_service import get_section_details
from llm_services.letter_generator import generate_complaint_body
st.set_page_config(
    page_title="Legal Complaint Generator",
    page_icon="⚖️",
    layout="wide"
)
st.title("⚖️ Legal Advice")

left_col, right_col = st.columns([1, 2])

# --------------------------------------------------
# LEFT PANEL
# --------------------------------------------------
with left_col:
    st.subheader("⚖️ Legal Advice")

    mode = st.radio(
        "Select Service",
        (
            "🔍 Get Legal Advice",
            "📝 Generate Complaint Letter"
        )
    )

# --------------------------------------------------
# RIGHT PANEL
# --------------------------------------------------
with right_col:

    # ===============================
    # OPTION 1 — LEGAL ADVICE
    # ===============================
    if mode.startswith("🔍"):
        st.subheader("Describe the Legal Issue")

        issue = st.text_area(
            "Issue Description",
            height=160,
            placeholder="Example: Fake Instagram account created and money collected"
        )

        # ✅ ADDED BUTTON (ONLY CHANGE)
        generate_advice = st.button("🔎 Generate Legal Advice", use_container_width=True)

        if generate_advice:

            if not issue.strip():
                st.warning("Please describe the legal issue first.")
            else:
                with st.spinner("Analyzing legal issue..."):
                    explanation = explain_crime(issue)
                    sections = find_relevant_sections(issue)

                st.subheader("Legal Understanding")
                st.markdown(
                    f"""
                    <div style="
                        background-color:#FFFFFF;
                        padding:16px;
                        border-radius:10px;
                        border:1px solid #E5E7EB;
                        margin-bottom:15px;
                    ">
                        <h4>🧠 Legal Understanding</h4>
                        <p>{explanation}</p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )


                st.subheader("Applicable Legal Sections")
                for category, section in sections:
                    details = get_section_details(category, section)
                    if details:
                        with st.expander(f"{section} — {details['title']}"):
                            st.write(details["description"])
                            st.success(details["punishment"])

    # ===============================
    # OPTION 2 — COMPLAINT LETTER
    # ===============================
    elif mode.startswith("📝"):
        st.subheader("Incident Description")

        incident = st.text_area(
            "Incident Details",
            height=180,
            placeholder="Describe the incident clearly and factually."
        )

        if st.button("📝 Generate Complaint Letter", use_container_width=True):

            if not incident.strip():
                st.error("Please provide the incident description.")
            else:
                with st.spinner("Drafting complaint letter..."):
                    body = generate_complaint_body(incident)

                # ---------------------------
                # ENFORCED LEGAL FORMAT
                # ---------------------------
                formatted_body = textwrap.fill(body, width=70)
                indented_body = textwrap.indent(formatted_body, "    ")

                letter = f"""
                               COMPLAINT

From,
[Complainant Name]
[Address]

To,
The Station House Officer
[Police Station Name]

Subject: Complaint regarding the incident

Respected Sir/Madam,

{indented_body}

    I therefore request you to kindly register my complaint and initiate
    appropriate legal action in accordance with law.

Thanking you.

Yours sincerely,

[Complainant Name]
"""

                st.subheader("📄 Complaint Letter (Ready for Submission)")
                st.text_area("Generated Letter", value=letter.strip(), height=500)

                # Download as TXT
                st.download_button(
                    "📥 Download as Text",
                    letter,
                    file_name="police_complaint.txt",
                    mime="text/plain"
                )

                # Download as PDF
                with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
                    generate_complaint_pdf(letter, tmp.name)
                    with open(tmp.name, "rb") as pdf_file:
                        st.download_button(
                            "📄 Download as PDF",
                            pdf_file,
                            file_name="police_complaint.pdf",
                            mime="application/pdf"
                        )