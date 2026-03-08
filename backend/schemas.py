"""
schemas.py
----------
Defines request and response data structures
for the legal RAG system.
"""

from typing import List
from pydantic import BaseModel


class LegalQueryRequest(BaseModel):
    query: str
    top_k: int = 5


class Evidence(BaseModel):
    source: str
    page_number: int
    content: str


class LegalQueryResponse(BaseModel):
    query: str
    answer: str
    evidence: List[Evidence]
