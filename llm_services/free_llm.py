"""
free_llm.py
-----------
Loads a FREE, offline instruction-tuned LLM.
"""

import streamlit as st
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM,pipeline


@st.cache_resource

def load_free_llm():

    model_name = "google/flan-t5-large"

    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

    pipe = pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
        max_length=512,
        temperature=0.2
    )

    return pipe