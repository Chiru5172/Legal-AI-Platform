"""
hallucination_check.py
----------------------
Checks whether generated answers are grounded
in retrieved legal evidence.
"""


def faithfulness_score(answer: str, evidence_texts: list) -> float:
    """
    Simple faithfulness check:
    - 1.0 = fully grounded
    - 0.5 = partially grounded
    - 0.0 = hallucinated
    """

    if not answer.strip():
        return 0.0

    grounded_sentences = 0
    total_sentences = 0

    sentences = [s.strip() for s in answer.split(".") if s.strip()]

    for sentence in sentences:
        total_sentences += 1
        if any(sentence.lower() in ev.lower() for ev in evidence_texts):
            grounded_sentences += 1

    if total_sentences == 0:
        return 0.0

    ratio = grounded_sentences / total_sentences

    if ratio > 0.8:
        return 1.0
    elif ratio > 0.4:
        return 0.5
    else:
        return 0.0


def citation_accuracy(evidence_list: list) -> float:
    """
    Checks if evidence contains valid source and page numbers.
    """

    if not evidence_list:
        return 0.0

    valid = 0
    for ev in evidence_list:
        if ev.source and ev.page_number is not None:
            valid += 1

    return valid / len(evidence_list)
