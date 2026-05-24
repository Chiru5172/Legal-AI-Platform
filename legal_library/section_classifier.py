"""
section_classifier.py
---------------------
Maps crime/legal issue description to relevant legal sections
using comprehensive keyword matching over the full legal library,
with a fuzzy word-overlap fallback so ALL sections in law_data.py
are reachable.
"""

from legal_library.law_data import LAW_SECTIONS


# =====================================================================
# COMPREHENSIVE KEYWORD → SECTION MAP
# Covers every section in law_data.py (60+ sections across 10 categories)
# =====================================================================
KEYWORD_SECTION_MAP = {

    # ── Constitution of India ────────────────────────────────────────
    "state authority":          ["Article 12"],
    "government action":        ["Article 12"],
    "equal":                    ["Article 14"],
    "equality":                 ["Article 14"],
    "discriminat":              ["Article 15"],
    "caste":                    ["Article 15"],
    "religion":                 ["Article 15"],
    "sex":                      ["Article 15"],
    "speech":                   ["Article 19"],
    "expression":               ["Article 19"],
    "assembly":                 ["Article 19"],
    "freedom":                  ["Article 19"],
    "press":                    ["Article 19"],
    "retrospective":            ["Article 20"],
    "double jeopardy":          ["Article 20"],
    "self-incrimination":       ["Article 20"],
    "incrimination":            ["Article 20"],
    "life":                     ["Article 21"],
    "liberty":                  ["Article 21"],
    "privacy":                  ["Article 21", "IT Act 66E"],
    "personal liberty":         ["Article 21"],
    "right to life":            ["Article 21"],
    "arrest":                   ["Article 22", "CrPC 41", "CrPC 50"],
    "detain":                   ["Article 22", "CrPC 167"],
    "detention":                ["Article 22", "CrPC 167"],
    "writ":                     ["Article 32"],
    "habeas corpus":            ["Article 32"],
    "fundamental right":        ["Article 32", "Article 21"],
    "supreme court":            ["Article 32"],

    # ── Indian Penal Code (IPC) – Homicide ──────────────────────────
    "murder":                   ["IPC 302", "IPC 300"],
    "kill":                     ["IPC 302", "IPC 300"],
    "killed":                   ["IPC 302", "IPC 300"],
    "homicide":                 ["IPC 299", "IPC 304"],
    "culpable":                 ["IPC 299", "IPC 304"],
    "attempt to murder":        ["IPC 307"],
    "attempt murder":           ["IPC 307"],
    "tried to kill":            ["IPC 307"],
    "attempted to kill":        ["IPC 307"],
    "miscarriage":              ["IPC 312"],

    # ── IPC – Hurt ───────────────────────────────────────────────────
    "hurt":                     ["IPC 323", "IPC 325"],
    "assault":                  ["IPC 323", "IPC 325"],
    "beat":                     ["IPC 323"],
    "beaten":                   ["IPC 323"],
    "beating":                  ["IPC 323"],
    "hit":                      ["IPC 323"],
    "attack":                   ["IPC 323"],
    "attacked":                 ["IPC 323"],
    "punch":                    ["IPC 323"],
    "grievous":                 ["IPC 325"],
    "severe injury":            ["IPC 325"],
    "serious injury":           ["IPC 325"],
    "bodily harm":              ["IPC 325"],
    "broken":                   ["IPC 325"],
    "fracture":                 ["IPC 325"],

    # ── IPC – Sexual Offences ────────────────────────────────────────
    "rape":                     ["IPC 376", "IPC 375"],
    "sexual assault":           ["IPC 376", "IPC 375A/376A (Amendments)"],
    "sexual abuse":             ["IPC 376"],
    "sexually abused":          ["IPC 376"],
    "molestation":              ["IPC 376"],
    "molested":                 ["IPC 376"],
    "aggravated sexual":        ["IPC 375A/376A (Amendments)"],
    "gang rape":                ["IPC 375A/376A (Amendments)"],
    "unnatural":                ["IPC 377"],

    # ── IPC – Property & Fraud ───────────────────────────────────────
    "theft":                    ["IPC 379"],
    "steal":                    ["IPC 379"],
    "stolen":                   ["IPC 379"],
    "stole":                    ["IPC 379"],
    "rob":                      ["IPC 379"],
    "robbery":                  ["IPC 379"],
    "misappropriat":            ["IPC 404"],
    "trust":                    ["IPC 406"],
    "entrut":                   ["IPC 406"],
    "breach of trust":          ["IPC 406"],
    "cheat":                    ["IPC 420"],
    "cheating":                 ["IPC 420"],
    "fraud":                    ["IPC 420"],
    "deceiv":                   ["IPC 420"],
    "deception":                ["IPC 420"],
    "scam":                     ["IPC 420"],
    "swindl":                   ["IPC 420"],
    "fake":                     ["IPC 420", "IT Act 66D"],
    "forged":                   ["IPC 420"],
    "forgery":                  ["IPC 420"],
    "money collected":          ["IPC 420"],
    "inducement":               ["IPC 420"],

    # ── IPC – Threats & Intimidation ────────────────────────────────
    "threat":                   ["IPC 503", "IPC 506", "IPC 506/507"],
    "threaten":                 ["IPC 503", "IPC 506"],
    "intimidat":                ["IPC 503", "IPC 506"],
    "blackmail":                ["IPC 503", "IPC 506"],
    "extort":                   ["IPC 503", "IPC 506"],
    "anonymous threat":         ["IPC 506/507"],
    "threatening message":      ["IPC 506"],
    "threatening call":         ["IPC 506"],

    # ── IPC – Public Order & State ───────────────────────────────────
    "waging war":               ["IPC 121"],
    "terror":                   ["IPC 121", "IT Act 66F"],
    "sedition":                 ["IPC 124A"],
    "disaffection":             ["IPC 124A"],
    "incite":                   ["IPC 124A"],

    # ── IPC – Domestic & Family ──────────────────────────────────────
    "harass":                   ["IPC 498A"],
    "harassment":               ["IPC 498A"],
    "domestic":                 ["IPC 498A"],
    "dowry":                    ["IPC 498B (Dowry Prohibition Act related)", "IPC 498A"],
    "cruelty":                  ["IPC 498A"],
    "husband":                  ["IPC 498A"],
    "wife":                     ["IPC 498A"],
    "marital":                  ["IPC 498A"],
    "matrimonial":              ["IPC 498A"],
    "maintenance":              ["Maintenance & Welfare (Maintenance Act provisions)"],
    "alimony":                  ["Maintenance & Welfare (Maintenance Act provisions)"],

    # ── CrPC – Procedural ────────────────────────────────────────────
    "fir":                      ["CrPC 154"],
    "first information report": ["CrPC 154"],
    "register complaint":       ["CrPC 154"],
    "police report":            ["CrPC 154"],
    "cognizable":               ["CrPC 154", "CrPC 2"],
    "remand":                   ["CrPC 167"],
    "custody":                  ["CrPC 167"],
    "investigation":            ["CrPC 167"],
    "produce before magistrate":["CrPC 56-60"],
    "magistrate":               ["CrPC 56-60", "CrPC 167"],
    "prosecut":                 ["CrPC 197"],
    "sanction":                 ["CrPC 197"],
    "public servant":           ["CrPC 197"],
    "police officer":           ["CrPC 41"],
    "without warrant":          ["CrPC 41"],
    "grounds of arrest":        ["CrPC 50"],
    "right to bail":            ["CrPC 50"],

    # ── IT Act – Cyber ───────────────────────────────────────────────
    "hack":                     ["IT Act 66"],
    "hacked":                   ["IT Act 66"],
    "hacking":                  ["IT Act 66"],
    "unauthorized access":      ["IT Act 66"],
    "computer":                 ["IT Act 43", "IT Act 66"],
    "cyber":                    ["IT Act 66", "IT Act 66F"],
    "damage to computer":       ["IT Act 43"],
    "data breach":              ["IT Act 43", "IT Act 66"],
    "identity theft":           ["IT Act 66C"],
    "identity":                 ["IT Act 66C"],
    "credential":               ["IT Act 66C"],
    "password":                 ["IT Act 66C"],
    "impersonat":               ["IT Act 66D"],
    "fake account":             ["IT Act 66D"],
    "fake profile":             ["IT Act 66D"],
    "posing as":                ["IT Act 66D"],
    "instagram":                ["IT Act 66D", "IPC 420"],
    "social media":             ["IT Act 66D"],
    "online":                   ["IT Act 66D"],
    "voyeur":                   ["IT Act 66E"],
    "intimate image":           ["IT Act 66E"],
    "obscene":                  ["IT Act 67 / 67A"],
    "pornograph":               ["IT Act 67 / 67A"],
    "obscene image":            ["IT Act 67 / 67A"],
    "nude":                     ["IT Act 67 / 67A"],
    "cyber terrorism":          ["IT Act 66F"],
    "disclosure of information":["IT Act 72A"],
    "personal data":            ["IT Act 72A"],
    "child pornography":        ["IT Act 67B (Child Pornography)"],
    "child abuse material":     ["IT Act 67B (Child Pornography)"],

    # ── Evidence ─────────────────────────────────────────────────────
    "electronic record":        ["Section 65B (Evidence Act)", "IT Act 65A / 65B"],
    "digital evidence":         ["Section 65B (Evidence Act)", "Electronic Evidence Best Practices"],
    "email":                    ["Section 65B (Evidence Act)"],
    "screenshot":               ["Section 65B (Evidence Act)"],
    "dna":                      ["DNA Evidence (Judicial Standards)"],
    "forensic":                 ["DNA Evidence (Judicial Standards)", "Electronic Evidence Best Practices"],
    "chain of custody":         ["Electronic Evidence Best Practices"],
    "confession":               ["Section 27 (Evidence Act)"],
    "accused statement":        ["Section 27 (Evidence Act)"],
    "admissibility":            ["Section 65B (Evidence Act)"],

    # ── Contract & Civil ─────────────────────────────────────────────
    "contract":                 ["Contract Act 10", "Contract Act 73"],
    "agreement":                ["Contract Act 10"],
    "breach":                   ["Contract Act 73"],
    "damages":                  ["Contract Act 73"],
    "compensation":             ["Contract Act 73"],
    "limitation":               ["Limitation Act (Selected)"],
    "time limit":               ["Limitation Act (Selected)"],
    "civil suit":               ["Limitation Act (Selected)"],

    # ── Special & Procedural Laws ────────────────────────────────────
    "narcotic":                 ["NDPS Act (Selected Provisions)"],
    "drug":                     ["NDPS Act (Selected Provisions)"],
    "drugs":                    ["NDPS Act (Selected Provisions)"],
    "psychotropic":             ["NDPS Act (Selected Provisions)"],
    "motor vehicle":            ["Motor Vehicles Act (Selected)"],
    "traffic":                  ["Motor Vehicles Act (Selected)"],
    "drunk driving":            ["Motor Vehicles Act (Selected)"],
    "rash driving":             ["Motor Vehicles Act (Selected)"],
    "accident":                 ["Motor Vehicles Act (Selected)"],
    "consumer":                 ["Consumer Protection (Selected Provisions)"],
    "defective":                ["Consumer Protection (Selected Provisions)"],
    "unfair trade":             ["Consumer Protection (Selected Provisions)"],
    "juvenile":                 ["Juvenile Justice (Selected Provisions)"],
    "minor":                    ["Juvenile Justice (Selected Provisions)"],
    "child":                    ["Juvenile Justice (Selected Provisions)"],
    "extradition":              ["Extradition (Selected Provisions)"],
    "fugitive":                 ["Extradition (Selected Provisions)"],
}


def _build_section_lookup():
    """
    Build a flat map: section_key → (category, section_key)
    for fast validation and fuzzy matching.
    """
    lookup = {}
    for category, laws in LAW_SECTIONS.items():
        for section_key, details in laws.items():
            lookup[section_key] = (category, section_key, details)
    return lookup


_SECTION_LOOKUP = _build_section_lookup()


def _keyword_match(crime_text: str):
    """Match crime text against KEYWORD_SECTION_MAP (case-insensitive substring match)."""
    crime_lower = crime_text.lower()
    matched = set()
    for keyword, sections in KEYWORD_SECTION_MAP.items():
        if keyword in crime_lower:
            matched.update(sections)
    return matched


def _fuzzy_match(crime_text: str, top_n: int = 3):
    """
    Fallback: score each section by word overlap between the user's text
    and the section title + description. Returns top_n section keys.
    """
    crime_words = set(w.strip(".,;:!?\"'()") for w in crime_text.lower().split() if len(w) > 3)
    scores = []
    for section_key, (category, _, details) in _SECTION_LOOKUP.items():
        combined = (details.get("title", "") + " " + details.get("description", "")).lower()
        section_words = set(w.strip(".,;:!?\"'()") for w in combined.split() if len(w) > 3)
        overlap = len(crime_words & section_words)
        if overlap > 0:
            scores.append((overlap, section_key))
    scores.sort(reverse=True)
    return [section_key for _, section_key in scores[:top_n]]


def find_relevant_sections(crime_text: str):
    """
    Map a crime/legal issue description to validated (category, section) tuples.

    Strategy:
    1. Keyword match against comprehensive KEYWORD_SECTION_MAP.
    2. If fewer than 2 sections matched, supplement with fuzzy word-overlap fallback.
    3. Validate all results against law_data.py and return verified (category, section) pairs.
    """
    matched_keys = _keyword_match(crime_text)

    # Supplement with fuzzy match when keyword matching yields sparse results
    if len(matched_keys) < 2:
        fuzzy_keys = _fuzzy_match(crime_text, top_n=4)
        matched_keys.update(fuzzy_keys)

    # Validate against law library and return ordered results
    verified = []
    seen = set()
    for category, laws in LAW_SECTIONS.items():
        for section_key in laws:
            if section_key in matched_keys and section_key not in seen:
                verified.append((category, section_key))
                seen.add(section_key)

    return verified
