"""Independent arithmetic checks for research/content/variance.md."""

from fractions import Fraction
from math import isclose, sqrt
from pathlib import Path


def weighted_moments(values, probabilities):
    assert sum(probabilities) == 1
    mean = sum(value * probability for value, probability in zip(values, probabilities))
    second = sum(value * value * probability for value, probability in zip(values, probabilities))
    variance = sum((value - mean) ** 2 * probability for value, probability in zip(values, probabilities))
    assert variance == second - mean * mean
    return mean, variance


if __name__ == "__main__":
    root = Path(__file__).resolve().parents[1]
    prose = (root / "research/content/variance.md").read_text()
    for printed in ("100 squared minutes", "19/4=4.75", r"\approx2.179", "8/3"):
        assert printed in prose, f"Worked value missing from article source: {printed}"
    assert weighted_moments([10], [Fraction(1)]) == (10, 0)
    assert weighted_moments([0, 20], [Fraction(1, 2)] * 2) == (10, 100)
    mean, variance = weighted_moments([-2, 0, 4], [Fraction(1, 4), Fraction(1, 2), Fraction(1, 4)])
    assert (mean, variance) == (Fraction(1, 2), Fraction(19, 4))
    assert isclose(sqrt(variance), 2.179449471770337)
    assert round(sqrt(variance), 3) == 2.179
    assert weighted_moments([1, 3, 5], [Fraction(1, 3)] * 3) == (3, Fraction(8, 3))
    assert Fraction(1) + Fraction(2) ** 2 == 5
    assert Fraction(1, 3) - Fraction(1, 2) ** 2 == Fraction(1, 12)
    die_variance = sum((Fraction(k) - Fraction(7, 2)) ** 2 for k in range(1, 7)) / 6
    assert die_variance == Fraction(35, 12)
    dice_variance = 2 * die_variance
    assert dice_variance == Fraction(35, 6) and round(float(dice_variance), 2) == 5.83
    assert dice_variance - 5 == Fraction(5, 6)
    assert round(float(100 * (dice_variance - 5)), 1) == 83.3
    generated = root / "articles/variance.qmd"
    if generated.exists():
        page = generated.read_text()
        for printed in ("1/12", "35/6", "5.83", "5/6", "83.3"):
            assert printed in page, f"Original worked value missing from generated page: {printed}"
    print("variance arithmetic and printed values passed")
