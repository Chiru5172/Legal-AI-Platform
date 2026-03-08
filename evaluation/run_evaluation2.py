"""
run_evaluation.py
-----------------
Runs evaluation for the Legal RAG system.
"""

import os
import sys

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(PROJECT_ROOT)

from evaluation.test_data import TEST_CASES
from evaluation.metrics_2 import precision_recall_f1
from legal_library.section_classifier import find_relevant_sections


def evaluate_system():
    print("\n===== LEGAL RAG SYSTEM EVALUATION =====\n")

    total_precision = 0
    total_recall = 0
    total_f1 = 0

    for idx, case in enumerate(TEST_CASES, start=1):
        question = case["question"]
        expected = case["expected_sections"]

        matched = find_relevant_sections(question)
        retrieved_sections = [sec for _, sec in matched]

        precision, recall, f1 = precision_recall_f1(retrieved_sections, expected)

        total_precision += precision
        total_recall += recall
        total_f1 += f1

        print(f"Test Case {idx}")
        print(f"Question: {question}")
        print(f"Expected Sections: {expected}")
        print(f"Retrieved Sections: {retrieved_sections}")
        print(f"Precision: {precision:.2f}")
        print(f"Recall: {recall:.2f}")
        print(f"F1 Score: {f1:.2f}")
        print("-" * 50)

    n = len(TEST_CASES)
    print("\n===== OVERALL METRICS =====")
    print(f"Average Precision: {total_precision / n:.2f}")
    print(f"Average Recall: {total_recall / n:.2f}")
    print(f"Average F1 Score: {total_f1 / n:.2f}")


if __name__ == "__main__":
    evaluate_system()
