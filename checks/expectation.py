"""Check all new numerical expectation examples with exact fractions."""

from fractions import Fraction
from pathlib import Path


if __name__ == "__main__":
    root = Path(__file__).resolve().parents[1]
    prose = (root / "research/content/expectation.md").read_text()
    for printed in ("30 dollars", "3.5", "-2/3", "0.50", "36", "1/36"):
        assert printed in prose, f"Worked value missing from article source: {printed}"
    assert Fraction(3, 10) * 100 == 30
    assert sum(range(1, 7)) / 6 == Fraction(7, 2)
    assert Fraction(1, 6) * 6 + Fraction(5, 6) * -2 == Fraction(-2, 3)
    assert Fraction(1, 3) * Fraction(9, 2) + Fraction(2, 3) * Fraction(-3, 2) == Fraction(1, 2)
    assert Fraction(1, 36) * 36 == 1
    assert Fraction(1, 36) ** -1 == 36
    assert 2 * Fraction(1, 3) + 5 * Fraction(1, 6) == Fraction(3, 2)
    assert 10 * Fraction(25, 100) == Fraction(5, 2)
    die_variance = sum((Fraction(k) - Fraction(7, 2)) ** 2 for k in range(1, 7)) / 6
    dice_variance = 2 * die_variance
    assert dice_variance == Fraction(35, 6)
    assert round(float(100 * (dice_variance - 5)), 1) == 83.3
    generated = root / "articles/expectation.qmd"
    if generated.exists():
        page = generated.read_text()
        for printed in ("3/2", "2.5", "35/6", "5.83", "83.3"):
            assert printed in page, f"Original worked value missing from generated page: {printed}"
    for n in (1, 2, 10, 100):
        assert n * Fraction(1, n) == 1
        assert n * n * Fraction(1, n) == n
        assert 2**n * Fraction(1, 2**n) == 1
    print("expectation arithmetic and printed values passed")
