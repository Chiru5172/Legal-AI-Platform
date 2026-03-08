"""
crime_explainer.py
------------------
Explains crime description using FREE LLM.
"""

from llm_services.free_llm import load_free_llm


def explain_crime(crime_text: str) -> str:
    """
    Uses LLM to explain the given crime in legal terms.
    """
    llm = load_free_llm()

    prompt = (
        "Explain the following legal issue or crime in simple legal terms. "
        "Do not give punishment. Do not cite sections.\n\n"
        f"Crime description: {crime_text}"
    )

    response = llm(prompt)[0]["generated_text"]
    return response.strip()
