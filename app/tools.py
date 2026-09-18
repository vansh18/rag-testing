def get_order_status(order_id: str) -> str:

    orders = {
        "123": "Your order has been shipped.",
        "456": "Your order is being processed."
    }

    if order_id not in orders:
        return "Order not found"

    return orders[order_id]


def cancel_order(order_id: str) -> str:

    return f"Order {order_id} has been cancelled."