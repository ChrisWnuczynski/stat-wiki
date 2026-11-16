"""Printed-value checks for the Borel–Cantelli depth pass."""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROSE = (ROOT / "research" / "content" / "borel-cantelli-lemmas.md").read_text(encoding="utf-8")


def main() -> None:
    # sum_{n=5}^{∞} 2^{-n} = 2^{-5}/(1-1/2) = 1/16
    assert Fraction(1, 32) / Fraction(1, 2) == Fraction(1, 16)
    partial = sum(Fraction(1, 2) ** n for n in range(1, 5))
    assert partial == Fraction(15, 16)
    assert partial + Fraction(1, 16) == 1
    assert "1/16" in PROSE and "15/16" in PROSE
    assert "1/2" in PROSE and "1/n" in PROSE
    # 1-x <= exp(-x) at the endpoints used in the proof
    import math
    for x in (0, 0.25, 0.5, 1):
        assert 1 - x <= math.exp(-x) + 1e-12
    article = ROOT / "articles" / "borel-cantelli-lemmas.qmd"
    if article.is_file():
        body = article.read_text(encoding="utf-8")
        assert "1/16" in body and "15/16" in body
        assert body.count('title="Proof"') == 1
    print("borel-cantelli-lemmas checks passed")


if __name__ == "__main__":
    main()
