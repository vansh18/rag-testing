from fastapi import FastAPI
from pydantic import BaseModel

from app.llm import MockLLM
from app.rag import answer_question
from app.retriever import load_documents


app = FastAPI(title="RAG Testing Demo")

documents = load_documents()
llm = MockLLM()


class QuestionRequest(BaseModel):
    question: str


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/ask")
def ask_question(request: QuestionRequest):
    answer = answer_question(
        request.question,
        documents,
        llm
    )

    return {
        "answer": answer
    }