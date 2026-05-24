"""
free_llm.py
-----------
Shared Flan-T5 model loader for all LLM services.
Uses a SINGLE shared cache key so rag_chain.py and
llm_services modules share the same model instance.

Performance optimizations:
  - num_beams=1 (greedy decode) — 4x faster than beam=4 on CPU
  - max_new_tokens=128 — sufficient for Flan-T5-small answers
  - Prompt capped at 400 tokens to leave room for output tokens
"""

import streamlit as st


@st.cache_resource(show_spinner="Loading AI model (first time only)...")
def _load_shared_model():
    """
    Load Flan-T5-small once and cache for the entire Streamlit session.
    This single resource is shared across rag_chain.py and all llm_services.
    """
    from transformers import AutoTokenizer, T5ForConditionalGeneration
    model_name = "google/flan-t5-small"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = T5ForConditionalGeneration.from_pretrained(model_name)
    model.eval()          # disable dropout for faster inference
    return tokenizer, model


def load_free_llm():
    """
    Returns a callable that mimics the pipeline interface:
        llm(prompt) -> [{"generated_text": str}]
    """
    tokenizer, model = _load_shared_model()

    def _infer(prompt: str, max_new_tokens: int = 128):
        inputs = tokenizer(
            prompt,
            return_tensors="pt",
            max_length=400,       # cap input; leaves headroom for output tokens
            truncation=True
        )
        outputs = model.generate(
            **inputs,
            max_new_tokens=max_new_tokens,
            num_beams=1,          # greedy — 4x faster than beam=4 on CPU
            early_stopping=False,
            no_repeat_ngram_size=3,
            do_sample=False,
        )
        text = tokenizer.decode(outputs[0], skip_special_tokens=True)
        return [{"generated_text": text.strip()}]

    return _infer


def get_shared_model():
    """
    Direct access to (tokenizer, model) — used by rag_chain.py
    so both code paths share the exact same cached instance.
    """
    return _load_shared_model()