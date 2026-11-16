"""Printed-value checks for Dirichlet–multinomial conjugacy."""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROSE = (ROOT / "research" / "content" / "dirichlet-multinomial-conjugacy.md").read_text(encoding="utf-8")


def means(alpha, counts):
    total = sum(alpha) + sum(counts)
    return [Fraction(a + x, total) for a, x in zip(alpha, counts)]


def main() -> None:
    alpha = (2, 2, 2)
    counts = (3, 1, 2)
    got = means(alpha, counts)
    assert got == [Fraction(5, 12), Fraction(1, 4), Fraction(1, 3)]
    mode = [Fraction(x + a - 1, 6 + 6 - 3) for a, x in zip(alpha, counts)]
    assert mode == [Fraction(4, 9), Fraction(2, 9), Fraction(1, 3)]
    assert sum(mode) == 1
    mix = Fraction(6, 12) * Fraction(1, 3) + Fraction(6, 12) * Fraction(1, 2)
    assert mix == Fraction(5, 12)
    empty = means((2, 2, 2), (0, 0, 6))
    assert empty == [Fraction(1, 6), Fraction(1, 6), Fraction(2, 3)]
    mode0 = [Fraction(0 + 2 - 1, 9), Fraction(1, 9), Fraction(7, 9)]
    assert mode0[0] == mode0[1] == Fraction(1, 9)
    flat = means((1, 1, 1), (4, 1, 1))
    assert flat == [Fraction(5, 9), Fraction(2, 9), Fraction(2, 9)]
    for token in ("5/12", "frac49", "frac29", "5/9", "1/9", "7/9"):
        assert token in PROSE, token
    article = ROOT / "articles" / "dirichlet-multinomial-conjugacy.qmd"
    if article.is_file():
        body = article.read_text(encoding="utf-8")
        assert "5/12" in body and body.count('title="Proof"') == 1
    print("dirichlet-multinomial-conjugacy checks passed")


if __name__ == "__main__":
    main()
