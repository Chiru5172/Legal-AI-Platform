"""
pdf_loader.py
----------------
Loads legal PDF documents page-by-page while preserving:
- Source file name
- Page number
- Raw text content
"""

import os
from typing import List
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document

RAW_PDF_DIR = "data/raw_pdfs"


def load_legal_pdfs() -> List[Document]:
    return load_legal_pdfs_from_path(RAW_PDF_DIR)


def load_legal_pdfs_from_path(directory_path: str) -> List[Document]:
    documents = []

    for file_name in os.listdir(directory_path):
        if file_name.lower().endswith(".pdf"):
            file_path = os.path.join(directory_path, file_name)
            loader = PyPDFLoader(file_path)
            pages = loader.load()

            for page in pages:
                page.metadata["source"] = file_name
                page.metadata["page_number"] = page.metadata.get("page", "N/A")
                documents.append(page)

    return documents
