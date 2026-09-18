class MockJudge:
    def evaluate(
        self,
        question: str,
        context: str,
        answer: str,
        expected_answer: str,
    ) -> dict:

        return {
            "faithfulness": 1.0,
            "correctness": 1.0,
            "reason": "The answer is supported by the context."
        }