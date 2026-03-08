# ingestion/test_cleaner.py
from pdf_loader import load_legal_pdfs
from text_cleaner import clean_documents

docs = load_legal_pdfs()
cleaned_docs = clean_documents(docs)

print(cleaned_docs[0].page_content[:500])
print(cleaned_docs[0].metadata)
