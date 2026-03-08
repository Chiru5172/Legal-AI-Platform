"""
context_builder.py
------------------
Builds a structured legal context from retrieved documents
to be passed safely to the LLM in a RAG pipeline.
"""

from typing import List
from langchain_core.documents import Document


def build_legal_context(
    documents: List[Document],
    max_chars: int = 4000
) -> str:
    """
    Combines retrieved legal document chunks into a single context string
    with source and page number citations.
    """

    context_blocks = []
    current_length = 0

    for idx, doc in enumerate(documents, start=1):
        source = doc.metadata.get("source", "Unknown Source")
        page = doc.metadata.get("page_number", "N/A")

        block = (
            f"[Evidence {idx}]\n"
            f"Source: {source}\n"
            f"Page: {page}\n"
            f"Text:\n{doc.page_content}\n"
        )

        if current_length + len(block) > max_chars:
            break

        context_blocks.append(block)
        current_length += len(block)

    return "\n\n".join(context_blocks)
