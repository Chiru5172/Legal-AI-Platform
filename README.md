# ⚖️ Legal AI Platform

An AI-powered legal research and complaint drafting system using Retrieval-Augmented Generation (RAG).

## Features
- Legal document analysis
- Evidence-backed legal research
- Law explorer with sections
- AI-powered legal advice
- Complaint letter generator
- PDF export

## Tech Stack
- Python
- Streamlit
- LangChain
- FAISS
- HuggingFace Transformers

Project Structure
legal-ai-platform/
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── frontend/                         # STREAMLIT UI (MULTI-PAGE)
│   ├── app.py                        # Main router / entry point
│   └── pages/
│       ├── 1_Home_RAG.py             # Existing RAG-based Legal Q&A
│       ├── 2_Legal_Advice.py         # NEW: Legal Advice + Library
│       └── 3_Complaint_Generator.py  # NEW: Letter generation page
│
├── backend/                          # SERVICE LAYER
│   ├── __init__.py
│   ├── api.py
│   ├── services.py
│   └── schemas.py
│
├── ingestion/                        # DOCUMENT INGESTION
│   ├── __init__.py
│   ├── pdf_loader.py
│   ├── text_cleaner.py
│   └── chunker.py
│
├── embeddings/                       # VECTOR + FAISS
│   ├── __init__.py
│   ├── embedding_model.py            # HuggingFace embeddings (FREE)
│   └── vector_store.py
│
├── retrieval/                        # RETRIEVAL (R in RAG)
│   ├── __init__.py
│   └── dense_retriever.py
│
├── generation/                       # GENERATION (G in RAG)
│   ├── __init__.py
│   ├── context_builder.py
│   ├── prompt_templates.py
│   └── rag_chain.py
│
├── legal_library/                    # 🔥 NEW: LEGAL KNOWLEDGE BASE
│   ├── __init__.py
│   ├── law_data.py                   # All laws + sections (structured)
│   ├── library_service.py            # Fetch/search sections
│   └── section_classifier.py         # Maps crime → law category
│
├── llm_services/                     # 🔥 NEW: FREE LLM SERVICES
│   ├── __init__.py
│   ├── free_llm.py                   # Loads & caches FREE LLM
│   ├── crime_explainer.py            # Explains crime + sections
│   └── letter_generator.py           # Generates complaint letters
│
├── evaluation/                       # EVALUATION
│   ├── metrics.py
│   ├── hallucination_check.py
│   └── run_evaluation.py
│
├── data/
│   ├── raw_pdfs/                     # Optional static legal PDFs
│   └── faiss_index/                  # Stored FAISS index
│
│
└── venv/


## Run Locally

```bash
pip install -r requirements.txt
streamlit run frontend/app.py