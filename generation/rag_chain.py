"""
rag_chain.py
------------
Retrieval-Augmented Generation for legal queries.
Uses the shared model from free_llm.py so only ONE model
instance is ever loaded — saving memory and load time.

Performance optimisations:
  - Shared model (no duplicate loading)
  - Greedy decoding (num_beams=1) — 4x faster on CPU
  - Input capped at 400 tokens, output at 128 tokens
  - Context limited to 1500 chars (fits cleanly in 400 tokens)
"""

from typing import Dict, Any
import streamlit as st

from retrieval.dense_retriever import semantic_search
from generation.context_builder import build_legal_context
from generation.prompt_templates import LEGAL_RAG_PROMPT


def generate_answer(prompt: str, max_new_tokens: int = 128) -> str:
    """
    Run seq2seq inference using the shared cached Flan-T5 model.
    Importing here (lazy) avoids circular imports while still
    using the single shared @st.cache_resource instance.
    """
    from llm_services.free_llm import get_shared_model
    tokenizer, model = get_shared_model()

    inputs = tokenizer(
        prompt,
        return_tensors="pt",
        max_length=400,       # tight cap — leaves room for output tokens
        truncation=True
    )

    outputs = model.generate(
        **inputs,
        max_new_tokens=max_new_tokens,
        num_beams=1,          # greedy decode — 4x faster than beam=4 on CPU
        early_stopping=False,
        no_repeat_ngram_size=3,
        do_sample=False,
    )

    answer = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return answer.strip()


def run_legal_rag(
    question: str,
    top_k: int = 3,
    vectorstore=None
) -> Dict[str, Any]:
    """
    Executes Retrieval-Augmented Generation for legal queries.
    top_k reduced to 3 (from 5) to keep context tight and fast.
    """

    # ----------------------------
    # RETRIEVAL
    # ----------------------------
    retrieved_docs = semantic_search(
        question,
        top_k=top_k,
        vectorstore=vectorstore
    )

    # ----------------------------
    # CONTEXT BUILDING (tight limit)
    # ----------------------------
    context = build_legal_context(retrieved_docs, max_chars=1500)

    # ----------------------------
    # GENERATION
    # ----------------------------
    prompt = LEGAL_RAG_PROMPT.format(
        context=context,
        question=question
    )

    answer = generate_answer(prompt)

    return {
        "question": question,
        "answer": answer,
        "source_documents": retrieved_docs
    }
