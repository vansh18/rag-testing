from app.llm import MockLLM
from app.rag import answer_question
from app.retriever import load_documents

documents = load_documents()
llm = MockLLM()

answer = answer_question(
    "Can I cancel my order?",
    documents,
    llm
)

print(answer)

