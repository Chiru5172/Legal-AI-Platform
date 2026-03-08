"""
run_evaluation.py
-----------------
Runs end-to-end evaluation of the Legal RAG system
and prints all metrics including F1-score and Accuracy.
"""

import sys
import os

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(PROJECT_ROOT)

from backend.api import handle_query
from evaluation.metrics import (
    precision_at_k,
    recall_at_k,
    f1_score,
    answer_accuracy
)
from evaluation.hallucination_check import (
    faithfulness_score,
    citation_accuracy
)


# -----------------------------
# TEST QUERIES (GOLD STANDARD)
# -----------------------------
evaluation_dataset = [
    {
        "query": "What rights of arrested persons are discussed?",
        "relevant_sources": [
            "1619069016Human Rights Judgments on Human Rights and Policing in India.pdf"
        ]
    },
    {
        "query": "What are the powers of police in evidence collection?",
        "relevant_sources": [
            "1619069016Human Rights Judgments on Human Rights and Policing in India.pdf"
        ]
    }
]

TOP_K = 3

precision_scores = []
recall_scores = []
f1_scores = []
faithfulness_scores = []
citation_scores = []
accuracy_scores = []

print("\n===== LEGAL RAG SYSTEM EVALUATION =====\n")

for idx, sample in enumerate(evaluation_dataset, start=1):
    print(f"🔍 Query {idx}: {sample['query']}")

    response = handle_query(
        query=sample["query"],
        top_k=TOP_K,
        vectorstore=None
    )

    retrieved_sources = [ev.source for ev in response.evidence]

    precision = precision_at_k(
        sample["relevant_sources"],
        retrieved_sources
    )

    recall = recall_at_k(
        sample["relevant_sources"],
        retrieved_sources
    )

    f1 = f1_score(precision, recall)

    evidence_texts = [ev.content for ev in response.evidence]
    faithfulness = faithfulness_score(response.answer, evidence_texts)

    citation = citation_accuracy(response.evidence)

    accuracy = answer_accuracy(
        retrieved_sources,
        sample["relevant_sources"],
        faithfulness
    )

    precision_scores.append(precision)
    recall_scores.append(recall)
    f1_scores.append(f1)
    faithfulness_scores.append(faithfulness)
    citation_scores.append(citation)
    accuracy_scores.append(accuracy)

    print(f"   Precision@{TOP_K}: {precision:.2f}")
    print(f"   Recall@{TOP_K}:    {recall:.2f}")
    print(f"   F1-Score:          {f1:.2f}")
    print(f"   Faithfulness:      {faithfulness:.2f}")
    print(f"   Citation Accuracy: {citation:.2f}")
    print(f"   Answer Accuracy:   {accuracy}\n")


# -----------------------------
# FINAL AVERAGES
# -----------------------------
print("===== FINAL EVALUATION RESULTS =====\n")

print(f"📌 Average Precision@{TOP_K}: {sum(precision_scores)/len(precision_scores):.2f}")
print(f"📌 Average Recall@{TOP_K}:    {sum(recall_scores)/len(recall_scores):.2f}")
print(f"📌 Average F1-Score:          {sum(f1_scores)/len(f1_scores):.2f}")
print(f"📌 Faithfulness Score:        {sum(faithfulness_scores)/len(faithfulness_scores):.2f}")
print(f"📌 Citation Accuracy:         {sum(citation_scores)/len(citation_scores):.2f}")
print(f"📌 Model Accuracy:            {sum(accuracy_scores)/len(accuracy_scores):.2f}")

print("\n✅ Evaluation completed successfully.\n")
