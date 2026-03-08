"""
app.py
------
Main entry point for the Legal AI Platform (Multi-page App).
"""

import streamlit as st

st.markdown(
    """
    <div style="
        background: linear-gradient(135deg, #020617, #020617);
        padding: 40px;
        border-radius: 16px;
        margin-bottom: 30px;
    ">
        <h1 style="color:#FFFFFF;">⚖️ Legal AI Platform</h1>
        <p style="color:#CBD5E1; font-size:18px;">
            An AI-powered system for legal research, advice, and complaint drafting
        </p>
    </div>
    """,
    unsafe_allow_html=True
)


st.set_page_config(
    page_title="Legal AI Platform",
    page_icon="⚖️",
    layout="wide"
)

st.markdown("""
<style>
.stApp {
    background-color: #0E1117;
    color: #E5E7EB;
}
</style>
""", unsafe_allow_html=True)

# st.title("⚖️ Legal AI Platform")

st.markdown("## 🚀 Platform Capabilities")

col1, col2 = st.columns(2)

with col1:
    st.markdown(
        """
        <div style="background:#020617; padding:20px; border-radius:12px;">
            <h4>📄 Legal Document Analysis</h4>
            <p>Upload legal PDFs and query them using Retrieval-Augmented Generation (RAG).</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div style="background:#020617; padding:20px; border-radius:12px; margin-top:15px;">
            <h4>🧠 Evidence-backed Research</h4>
            <p>All answers are grounded in legal documents with citations.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        """
        <div style="background:#020617; padding:20px; border-radius:12px;">
            <h4>📚 Law Explorer</h4>
            <p>Explore criminal, civil, cyber, and constitutional law sections.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div style="background:#020617; padding:20px; border-radius:12px; margin-top:15px;">
            <h4>📝 Complaint Drafting</h4>
            <p>Generate professionally formatted, submission-ready complaint letters.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("## ⚡ Quick Actions")

col1, col2, col3 = st.columns(3)

def quick_action_card(title, description, page):
    st.markdown(
        f"""
        <a href="/{page}" style="text-decoration:none;">
            <div style="
                background:#020617;
                padding:20px;
                border-radius:14px;
                border:1px solid #1E293B;
                color:#FFFFFF;
                transition:0.3s;
            ">
                <h4 style="color:#E5E7EB;">{title}</h4>
                <p style="color:#94A3B8;">{description}</p>
            </div>
        </a>
        """,
        unsafe_allow_html=True
    )

with col1:
    quick_action_card(
        "🔍 Legal Research",
        "Ask questions over uploaded legal documents",
        "Home_RAG"
    )

with col2:
    quick_action_card(
        "⚖️ Law Explorer",
        "Understand crimes and applicable sections",
        "Legal_Advice"
    )

with col3:
    quick_action_card(
        "📝 Draft Complaint",
        "Generate submission-ready complaint letters",
        "Complaint_Generator"
    )



st.markdown(
    """
    <div style="
        background:#020617;
        padding:16px;
        border-radius:10px;
        border-left:6px solid #FACC15;
        margin-top:30px;
    ">
        ⚠️ <b>Disclaimer:</b> This platform provides legal information and drafting assistance only.
        It is not a substitute for professional legal advice.
    </div>
    """,
    unsafe_allow_html=True
)

