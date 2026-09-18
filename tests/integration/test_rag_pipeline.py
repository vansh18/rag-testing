from app.llm import MockLLM
from app.rag import answer_question
from app.retriever import load_documents

def test_rag_pipeline_refund():

    documents = load_documents()
    llm = MockLLM()

    answer = answer_question(
        "How do I get a refund?",
        documents,
        llm
    )

    assert "refund" in answer.lower()
    assert "30 days" in answer

def test_rag_pipeline_unknown_question():

    documents = load_documents()
    llm = MockLLM()

    answer = answer_question(
        "What is your office address?",
        documents,
        llm
    )

    assert "don't have enough information" in answer.lower()