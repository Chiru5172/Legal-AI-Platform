"""
chunker.py
-----------
Splits cleaned legal documents into overlapping chunks
while preserving page-level metadata for citation.
"""

from typing import List
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document


def chunk_documents(documents: List[Document]) -> List[Document]:
    """
    Splits legal documents into overlapping chunks.
    """

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        separators=["\n\n", "\n", ".", " "]
    )

    chunked_docs = []

    for doc in documents:
        chunks = splitter.split_text(doc.page_content)

        for i, chunk in enumerate(chunks):
            chunk_metadata = doc.metadata.copy()
            chunk_metadata["chunk_id"] = i

            chunked_docs.append(
                Document(
                    page_content=chunk,
                    metadata=chunk_metadata
                )
            )

    return chunked_docs
