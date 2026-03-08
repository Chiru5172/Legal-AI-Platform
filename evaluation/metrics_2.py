"""
metrics.py
----------
Evaluation metrics for RAG-based legal system.
"""

def precision_recall_f1(retrieved, expected):
    retrieved = set(retrieved)
    expected = set(expected)

    true_positive = len(retrieved & expected)
    false_positive = len(retrieved - expected)
    false_negative = len(expected - retrieved)

    precision = true_positive / (true_positive + false_positive) if (true_positive + false_positive) else 0
    recall = true_positive / (true_positive + false_negative) if (true_positive + false_negative) else 0
    f1 = (
        2 * precision * recall / (precision + recall)
        if (precision + recall)
        else 0
    )

    return precision, recall, f1
