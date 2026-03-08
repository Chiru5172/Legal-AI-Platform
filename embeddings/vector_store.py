"""
vector_store.py
----------------
Builds and manages the FAISS vector database
for legal document embeddings.
"""

import os
from typing import List
from langchain_core.documents import Document
from langchain_community.vectorstores import FAISS

from embeddings.embedding_model import get_embedding_model

FAISS_INDEX_PATH = "data/faiss_index"


def build_faiss_index(documents: List[Document]) -> FAISS:
    """
    Creates a FAISS vector store from legal document chunks.
    """

    embedding_model = get_embedding_model()

    vectorstore = FAISS.from_documents(
        documents=documents,
        embedding=embedding_model
    )

    return vectorstore


def save_faiss_index(vectorstore: FAISS):
    """
    Saves FAISS index to disk.
    """
    vectorstore.save_local(FAISS_INDEX_PATH)


def load_faiss_index() -> FAISS:
    """
    Loads FAISS index from disk.
    """
    embedding_model = get_embedding_model()

    if not os.path.exists(FAISS_INDEX_PATH):
        raise FileNotFoundError("FAISS index not found. Build it first.")

    return FAISS.load_local(
        FAISS_INDEX_PATH,
        embedding_model,
        allow_dangerous_deserialization=True
    )
