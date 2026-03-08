from typing import List
from langchain_core.documents import Document
from embeddings.vector_store import load_faiss_index


def semantic_search(query: str, top_k: int = 5, vectorstore=None) -> List[Document]:
    if vectorstore is None:
        vectorstore = load_faiss_index()

    return vectorstore.similarity_search(query, k=top_k)
