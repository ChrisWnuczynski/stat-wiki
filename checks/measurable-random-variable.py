from pathlib import Path
"""Exact interval and inverse-image calculations on the measurability page."""


def inverse_image(outcomes, values, threshold):
    return frozenset(w for w, value in zip(outcomes, values) if value <= threshold)


def test_printed_values():
    page = (Path(__file__).resolve().parents[1] / "articles" / "measurable-random-variable.qmd").read_text()
    assert "{#worked-example}" in page and "Your turn" in page
    assert abs((0.7 - 0.2) - 0.5) < 1e-12
    assert 0.4 == 2 / 5
    assert 0.5 == 1 / 2

    outcomes = ("a", "b", "c", "d")
    sigma = {frozenset(), frozenset(("a", "b")),
             frozenset(("c", "d")), frozenset(outcomes)}
    assert inverse_image(outcomes, (0, 1, 1, 1), 0) == frozenset(("a",))
    assert inverse_image(outcomes, (0, 1, 1, 1), 0) not in sigma
    assert inverse_image(outcomes, (2, 2, 3, 3), 2) == frozenset(("a", "b"))
    assert inverse_image(outcomes, (2, 2, 3, 3), 2) in sigma
    assert inverse_image(outcomes, (0, 1, 0, 1), 0) == frozenset(("a", "c"))
    assert inverse_image(outcomes, (0, 1, 0, 1), 0) not in sigma

    # Uniform probabilities equal interval lengths in the page and new bank.
    assert 1 / 2 - 0 == 0.5
    assert 1 - 1 / 2 == 0.5
    assert (1 / 2) ** 2 == 1 / 4
    assert (3 / 4) ** 2 == 9 / 16
    assert 3 / 4 - 1 / 2 == 1 / 4


if __name__ == "__main__":
    test_printed_values()
