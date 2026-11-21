"""Printed-value checks for nominal responses."""

from __future__ import annotations

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tools.shown import shown

import math
from fractions import Fraction

ROOT = Path(__file__).resolve().parents[1]
PROSE = (ROOT / "research" / "content" / "nominal-responses.md").read_text(encoding="utf-8")
PROSE = shown(PROSE, "nominal-responses")


def main() -> None:
    p = (Fraction(1, 2), Fraction(3, 10), Fraction(1, 5))
    assert sum(p) == 1
    assert abs(math.log(3 / 5) - (-0.5108256237659907)) < 1e-12
    assert f"{math.log(3 / 5):.4f}" == "-0.5108"
    assert f"{math.log(2 / 5):.4f}" == "-0.9163"
    assert f"{math.log(2 / 3):.4f}" == "-0.4055"
    assert math.isclose(math.log(p[2] / p[0]) - math.log(p[1] / p[0]), math.log(p[2] / p[1]))
    denom = 1 + Fraction(3, 5) + Fraction(2, 5)
    assert denom == 2
    assert Fraction(1, 1) / denom == Fraction(1, 2)
    assert Fraction(3, 5) / denom == Fraction(3, 10)
    assert Fraction(2, 5) / denom == Fraction(1, 5)
    q = (Fraction(3, 5), Fraction(3, 10), Fraction(1, 10))
    assert sum(q) == 1
    assert math.isclose(math.log(float(q[2] / q[0])) - math.log(float(q[1] / q[0])), math.log(1 / 3))
    assert Fraction(6, 2) == 3
    assert 1 + 2 + 6 == 9
    for token in ("-0.5108", "-0.9163", "-0.4055", "1/9", "3/10"):
        assert token in PROSE, token
    article = ROOT / "articles" / "nominal-responses.qmd"
    if article.is_file():
        body = article.read_text(encoding="utf-8")
        assert "-0.5108" in body and "1/9" in body
    print("nominal-responses checks passed")


if __name__ == "__main__":
    main()
