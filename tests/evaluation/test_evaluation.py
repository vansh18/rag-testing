from app.evaluation import evaluate_retrieval
from app.retriever import load_documents
from tests.evaluation.dataset import EVALUATION_DATASET


def test_retrieval_quality():
    documents = load_documents()

    results = evaluate_retrieval(
        documents,
        EVALUATION_DATASET,
    )

    assert results["hit_rate"] >= 0.90
    assert results["mrr"] >= 0.80