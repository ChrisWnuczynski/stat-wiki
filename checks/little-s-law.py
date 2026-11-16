"""Printed-value checks for Little's law."""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROSE = (ROOT / "research" / "content" / "little-s-law.md").read_text(encoding="utf-8")


def main() -> None:
    assert 20 * Fraction(1, 4) == 5
    assert Fraction(5, 20) == Fraction(1, 4)
    assert 20 * Fraction(1, 10) == 2
    assert Fraction(1, 10) + Fraction(3, 20) == Fraction(1, 4)
    assert Fraction(8, 1) / Fraction(2, 5) == 20
    assert 12 * Fraction(1, 6) == 2
    assert 12 * Fraction(1, 4) == 3
    assert Fraction(1, 6) + Fraction(1, 12) == Fraction(1, 4)
    for token in ("20", "1/4", "1/10", "2/5", "15"):
        assert token in PROSE, token
    article = ROOT / "articles" / "little-s-law.qmd"
    if article.is_file():
        body = article.read_text(encoding="utf-8")
        assert "1/4" in body and "L=20" in body.replace(" ", "")
    print("little-s-law checks passed")


if __name__ == "__main__":
    main()
