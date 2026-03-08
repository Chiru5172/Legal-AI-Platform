import sys
import os

# Add project root to Python path
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(PROJECT_ROOT)

from ingestion.pdf_loader import load_legal_pdfs
from ingestion.text_cleaner import clean_documents
from ingestion.chunker import chunk_documents
from embeddings.vector_store import build_faiss_index, save_faiss_index

# Pipeline
docs = load_legal_pdfs()
cleaned_docs = clean_documents(docs)
chunks = chunk_documents(cleaned_docs)

print("Total chunks:", len(chunks))

# Build FAISS
vectorstore = build_faiss_index(chunks)
save_faiss_index(vectorstore)

print("FAISS index built and saved successfully.")
