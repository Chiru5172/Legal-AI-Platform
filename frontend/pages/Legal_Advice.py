"""
2_Legal_Advice.py
-----------------
Legal Advice Page:
LAW EXPLORER ONLY (No AI, No Complaint Generator)
"""

import os
import sys
import streamlit as st

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

from legal_library.library_service import (
    get_all_categories,
    get_sections_by_category,
    get_section_details
)

st.set_page_config(
    page_title="Legal Advice - Law Explorer",
    page_icon="⚖️",
    layout="wide"
)

st.title("⚖️ Legal Advice — Law Explorer")

st.markdown(
    """
Explore Indian laws and legal provisions in a structured manner.
Select a category and section to view detailed legal explanations.

⚠️ *This section provides legal information only.*
"""
)

# --------------------------------------------------
# LAYOUT
# --------------------------------------------------
left_col, right_col = st.columns([1, 2])

# ==================================================
# LEFT PANEL — LAW EXPLORER
# ==================================================
with left_col:
    st.subheader("📚 Law Explorer")

    categories = get_all_categories()
    selected_category = st.selectbox(
        "Select Law Category",
        categories
    )

    sections = get_sections_by_category(selected_category)

    selected_section = st.radio(
        "Available Sections",
        sections
    )

# ==================================================
# RIGHT PANEL — SECTION DETAILS
# ==================================================
with right_col:
    st.subheader("📖 Section Details")

    details = get_section_details(selected_category, selected_section)

    if details:
        st.markdown(f"### {selected_section} — {details['title']}")
        st.markdown("**Description:**")
        st.write(details["description"])

        st.markdown("**Punishment / Remedy:**")
        st.success(details["punishment"])
    else:
        st.warning("No details available for the selected section.")
