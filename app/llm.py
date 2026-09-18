class LLM:
    def generate(self, prompt: str) -> str:
        raise NotImplementedError


class MockLLM(LLM):
    def generate(self, prompt: str) -> str:
        if "refund" in prompt.lower():
            return "Customers can request a refund within 30 days of purchase."

        if "shipping" in prompt.lower():
            return "Standard shipping takes 5-7 business days."

        if "cancel" in prompt.lower():
            return "Orders can be cancelled before they are dispatched."

        return "I don't have enough information to answer that."