from unittest.mock import patch

from app.agent import SimpleAgent
from app.tools import OrderServiceError


def test_agent_gets_order_status():

    agent = SimpleAgent()

    result = agent.run(
        "What is the status of order 123"
    )

    assert result == "Your order has been shipped."


@patch("app.agent.get_order_status")
def test_agent_chooses_status_tool(mock_get_status):

    mock_get_status.return_value = "Order shipped."

    agent = SimpleAgent()

    result = agent.run(
        "What is the status of order 123"
    )

    assert result == "Order shipped."

    mock_get_status.assert_called_once_with("123")


@patch("app.agent.get_order_status")
def test_agent_handles_tool_failure(mock_get_status):

    mock_get_status.side_effect = OrderServiceError("Order service is down")

    agent = SimpleAgent()

    result = agent.run(
        "What is the status of order 123"
    )

    assert result == "Unable to retrieve the order status right now."

    mock_get_status.assert_called_once_with("123")