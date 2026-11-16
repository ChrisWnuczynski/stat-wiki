"""Printed-value checks for the confounding-variable depth pass."""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROSE = (ROOT / "research" / "content" / "confounding-variable.md").read_text(encoding="utf-8")


def main() -> None:
    men_a, men_b = Fraction(8, 10), Fraction(70, 100)
    women_a, women_b = Fraction(40, 100), Fraction(3, 10)
    assert men_a == Fraction(4, 5) and men_b == Fraction(7, 10)
    assert women_a == Fraction(2, 5) and women_b == Fraction(3, 10)
    assert men_a > men_b and women_a > women_b
    pooled_a = Fraction(8 + 40, 10 + 100)
    pooled_b = Fraction(70 + 3, 100 + 10)
    assert pooled_a == Fraction(24, 55) == Fraction(48, 110)
    assert pooled_b == Fraction(73, 110)
    assert pooled_a < pooled_b
    assert abs(float(pooled_a) - 0.43636363636363634) < 1e-12
    assert abs(float(pooled_b) - 0.6636363636363637) < 1e-12
    assert "0.4364" in PROSE and "0.6636" in PROSE
    assert Fraction(100, 110) == Fraction(10, 11)
    weights = Fraction(10, 110) * men_a + Fraction(100, 110) * women_a
    assert weights == pooled_a
    balanced_a = 50 * men_a + 50 * women_a
    balanced_b = 50 * men_b + 50 * women_b
    assert balanced_a == 60 and balanced_b == 50
    assert Fraction(1, 2) * men_b + Fraction(1, 2) * women_b == Fraction(1, 2)
    for token in ("24/55", "73/110", "10/11", "0.60", "48/110"):
        assert token in PROSE, token
    article = ROOT / "articles" / "confounding-variable.qmd"
    if article.is_file():
        body = article.read_text(encoding="utf-8")
        assert "24/55" in body and "73/110" in body
        assert "da-01-studies-and-data-assignment.png" in body
    print("confounding-variable checks passed")


if __name__ == "__main__":
    main()
