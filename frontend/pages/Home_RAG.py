"""
1_Home_RAG.py
-------------
Home page: RAG-based Legal Document Analysis
"""

import os
import sys
import tempfile
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

from backend.api import handle_query
from ingestion.pdf_loader import load_legal_pdfs_from_path
from ingestion.text_cleaner import clean_documents
from ingestion.chunker import chunk_documents
from embeddings.vector_store import build_faiss_index

st.set_page_config(
    page_title="Legal AI Home",
    page_icon="⚖️",
    layout="wide"
)
st.title("📚 Legal Document Analysis (RAG)")

st.markdown(
    "Ask legal questions based **strictly on uploaded legal documents** "
    "and receive **evidence-backed answers**."
)

uploaded_files = st.file_uploader(
    "📂 Upload Legal PDF(s)",
    type=["pdf"],
    accept_multiple_files=True
)

top_k = st.slider("Number of evidence chunks", 1, 10, 3)

query = st.text_area(
    "🔍 Enter your legal query",
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


if st.button("Analyze") and query.strip():

    if uploaded_files:
        with st.spinner("Processing uploaded documents..."):
            vectorstore = process_uploaded_pdfs(uploaded_files)
    else:
        vectorstore = None

    with st.spinner("Analyzing legal documents..."):
        response = handle_query(query, top_k, vectorstore)

    st.subheader("🧠 Legal Answer")
    st.markdown(
        f"<div style='background:#1F2937;padding:20px;border-radius:10px;color:white;"
        f"border-left:5px solid #22C55E;'>{response.answer}</div>",
        unsafe_allow_html=True
    )

    confidence = min(0.95, 0.5 + 0.1 * len(response.evidence))
    st.subheader("📊 Confidence")
    st.progress(confidence)

    st.subheader("📌 Evidence")
    for i, ev in enumerate(response.evidence, 1):
        with st.expander(f"Evidence {i} — {ev.source} (Page {ev.page_number})"):
            st.write(ev.content)
