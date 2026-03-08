"""
library_service.py
------------------
Service layer for accessing legal library data.
"""

from legal_library.law_data import LAW_SECTIONS


def get_all_categories():
    """Return all law categories."""
    return list(LAW_SECTIONS.keys())


def get_sections_by_category(category: str):
    """Return all section numbers under a category."""
    if category not in LAW_SECTIONS:
        return []
    return list(LAW_SECTIONS[category].keys())


def get_section_details(category: str, section: str):
    """Return details of a specific section."""
    return LAW_SECTIONS.get(category, {}).get(section, None)
