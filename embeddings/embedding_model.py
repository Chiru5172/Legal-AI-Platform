"""
embedding_model.py
------------------
Provides a free, local embedding model using HuggingFace
(sentence-transformers), following latest LangChain standards.
"""

from langchain_huggingface import HuggingFaceEmbeddings


def get_embedding_model():
    """
    Returns a HuggingFace embedding model instance.
    """
    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
