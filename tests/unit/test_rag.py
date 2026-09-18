from app.rag import build_context, build_prompt, answer_question
from app.llm import MockLLM
from app.retriever import load_documents
from unittest.mock import Mock


def test_build_context():
    documents = [
        {"id": "refund.txt", "text": "Refunds are available within 30 days."},
        {"id": "shipping.txt", "text": "Shipping takes 5-7 business days."},
    ]

    context = build_context(documents)

    assert "Refunds are available within 30 days." in context
    assert "Shipping takes 5-7 business days." in context

def test_build_context_with_no_documents():
    context = build_context([])

    assert context == ""


def test_build_prompt():

    question = "How do I cancel my order?"

    context = "Orders can be cancelled via mail."

    prompt = build_prompt(question, context)

    assert question in prompt
    assert context in prompt
    assert "provided context" in prompt.lower()


def test_answer_question_with_MockLLM():

    documents = [
        {
            "id": "refund.txt",
            "text": "Customers can request a refund with 30 days of delivery."
        }
    ]

    mock_llm = Mock()
    mock_llm.generate.return_value = "Refunds are available within 30 days."

    answer = answer_question(
        "How do I get a refund?",
        documents,
        mock_llm
    )

    assert answer == "Refunds are available within 30 days."
    mock_llm.generate.assert_called_once()
    prompt = mock_llm.generate.call_args[0][0]

    assert "How do I get a refund?" in prompt
    assert "Customers can request a refund with 30 days of delivery." in prompt
