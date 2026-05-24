"""
letter_generator.py
-------------------
Generates the body of a formal Indian police complaint letter.

Approach:
  - The incident description IS the complaint body — it is included verbatim
    as the core factual narration (first-person, clear, factual).
  - The LLM generates ONE short sentence: a legal characterisation of the issue.
  - Identified legal sections are appended as a compact reference list.
  - This is fast (tiny LLM call), accurate (incident verbatim), and
    structurally correct per Indian police complaint standards.
"""

from llm_services.free_llm import load_free_llm
from legal_library.section_classifier import find_relevant_sections
from legal_library.library_service import get_section_details


def get_applicable_sections_text(incident_text: str) -> tuple[str, list]:
    """
    Returns:
      - A formatted string listing applicable sections (for the letter)
      - The raw list of (category, section) tuples
    """
    matched = find_relevant_sections(incident_text)
    lines = []
    for category, section in matched[:5]:   # cap at 5 sections in the letter
        details = get_section_details(category, section)
        if details:
            lines.append(f"{section} – {details.get('title', '')}")
    section_text = ", ".join(lines) if lines else "relevant provisions of law"
    return section_text, matched


def generate_legal_characterisation(incident_text: str, sections_text: str) -> str:
    """
    Use the LLM to generate ONE concise sentence characterising the legal nature
    of the incident. This is the only LLM call — keeps it fast and focused.
    """
    llm = load_free_llm()

    prompt = (
        "Summarise in one sentence the legal nature of this incident "
        "and which laws are violated. Be brief and formal.\n\n"
        f"Incident: {incident_text[:300]}\n"
        f"Applicable laws: {sections_text[:200]}\n\n"
        "Legal summary:"
    )

    result = llm(prompt, max_new_tokens=80)
    text = result[0]["generated_text"].strip()

    # Fallback if model returns empty or too short
    if len(text) < 15:
        text = (
            f"The aforesaid acts constitute offences punishable under {sections_text} "
            "and other applicable provisions of law."
        )
    return text


def generate_complaint_body(incident_text: str) -> str:
    """
    Compose the complaint letter body paragraphs.

    Structure (per Indian police complaint convention):
      Para 1 — First-person factual narration of the incident (verbatim from user)
      Para 2 — Legal characterisation + list of applicable sections
      Para 3 — Prayer / request for action
    """
    sections_text, matched_sections = get_applicable_sections_text(incident_text)
    legal_summary = generate_legal_characterisation(incident_text, sections_text)

    # Build section reference block
    section_lines = []
    for category, section in matched_sections[:5]:
        details = get_section_details(category, section)
        if details:
            section_lines.append(
                f"  • {section} – {details.get('title', '')} "
                f"(Punishment: {details.get('punishment', 'as per law')})"
            )
    section_block = "\n".join(section_lines) if section_lines else (
        "  • Relevant provisions of Indian law as applicable"
    )

    body = (
        f"I most respectfully submit that {incident_text.strip()}\n\n"
        f"{legal_summary}\n\n"
        f"The acts of the accused are cognizable and punishable under the following provisions:\n"
        f"{section_block}\n\n"
        f"I therefore humbly request you to kindly register my complaint, "
        f"take cognizance of the offences, investigate the matter thoroughly, "
        f"and initiate appropriate legal action against the accused as per law."
    )

    return body
