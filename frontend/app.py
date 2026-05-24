"""
app.py
------
Main entry point for the Legal AI Platform (Multi-page App).
"""

import os
import sys
import streamlit as st

st.set_page_config(
    page_title="Legal AI Platform",
    page_icon="⚖️",
    layout="wide"
)

# Bootstrap dark mode default before any render
if "dark_mode" not in st.session_state:
    st.session_state["dark_mode"] = True

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__) + "/..")
sys.path.append(PROJECT_ROOT)

from frontend.theme import (
    load_css, render_theme_toggle, render_hero,
    render_card, render_action_card, render_disclaimer, render_section_header
)

# Apply premium global UI styles (must come after session_state init)
load_css()

# Render the theme toggle in sidebar
render_theme_toggle()

# Render Premium Hero Section
render_hero("⚖️ Legal AI Platform", "An AI-powered system for legal research, advice, and complaint drafting")

render_section_header("🚀 Platform Capabilities")

col1, col2 = st.columns(2, gap="medium")

with col1:
    render_card("📄 Legal Document Analysis", "Upload legal PDFs and query them using Retrieval-Augmented Generation (RAG).")
    render_card("🧠 Evidence-backed Research", "All answers are grounded in legal documents with citations.")

with col2:
    render_card("📚 Law Explorer", "Explore criminal, civil, cyber, and constitutional law sections.")
    render_card("📝 Complaint Drafting", "Generate professionally formatted, submission-ready complaint letters.")

render_section_header("⚡ Quick Actions")

col1, col2, col3 = st.columns(3, gap="medium")

with col1:
    render_action_card("🔍 Legal Research", "Ask questions over uploaded legal documents", "Home_RAG")

with col2:
    render_action_card("⚖️ Law Explorer", "Understand crimes and applicable sections", "Legal_Advice")

with col3:
    render_action_card("📝 Draft Complaint", "Generate submission-ready complaint letters", "Complaint_Generator")

render_disclaimer("This platform provides legal information and drafting assistance only. It is not a substitute for professional legal advice.")
