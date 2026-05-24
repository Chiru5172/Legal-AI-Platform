"""
1_Home_RAG.py
-------------
Home page: RAG-based Legal Document Analysis
"""

import os
import sys
import tempfile
import streamlit as st

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.append(PROJECT_ROOT)

from frontend.theme import load_css, render_hero, render_theme_toggle, render_answer_box, render_section_header

# Bootstrap dark mode default
if "dark_mode" not in st.session_state:
    st.session_state["dark_mode"] = True

st.set_page_config(
    page_title="Legal AI – Research",
    page_icon="🔍",
    layout="wide"
)

load_css()
render_theme_toggle()
render_hero("🔍 Legal Research", "Ask questions over your uploaded legal documents using AI")

from backend.api import handle_query
from ingestion.pdf_loader import load_legal_pdfs_from_path
from ingestion.text_cleaner import clean_documents
from ingestion.chunker import chunk_documents
from embeddings.vector_store import build_faiss_index

render_section_header("📂 Upload & Query")

uploaded_files = st.file_uploader(
    "Upload Legal PDF(s)",
    type=["pdf"],
    accept_multiple_files=True
)

top_k = st.slider("Number of evidence chunks", 1, 10, 3)

query = st.text_area(
    "Enter your legal query",
    height=100,
    placeholder="Example: What rights of arrested persons are discussed?"
)


def process_uploaded_pdfs(files):
    temp_dir = tempfile.mkdtemp()
    for file in files:
        with open(os.path.join(temp_dir, file.name), "wb") as f:
            f.write(file.getbuffer())
    docs = load_legal_pdfs_from_path(temp_dir)
    cleaned = clean_documents(docs)
    chunks = chunk_documents(cleaned)
    return build_faiss_index(chunks)


if st.button("🔎 Analyze", use_container_width=False) and query.strip():

    if uploaded_files:
        with st.spinner("Processing uploaded documents..."):
            vectorstore = process_uploaded_pdfs(uploaded_files)
    else:
        vectorstore = None

    with st.spinner("Analyzing legal documents..."):
        response = handle_query(query, top_k, vectorstore)

    render_section_header("🧠 Legal Answer")
    answer_text = response.answer or "The provided documents do not contain sufficient information to answer this question."
    render_answer_box(answer_text)
    if not response.answer:
        st.warning("The model returned an empty answer. Try rephrasing your query.")

    render_section_header("📊 Confidence")
    confidence = min(0.95, 0.5 + 0.1 * len(response.evidence))
    st.progress(confidence)

    render_section_header("📌 Evidence")
    for i, ev in enumerate(response.evidence, 1):
        with st.expander(f"Evidence {i} — {ev.source} (Page {ev.page_number})"):
            st.write(ev.content)
