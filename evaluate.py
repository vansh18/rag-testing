from app.evaluation import evaluate_retrieval
from app.retriever import load_documents
from tests.evaluation.dataset import EVALUATION_DATASET

MIN_HIT_RATE = 0.90
MIN_MRR = 0.80


documents = load_documents()

results = evaluate_retrieval(
    documents,
    EVALUATION_DATASET
)

print("\nRAG Evaluation")
print("-"*30)

print(f"Hit Rate: {results['hit_rate']:.2%}")
print(f"Precision: {results['precision']:.2%}")
print(f"Recall: {results['recall']:.2%}")
print(f"MRR: {results['mrr']:.2%}")


if results["hit_rate"] < MIN_HIT_RATE:
    raise SystemExit("RAG evaluation failed: Hit Rate below threshold.")

if results["mrr"] < MIN_MRR:
    raise SystemExit("RAG evaluation failed: MRR below threshold.")


print("\nRAG evaluation passed.")