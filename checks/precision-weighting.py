"""Printed-value checks for precision weighting."""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROSE = (ROOT / "research" / "content" / "precision-weighting.md").read_text(encoding="utf-8")


def main() -> None:
    a = Fraction(4, 4 + 1)
    assert a == Fraction(4, 5)
    assert a * 10 == 8
    assert a / 4 == Fraction(1, 5)
    assert float(a / 4) == 0.2
    mu = Fraction(5 * 20 + 16, 6)
    assert mu == Fraction(58, 3)
    a9 = Fraction(9, 10)
    assert a9 * 3 == Fraction(27, 10)
    assert a9 / 9 == Fraction(1, 10)
    kappa = Fraction(4, 1)
    assert Fraction(4, 4 + kappa) == Fraction(1, 2)
    for token in ("0.8", "0.2", "58/3", "2.7", "0.1", "19.3333"):
        assert token in PROSE, token
    article = ROOT / "articles" / "precision-weighting.qmd"
    if article.is_file():
        body = article.read_text(encoding="utf-8")
        assert "58/3" in body and "0.8" in body
    print("precision-weighting checks passed")


if __name__ == "__main__":
    main()
