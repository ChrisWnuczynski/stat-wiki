"""Exact checks for the training-set nearest-neighbour and intercept calculations."""

from fractions import Fraction
from pathlib import Path


def nearest_label(points, x):
    best = None
    for px, py in points:
        distance = abs(x - px)
        if best is None or distance < best[0]:
            best = (distance, py, px)
    return best


if __name__ == "__main__":
    article = (Path(__file__).resolve().parents[1] / "research/content/training-set.md").read_text()
    for printed in (r"\frac{4}{15}", "3/8", "10-2=8", "1/2", "3/4", r"3\%", r"50\%"):
        assert printed in article, f"Worked or sourced value missing from article: {printed}"
    train = ((0, 0), (1, 0), (3, 1))
    assert nearest_label(train, 0)[1:] == (0, 0)
    assert nearest_label(train, 1)[1:] == (0, 1)
    assert nearest_label(train, 3)[1:] == (1, 3)
    assert all(nearest_label(train, px)[2] == px for px, _ in train)
    at_15 = nearest_label(train, Fraction(3, 2))
    assert at_15[0] == Fraction(1, 2)
    assert at_15[1:] == (0, 1)
    distances = {px: abs(Fraction(3, 2) - px) for px, _ in train}
    assert distances == {0: Fraction(3, 2), 1: Fraction(1, 2), 3: Fraction(3, 2)}
    assert abs(Fraction(1, 2) - 0) == abs(Fraction(1, 2) - 1)
    assert abs(2 - 1) == abs(2 - 3)
    error_length = Fraction(2) - Fraction(6, 5)
    conditional_error = error_length / 3
    assert error_length == Fraction(4, 5)
    assert conditional_error == Fraction(4, 15)

    exercise = ((0, 0), (2, 1), (4, 0))
    assert all(nearest_label(exercise, px)[2] == px for px, _ in exercise)
    assert nearest_label(exercise, Fraction(7, 2))[1:] == (0, 4)
    exercise_error = (Fraction(3, 2) - 1 + (4 - 3)) / 4
    assert exercise_error == Fraction(3, 8)

    responses = (1, 3, 3, 5)
    n = 4
    mean = Fraction(sum(responses), n)
    training_error = sum((Fraction(y) - mean) ** 2 for y in responses) / n
    sigma2 = 1
    mu = 0
    in_sample = sigma2 + (mean - mu) ** 2
    optimism = in_sample - training_error
    expected_optimism = Fraction(2 * sigma2, n)
    expected_training = Fraction(sigma2 * (n - 1), n)
    expected_in_sample = Fraction(sigma2 * (n + 1), n)
    assert mean == 3
    assert training_error == 2
    assert in_sample == 10
    assert optimism == 8
    assert expected_optimism == Fraction(1, 2)
    assert expected_training == Fraction(3, 4)
    assert expected_in_sample == Fraction(5, 4)
    assert expected_in_sample - expected_training == expected_optimism

    checks = [
        conditional_error == Fraction(4, 15),
        exercise_error == Fraction(3, 8),
        training_error == 2,
        optimism == 8,
        expected_optimism == Fraction(1, 2),
        expected_training == Fraction(3, 4),
        expected_in_sample == Fraction(5, 4),
        at_15[1] == 0,
        nearest_label(exercise, Fraction(6, 5))[1] == 1,
        nearest_label(exercise, Fraction(1, 2))[1] == 0,
    ]
    assert all(checks)
    print(f"training-set arithmetic: {len(checks)} checks passed")
