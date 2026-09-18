from app.evaluation import evaluate_retrieval
from app.retriever import load_documents
from tests.evaluation.dataset import EVALUATION_DATASET

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