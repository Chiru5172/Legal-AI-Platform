import sys
import os

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(PROJECT_ROOT)

from retrieval.dense_retriever import semantic_search
from generation.context_builder import build_legal_context

query = "violation of human rights by police"

docs = semantic_search(query, top_k=3)
context = build_legal_context(docs)

print(context)
