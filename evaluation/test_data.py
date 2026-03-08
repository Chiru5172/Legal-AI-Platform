"""
test_data.py
------------
Ground-truth questions and expected legal sections.
"""

TEST_CASES = [
    {
        "question": "What are the rights of an arrested person?",
        "expected_sections": ["CrPC 50", "CrPC 41", "Article 22"]
    },
    {
        "question": "What punishment is given for cheating?",
        "expected_sections": ["IPC 420"]
    },
    {
        "question": "What law applies to online identity theft?",
        "expected_sections": ["IT Act 66C", "IT Act 66D"]
    },
    {
        "question": "What are the fundamental rights related to equality?",
        "expected_sections": ["Article 14"]
    }
]
