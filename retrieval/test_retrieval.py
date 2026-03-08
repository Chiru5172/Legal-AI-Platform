import sys
import os

# Add project root to path
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(PROJECT_ROOT)

from retrieval.dense_retriever import semantic_search

query = "violation of human rights by police"

results = semantic_search(query, top_k=3)

print(f"Retrieved {len(results)} documents:\n")

for i, doc in enumerate(results, 1):
    print(f"--- Result {i} ---")
    print("Source:", doc.metadata.get("source"))
    print("Page:", doc.metadata.get("page_number"))
    print(doc.page_content[:500])
    print()
