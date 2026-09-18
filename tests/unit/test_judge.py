from app.judge import MockJudge


def test_mock_judge():

    judge = MockJudge()

    result = judge.evaluate(
        question="How do I get a refund",
        context="Customer can request a refund within 30 days.",
        answer="You can request a refund within 30 days.",
        expected_answer="Customer can request a refund within 30 days.", 
    )

    assert result["faithfulness"] == 1.0
    assert result["correctness"] == 1.0
    assert "reason" in result