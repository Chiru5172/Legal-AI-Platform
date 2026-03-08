from backend.schemas import LegalQueryRequest
from backend.services import process_legal_query


def handle_query(query: str, top_k: int = 5, vectorstore=None):
    request = LegalQueryRequest(query=query, top_k=top_k)
    return process_legal_query(request, vectorstore)
