from typing import Dict, Any

# -------------------------------------------------
# 🔴 LEGACY VERBOSITY PATCH (CRITICAL FIX)
# -------------------------------------------------
import langchain
langchain.verbose = False  # <- REQUIRED for LangChain 1.x compatibility

from langchain_core.globals import set_verbose
set_verbose(False)

# -------------------------------------------------
# STANDARD IMPORTS
# -------------------------------------------------
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
from langchain_community.llms import HuggingFacePipeline

from retrieval.dense_retriever import semantic_search
from generation.context_builder import build_legal_context
from generation.prompt_templates import LEGAL_RAG_PROMPT


def load_llm():
    """
    Load HuggingFace LLM (Flan-T5) safely under LangChain 1.x
    """

    model_name = "google/flan-t5-large"

    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

    pipe = pipeline(
        task="text-generation",
        model=model,
        tokenizer=tokenizer,
        max_length=512,
        temperature=0.1
    )

    return HuggingFacePipeline(
        pipeline=pipe,
        verbose=False
    )


def run_legal_rag(
    question: str,
    top_k: int = 5,
    vectorstore=None
) -> Dict[str, Any]:
    """
    Executes Retrieval-Augmented Generation for legal queries.
    """

    # ----------------------------
    # RETRIEVAL
    # ----------------------------
    retrieved_docs = semantic_search(
        question,
        top_k=top_k,
        vectorstore=vectorstore
    )

    # ----------------------------
    # CONTEXT BUILDING
    # ----------------------------
    context = build_legal_context(retrieved_docs)

    # ----------------------------
    # GENERATION
    # ----------------------------
    llm = load_llm()

    prompt = LEGAL_RAG_PROMPT.format(
        context=context,
        question=question
    )

    answer = llm.invoke(prompt)

    return {
        "question": question,
        "answer": answer,
        "source_documents": retrieved_docs
    }
