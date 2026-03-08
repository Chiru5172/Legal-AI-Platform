import sys
import os

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(PROJECT_ROOT)

from generation.rag_chain import run_legal_rag

query = "What are the human rights violations by police mentioned in the documents?"

result = run_legal_rag(query, top_k=3)

print("QUESTION:")
print(result["question"])
print("\nANSWER:")
print(result["answer"])

print("\nEVIDENCE:")
for doc in result["source_documents"]:
    print(
        f"- Source: {doc.metadata.get('source')}, "
        f"Page: {doc.metadata.get('page_number')}"
    )
