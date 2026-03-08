"""
letter_generator.py
-------------------
Generates a professional complaint body suitable for submission
to an Indian police station.
"""

from llm_services.free_llm import load_free_llm
from legal_library.section_classifier import find_relevant_sections
from legal_library.library_service import get_section_details


def build_sections_context(incident_text: str):
    """
    Retrieve relevant legal sections and convert them to readable context.
    """

    matched_sections = find_relevant_sections(incident_text)

    context = ""

    for category, section in matched_sections:
        details = get_section_details(category, section)

        if details:
            context += f"""
Section: {section}
Title: {details.get("title","")}
Description: {details.get("description","")}
Punishment: {details.get("punishment","")}
"""

    return context


def remove_repetitions(text: str):
    """
    Remove repeated sentences produced by small LLMs.
    """

    sentences = text.split(".")
    seen = set()
    cleaned = []

    for s in sentences:
        sentence = s.strip()

        if not sentence:
            continue

        if sentence.lower() not in seen:
            cleaned.append(sentence)
            seen.add(sentence.lower())

    return ". ".join(cleaned) + "."


def generate_complaint_body(incident_text: str):
    """
    Generate complaint body with strong prompt constraints.
    """

    llm = load_free_llm()

    sections_context = build_sections_context(incident_text)

    prompt = f"""
You are a legal drafting assistant in India.

Write the BODY of a police complaint letter.

Important rules:
- Write exactly 2 or 3 paragraphs.
- Use professional language suitable for an Indian police complaint.
- Clearly explain the incident.
- Mention legal implications where relevant.
- Do NOT repeat sentences.
- Do NOT include greeting lines or closing lines.

Incident Details:
{incident_text}

Relevant Legal Context:
{sections_context}

Write a clear and professional complaint explanation.
"""

    response = llm(prompt)[0]["generated_text"]

    cleaned_text = remove_repetitions(response.strip())

    return cleaned_text
