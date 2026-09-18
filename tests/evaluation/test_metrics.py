from app.evaluation import (
    calculate_hit_rate, 
    calculate_recall, 
    calculate_precision,
    calculate_mrr,
    context_contains_expected_document,
    is_answer_grounded,
    answer_contains_expected_information
)

def test_hit_rate():

    results = [True, True, False, True]

    hit_rate = calculate_hit_rate(results)

    assert hit_rate == 0.75


def test_precision():
    retrieved = [
        "refund.txt",
        "shipping.txt",
        "cancellation.txt",
    ]

    expected = ["refund.txt"]

    precision = calculate_precision(retrieved, expected)

    assert precision == 1 / 3


def test_recall():
    retrieved = ["refund.txt"]

    expected = ["refund.txt"]

    recall = calculate_recall(retrieved, expected)

    assert recall == 1.0


def test_mrr():
    retrieved = [
        "shipping.txt",
        "refund.txt",
        "cancellation.txt",
    ]

    expected = ["refund.txt"]

    mrr = calculate_mrr(retrieved, expected)

    assert mrr == 0.5


def test_relevant_context():
    retrieved = ["refund.txt"]
    expected = ["refund.txt"]

    assert context_contains_expected_document(
        retrieved,
        expected
    )


def test_irrelevant_context():
    retrieved = ["shipping.txt"]
    expected = ["refund.txt"]

    assert not context_contains_expected_document(
        retrieved,
        expected
    )


def test_answer_grounded():
    context = (
        "Customers can request a refund within 30 days "
        "of purchase."
    )

    answer = (
        "Customers can request a refund within 30 days "
        "of purchase."
    )

    assert is_answer_grounded(answer, context)

def test_answer_not_grounded():
    context = (
        "Customers can request a refund within 30 days "
        "of purchase."
    )

    answer = (
        "Customers can request a refund within 30 days "
        "and refunds are processed in 5 days."
    )

    assert not is_answer_grounded(answer, context)


def test_correct_answer():
    answer = "Customers can request a refund within 30 days of purchase."
    expected = "Customers can request a refund within 30 days of purchase."

    assert answer_contains_expected_information(
        answer,
        expected
    )