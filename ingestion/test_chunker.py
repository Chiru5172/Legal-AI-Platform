# ingestion/test_chunker.py
from pdf_loader import load_legal_pdfs
from text_cleaner import clean_documents
from chunker import chunk_documents

docs = load_legal_pdfs()
cleaned_docs = clean_documents(docs)
chunks = chunk_documents(cleaned_docs)

print("Total chunks:", len(chunks))
print(chunks[0].page_content[:500])
print(chunks[0].metadata)
