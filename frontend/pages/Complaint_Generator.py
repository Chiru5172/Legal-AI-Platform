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


PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.append(PROJECT_ROOT)

from frontend.theme import (
    load_css, render_hero, render_theme_toggle,
    render_section_header, render_legal_section_card, _p
)

if "dark_mode" not in st.session_state:
    st.session_state["dark_mode"] = True

st.set_page_config(
    page_title="Legal Complaint Generator",
    page_icon="📝",
    layout="wide"
)

load_css()
render_theme_toggle()
render_hero("📝 Complaint Generator", "Describe your legal issue and get AI-powered advice or a formal complaint letter")

from utils.pdf_generator import generate_complaint_pdf
import tempfile

from llm_services.crime_explainer import explain_crime
from legal_library.section_classifier import find_relevant_sections
from legal_library.library_service import get_section_details
from llm_services.letter_generator import generate_complaint_body

left_col, right_col = st.columns([1, 2], gap="large")

# --------------------------------------------------
# LEFT PANEL
# --------------------------------------------------
with left_col:
    render_section_header("⚙️ Select Service")

    mode = st.radio(
        "What would you like to do?",
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
        render_section_header("Describe Your Legal Issue")

        issue = st.text_area(
            "Issue Description",
            height=160,
            placeholder="Example: Fake Instagram account created and money collected"
        )

        if st.button("🔎 Generate Legal Advice", use_container_width=True):
            if not issue.strip():
                st.warning("Please describe the legal issue first.")
            else:
                with st.spinner("Analyzing legal issue..."):
                    explanation = explain_crime(issue)
                    sections = find_relevant_sections(issue)

                render_section_header("🧠 Legal Understanding")
                p = _p()
                st.markdown(f"""
                <div style="
                    background:{p['surface']};
                    border:1.5px solid {p['border']};
                    border-left:5px solid {p['accent']};
                    border-radius:12px;
                    padding:20px 24px;
                    color:{p['text']};
                    font-size:0.95rem;
                    line-height:1.75;
                    margin:10px 0 20px;
                ">
                    {explanation}
                </div>
                """, unsafe_allow_html=True)

                render_section_header("⚖️ Applicable Legal Sections")
                for category, section in sections:
                    details = get_section_details(category, section)
                    if details:
                        render_legal_section_card(
                            f"{section} — {details['title']}",
                            details["description"],
                            details["punishment"]
                        )

    # ===============================
    # OPTION 2 — COMPLAINT LETTER
    # ===============================
    elif mode.startswith("📝"):
        render_section_header("📋 Complainant Details")

        p = _p()
        col_name, col_date = st.columns(2)
        with col_name:
            complainant_name = st.text_input("Complainant Name", placeholder="Your Full Name")
        with col_date:
            complaint_date = st.text_input("Date", placeholder="e.g. 09/03/2026")

        col_addr, col_ps = st.columns(2)
        with col_addr:
            complainant_address = st.text_input("Address", placeholder="Your Address")
        with col_ps:
            police_station = st.text_input("Police Station", placeholder="Name of Police Station")

        render_section_header("📋 Incident Description")

        incident = st.text_area(
            "Describe what happened (clearly and factually, in first person)",
            height=180,
            placeholder=(
                "Example: On 05/03/2026, a person named [Name] approached me "
                "and fraudulently collected ₹50,000 from me by posing as a government official. "
                "He promised to get my son a government job but disappeared after collecting the money."
            )
        )

        if st.button("📝 Generate Complaint Letter", use_container_width=True):

            if not incident.strip():
                st.error("Please provide the incident description.")
            else:
                # Use provided values or sensible placeholders
                name_val    = complainant_name.strip() or "[Complainant Name]"
                addr_val    = complainant_address.strip() or "[Address]"
                ps_val      = police_station.strip() or "[Police Station Name]"
                date_val    = complaint_date.strip() or "[Date]"

                # Smart subject line from first 80 chars of incident
                subject_snippet = incident.strip()[:80].rstrip(" ,.;")
                if len(incident.strip()) > 80:
                    subject_snippet += "..."

                with st.spinner("Drafting complaint letter..."):
                    body = generate_complaint_body(incident)

                letter = (
                    f"                         COMPLAINT\n\n"
                    f"Date: {date_val}\n\n"
                    f"From,\n"
                    f"{name_val}\n"
                    f"{addr_val}\n\n"
                    f"To,\n"
                    f"The Station House Officer\n"
                    f"{ps_val}\n\n"
                    f"Subject: Complaint regarding – {subject_snippet}\n\n"
                    f"Respected Sir/Madam,\n\n"
                    f"{body}\n\n"
                    f"Yours faithfully,\n\n"
                    f"{name_val}\n"
                    f"Date: {date_val}"
                )

                render_section_header("📄 Complaint Letter (Ready for Submission)")
                st.markdown(f"""
                <div style="
                    background:{p['surface']};
                    border:1.5px solid {p['border']};
                    border-radius:12px;
                    padding:24px 28px;
                    font-family: 'Courier New', monospace;
                    font-size:0.88rem;
                    color:{p['text']};
                    line-height:1.9;
                    white-space:pre-wrap;
                    margin-bottom:16px;
                ">
{letter.strip()}
                </div>
                """, unsafe_allow_html=True)

                col_a, col_b = st.columns(2)
                with col_a:
                    st.download_button(
                        "📥 Download as Text",
                        letter,
                        file_name="police_complaint.txt",
                        mime="text/plain",
                        use_container_width=True
                    )
                with col_b:
                    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
                        generate_complaint_pdf(letter, tmp.name)
                        with open(tmp.name, "rb") as pdf_file:
                            st.download_button(
                                "📄 Download as PDF",
                                pdf_file,
                                file_name="police_complaint.pdf",
                                mime="application/pdf",
                                use_container_width=True
                            )