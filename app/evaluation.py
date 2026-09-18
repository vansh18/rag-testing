from app.retriever import retrieve

def calculate_hit_rate(results: list[bool]) -> float:

    if not results:
        return 0.0

    return sum(results) /  len(results)


def calculate_precision(retrieved_documents: list[str], expected_documents: list[str]) -> float:

    if not retrieved_documents:
        return 0.0

    relevant_count = sum(
        doc in expected_documents
        for doc in retrieved_documents
    )

    return relevant_count / len(retrieved_documents)

def calculate_recall(retrieved_documents: list[str], expected_documents: list[str]) -> float:

    if not expected_documents:
        return 0.0

    relevant_count = sum(
        doc in expected_documents
        for doc in retrieved_documents
    )

    return relevant_count / len(expected_documents)


def calculate_mrr(retrieved_documents: list[str], expected_documents: list[str]) -> float:

    for rank, document in enumerate(retrieved_documents, start=1):
        if document in expected_documents:
            return 1 / rank

    return 0.0


def context_contains_expected_document(
    retrieved_documents: list[str],
    expected_documents: list[str]
) -> bool:
    return any(
        document in expected_documents
        for document in retrieved_documents
    )


def is_answer_grounded(
    answer: str,
    context: str
) -> bool:
    return answer.lower() in context.lower()


def answer_contains_expected_information(
    answer: str,
    expected_answer: str
) -> bool:
    return expected_answer.lower() in answer.lower()


def evaluate_retrieval(
        documents: list[str],
        dataset: list[dict],
        top_k: int=2,
) -> dict:
    
    hit_results = []
    precision_scores = []
    recall_scores = []
    mrr_scores = []

    for case in dataset:
        retrieved_docs = retrieve(
            case["question"],
            documents,
            top_k=top_k
        )

        retrieved_ids = [
            doc["id"]
            for doc in retrieved_docs
        ]

        expected_ids = case["expected_documents"]

        hit_results.append(
            any(
                doc_id in expected_ids
                for doc_id in retrieved_ids
            )
        )

        precision_scores.append(
            calculate_precision(
                retrieved_ids,
                expected_ids,
            )
        )

        recall_scores.append(
            calculate_recall(
                retrieved_ids,
                expected_ids,
            )
        )

        mrr_scores.append(
            calculate_mrr(
                retrieved_ids,
                expected_ids,
            )
        )

    return {
        "hit_rate": calculate_hit_rate(hit_results),
        "precision": sum(precision_scores) / len(precision_scores),
        "recall": sum(recall_scores) / len(recall_scores),
        "mrr": sum(mrr_scores) / len(mrr_scores),
    }


def evaluate_answer(
        question: str,
        context: str,
        answer: str,
        expected_answer: str,
        judge,
) -> dict:

    return judge.evaluate(
        question=question,
        context=context,
        answer=answer,
        expected_answer=expected_answer,
    )