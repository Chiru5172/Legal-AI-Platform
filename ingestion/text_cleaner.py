"""
text_cleaner.py
----------------
Cleans legal text while preserving:
- Legal citations
- Section references
- Case names

Removes:
- Extra whitespace
- Page headers/footers
- Formatting noise
"""

import re
from typing import List
from langchain_core.documents import Document


def clean_legal_text(text: str) -> str:
    """
    Cleans raw legal text extracted from PDFs.
    """

    # Remove multiple newlines
    text = re.sub(r"\n{2,}", "\n", text)

    # Remove extra spaces
    text = re.sub(r"[ \t]{2,}", " ", text)

    # Remove page numbers like "Page 1 of 23"
    text = re.sub(r"Page\s+\d+\s+of\s+\d+", "", text, flags=re.IGNORECASE)

    # Remove common header/footer patterns
    text = re.sub(r"SUPREME COURT OF INDIA", "", text, flags=re.IGNORECASE)
    text = re.sub(r"HIGH COURT OF .*", "", text, flags=re.IGNORECASE)

    # Remove non-informative separators
    text = re.sub(r"[-_]{5,}", "", text)

    return text.strip()


def clean_documents(documents: List[Document]) -> List[Document]:
    """
    Applies legal text cleaning to all documents.
    """
    cleaned_docs = []

    for doc in documents:
        cleaned_text = clean_legal_text(doc.page_content)

        cleaned_doc = Document(
            page_content=cleaned_text,
            metadata=doc.metadata
        )

        cleaned_docs.append(cleaned_doc)

    return cleaned_docs
