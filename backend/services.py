from backend.schemas import LegalQueryRequest, LegalQueryResponse, Evidence
from generation.rag_chain import run_legal_rag


def process_legal_query(request: LegalQueryRequest, vectorstore=None):
    result = run_legal_rag(
        question=request.query,
        top_k=request.top_k,
        vectorstore=vectorstore
    )

    evidence = [
        Evidence(
            source=doc.metadata.get("source"),
            page_number=doc.metadata.get("page_number"),
            content=doc.page_content
        )
        for doc in result["source_documents"]
    ]

    return LegalQueryResponse(
        query=request.query,
        answer=result["answer"],
        evidence=evidence
    )
