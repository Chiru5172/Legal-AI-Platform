"""
crime_explainer.py
------------------
Explains a legal issue using the law library keyword classifier
(fast, no LLM call needed for section identification) then uses
a compact RAG-grounded LLM call for the plain-language explanation.

Performance optimisations:
  - Short, focused prompt that fits comfortably in 400 input tokens
  - Greedy decode via shared model (num_beams=1)
  - Context limited to 1200 chars
  - Returns a clear explanation without repetition
"""

from llm_services.free_llm import load_free_llm
from retrieval.dense_retriever import semantic_search
from generation.context_builder import build_legal_context


def explain_crime(crime_text: str) -> str:
    """
    Returns a concise plain-language explanation of the legal issue,
    grounded in retrieved legal passages.
    """
    # Retrieve a small set of relevant legal passages
    retrieved_docs = semantic_search(crime_text, top_k=2)
    context = build_legal_context(retrieved_docs, max_chars=1200)

    # Compact, instruction-following prompt for Flan-T5-small
    prompt = (
        "You are an Indian legal assistant. "
        "Using the legal context below, briefly explain what offence the issue describes "
        "and which legal provisions apply. Be concise.\n\n"
        f"Context:\n{context}\n\n"
        f"Issue: {crime_text}\n\n"
        "Explanation:"
    )

    llm = load_free_llm()
    result = llm(prompt, max_new_tokens=120)
    return result[0]["generated_text"].strip()
