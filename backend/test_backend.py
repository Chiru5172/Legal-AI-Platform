import sys
import os

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(PROJECT_ROOT)

from backend.api import handle_query

response = handle_query(
    query="What human rights violations by police are discussed?",
    top_k=3
)

print("ANSWER:")
print(response.answer)

print("\nEVIDENCE:")
for ev in response.evidence:
    print(ev.source, ev.page_number)
