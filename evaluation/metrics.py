"""
metrics.py
----------
Implements evaluation metrics for the Legal RAG system.
"""


def precision_at_k(relevant_docs, retrieved_docs):
    if not retrieved_docs:
        return 0.0
    return len(set(relevant_docs) & set(retrieved_docs)) / len(retrieved_docs)


def recall_at_k(relevant_docs, retrieved_docs):
    if not relevant_docs:
        return 0.0
    return len(set(relevant_docs) & set(retrieved_docs)) / len(relevant_docs)


def f1_score(precision, recall):
    """
    F1 = 2 * (P * R) / (P + R)
    """
    if precision + recall == 0:
        return 0.0
    return 2 * (precision * recall) / (precision + recall)


def answer_accuracy(retrieved_docs, relevant_docs, faithfulness):
    """
    Defines end-to-end model accuracy for RAG:
    - Correct (1) if:
        - At least one relevant document retrieved
        - Faithfulness >= 0.5
    - Else Incorrect (0)
    """
    correct_retrieval = len(set(retrieved_docs) & set(relevant_docs)) > 0
    faithful_answer = faithfulness >= 0.5

    return 1 if (correct_retrieval and faithful_answer) else 0
