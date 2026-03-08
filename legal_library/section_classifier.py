"""
section_classifier.py
---------------------
Maps crime description to relevant legal sections
using keyword matching over legal library.
"""

from legal_library.law_data import LAW_SECTIONS


KEYWORD_SECTION_MAP = {
    "cheat": ["IPC 420"],
    "fraud": ["IPC 420"],
    "theft": ["IPC 379"],
    "steal": ["IPC 379"],
    "rape": ["IPC 376"],
    "harass": ["IPC 354", "IPC 498A"],
    "dowry": ["IPC 498A"],
    "murder": ["IPC 302"],
    "kill": ["IPC 302"],
    "threat": ["IPC 506"],
    "hack": ["IT Act 66"],
    "identity": ["IT Act 66C"],
    "online": ["IT Act 66D"],
    "arrest": ["CrPC 41", "CrPC 50"],
    "fir": ["CrPC 154"],
    "custody": ["CrPC 167"],
    "speech": ["Article 19"],
    "equality": ["Article 14"]
}


def find_relevant_sections(crime_text: str):
    crime_text = crime_text.lower()
    matched_sections = []

    for keyword, sections in KEYWORD_SECTION_MAP.items():
        if keyword in crime_text:
            matched_sections.extend(sections)

    # Deduplicate
    matched_sections = list(set(matched_sections))

    # Validate against law library
    verified = []
    for category, laws in LAW_SECTIONS.items():
        for section in laws:
            if section in matched_sections:
                verified.append((category, section))

    return verified
