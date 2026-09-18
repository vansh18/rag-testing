from app.tools import get_order_status, cancel_order

class SimpleAgent:

    def run(self, request: str) -> str:

        request_lower = request.lower()

        if "status" in request_lower:
            order_id = request.split()[-1]

            try:
                return get_order_status(order_id)
            except Exception:
                return "Unable to retrieve the order status right now."

        if "cancel" in request_lower:
            order_id = request.split()[-1]

            try:
                return cancel_order(order_id)
            except Exception:
                return "Unable to cancel the order right now."

        return "I don't know how to handle that request."