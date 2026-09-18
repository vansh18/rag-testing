from pathlib import Path


def load_documents(directory: str = "documents") -> list[dict]:
    documents = []

    for file_path in Path(directory).glob("*.txt"):
        documents.append({
            "id": file_path.name,
            "text": file_path.read_text(encoding="utf-8")
        })

    return documents

def retrieve(query: str, documents: list[dict], top_k: int = 2) -> list[dict]:

    query_words = set(query.lower().split())
    scored_documents = []

    for document in documents:
        document_words = set(document["text"].lower().split())

        score = len(query_words & document_words)
        scored_documents.append((score, document))

    scored_documents.sort(
        key=lambda item: item[0],
        reverse=True
    )

    return [
        document for score, document in scored_documents[:top_k] if score > 0
    ]