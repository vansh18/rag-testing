from app.retriever import load_documents, retrieve
from tests.evaluation.dataset import EVALUATION_DATASET

def test_retrieval_evaluation():

    documents = load_documents()

    for case in EVALUATION_DATASET:

        retrieved_docs = retrieve(
            case["question"],
            documents
        )

        retrieved_ids = [
            doc['id']
            for doc in retrieved_docs
        ]

        assert any(
            doc_id in retrieved_ids
            for doc_id in case["expected_documents"]
        )