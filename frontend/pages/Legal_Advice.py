"""
2_Legal_Advice.py
-----------------
Legal Advice Page:
LAW EXPLORER ONLY (No AI, No Complaint Generator)
"""

import os
import sys
import streamlit as st

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.append(PROJECT_ROOT)

from frontend.theme import load_css, render_hero, render_theme_toggle, render_legal_section_card, render_section_header

if "dark_mode" not in st.session_state:
    st.session_state["dark_mode"] = True

st.set_page_config(
    page_title="Legal Advice – Law Explorer",
    page_icon="⚖️",
    layout="wide"
)

load_css()
render_theme_toggle()
render_hero("⚖️ Law Explorer", "Explore Indian laws and legal provisions in a structured manner")

from legal_library.library_service import (
    get_all_categories,
    get_sections_by_category,
    get_section_details
)

# --------------------------------------------------
# LAYOUT
# --------------------------------------------------
left_col, right_col = st.columns([1, 2], gap="large")

# ==================================================
# LEFT PANEL — LAW EXPLORER
# ==================================================
with left_col:
    render_section_header("📚 Browse Laws")

    categories = get_all_categories()
    selected_category = st.selectbox(
        "Law Category",
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
    render_section_header("📖 Section Details")

    details = get_section_details(selected_category, selected_section)

    if details:
        render_legal_section_card(
            f"{selected_section} — {details['title']}",
            details["description"],
            details["punishment"]
        )
    else:
        st.warning("No details available for the selected section.")
