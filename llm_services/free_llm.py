"""
free_llm.py
-----------
Loads a FREE, offline instruction-tuned LLM.
"""

import streamlit as st
from transformers import pipeline


@st.cache_resource
def load_free_llm():
    """
    Loads flan-t5-large for instruction following.
    Cached to avoid reloading on every run.
    """
    return pipeline(
        "text2text-generation",
        model="google/flan-t5-large",
        max_length=512
    )
