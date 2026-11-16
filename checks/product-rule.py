"""Printed-value checks for the product rule."""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROSE = (ROOT / "research" / "content" / "product-rule.md").read_text(encoding="utf-8")


def main() -> None:
    joint = Fraction(5, 10) * Fraction(4, 9) * Fraction(3, 8)
    assert joint == Fraction(1, 12)
    assert Fraction(1, 2) ** 3 == Fraction(1, 8)
    assert Fraction(4, 6) * Fraction(3, 5) == Fraction(2, 5)
    assert Fraction(5, 10) * Fraction(5, 9) == Fraction(5, 18)
    assert Fraction(1, 2) ** 3 == Fraction(1, 8)
    for token in ("1}{12", "1/8", "2}{5", "5}{18"):
        assert token in PROSE, token
    article = ROOT / "articles" / "product-rule.qmd"
    if article.is_file():
        body = article.read_text(encoding="utf-8")
        assert r"\frac{1}{12}" in body
        assert body.count('title="Proof"') == 1
    print("product-rule checks passed")


if __name__ == "__main__":
    main()
