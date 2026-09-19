from app.retriever import load_documents, retrieve


def test_load_documents():

    documents = load_documents()

    assert len(documents) > 0

    for document in documents:
        assert "id" in document
        assert "text" in document


def test_retrieve_refund_document():

    documents = load_documents()

    retrieved_docs = retrieve("How do I get a refund?", documents)

    assert len(retrieved_docs) > 0
    assert any(doc["id"] == "refund.txt" for doc in retrieved_docs)


def test_retrieve_shipping_document():
    documents = load_documents()

    retrieved_docs = retrieve("How long does shipping take?", documents)

    assert len(retrieved_docs) > 0
    assert any(doc["id"] == "shipping.txt" for doc in retrieved_docs)



def test_retrieve_cancellation_document():
    documents = load_documents()

    retrieved_docs = retrieve("Can I cancel my order?", documents)

    assert len(retrieved_docs) > 0
    assert any(doc["id"] == "cancellation.txt" for doc in retrieved_docs)


