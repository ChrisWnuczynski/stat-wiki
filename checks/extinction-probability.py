"""Printed-value checks for the extinction probability."""

from __future__ import annotations

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tools.shown import shown

from fractions import Fraction

ROOT = Path(__file__).resolve().parents[1]
PROSE = (ROOT / "research" / "content" / "extinction-probability.md").read_text(encoding="utf-8")
PROSE = shown(PROSE, "extinction-probability")


def main() -> None:
    assert 2 * Fraction(3, 4) == Fraction(3, 2)
    # (3s-1)(s-1)=3s^2-4s+1
    assert Fraction(3, 4) * Fraction(1, 9) + Fraction(1, 4) == Fraction(1, 3)
    assert Fraction(1, 2) + Fraction(1, 2) * 1 == 1  # mean 1/2, fixed point 1
    mean_turn = Fraction(1, 4) + 2 * Fraction(1, 4)
    assert mean_turn == Fraction(3, 4)
    # s^2 - 3s + 2 = (s-1)(s-2)
    assert (1 - 1) * (1 - 2) == 0
    mean_check = Fraction(1, 8) + 2 * Fraction(3, 4)
    assert mean_check == Fraction(13, 8)
    assert Fraction(13, 8) > 1
    assert "1/3" in PROSE and "3/2" in PROSE and "13/8" in PROSE and "3/4" in PROSE
    article = ROOT / "articles" / "extinction-probability.qmd"
    if article.is_file():
        body = article.read_text(encoding="utf-8")
        assert "1/3" in body and "13/8" in body
    print("extinction-probability checks passed")


if __name__ == "__main__":
    main()
