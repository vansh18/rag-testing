from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_ask_refund():

    response = client.post(
        "/ask",
        json={"question": "How do I get refund?"}
    )

    assert response.status_code == 200

    data = response.json()
    print("This is data", data)

    assert "answer" in data
    assert "refund" in data["answer"].lower()


def test_ask_missing_question():
    response = client.post(
        "/ask",
        json={}
    )

    assert response.status_code == 422