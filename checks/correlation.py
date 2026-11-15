"""Recompute the population and sample correlation examples."""

from fractions import Fraction
from math import isclose
from pathlib import Path
import re


if __name__ == "__main__":
    root = Path(__file__).resolve().parents[1]
    prose = (root / "research/content/correlation.md").read_text()
    for marker in re.finditer(r"\{\{cite:([^}]+)\}\}", prose):
        assert re.match(r" \((?:Ch\.|pp\.|Description)", prose[marker.end():]), (
            f"Citation without a location: {marker.group()}"
        )
    for printed in (
        "$(1,1)$, $(2,3)$, and $(3,2)$",
        "Both sample means are $2$",
        r"r=1/\sqrt{2\cdot2}=1/2",
        "1/(3-1)=1/2",
        "2/(3-1)=1",
        "$y'=5-2y$",
        "correlation becomes $-1/2$",
        "positive $12$ leaves it at $1/2$",
    ):
        assert printed in prose, f"Worked value missing from article source: {printed}"
    pairs = ((1, 1), (2, 3), (3, 2))
    xbar = Fraction(sum(x for x, _ in pairs), len(pairs))
    ybar = Fraction(sum(y for _, y in pairs), len(pairs))
    sxx = sum((x - xbar) ** 2 for x, _ in pairs)
    syy = sum((y - ybar) ** 2 for _, y in pairs)
    sxy = sum((x - xbar) * (y - ybar) for x, y in pairs)
    transformed = tuple((x, 5 - 2 * y) for x, y in pairs)
    nonlinear = tuple((x, x * x) for x in (-2, -1, 0, 1, 2))
    checks = [
        xbar == 2,
        ybar == 2,
        sxx == 2,
        syy == 2,
        sxy == 1,
        Fraction(sxy, 2) == Fraction(1, 2),
        isclose(sxy / (sxx * syy) ** 0.5, 0.5),
        3 / (2 * 3) == 0.5,
        4 * 9 - 3 * 3 == 27,
        sum((x - xbar) * (y - 1) for x, y in transformed) == -2,
        sum((y - 1) ** 2 for _, y in transformed) == 8,
        isclose(-2 / (2 * 8) ** 0.5, -0.5),
        Fraction(1, 2) * 12 / 12 == Fraction(1, 2),
        sum(x * y for x, y in nonlinear) == 0,
        len({y for _, y in nonlinear}) > 1,
        Fraction(1, 2) ** 2 == Fraction(1, 4),
    ]
    assert all(checks)
    generated = root / "articles/correlation.qmd"
    if generated.exists():
        page = generated.read_text()
        for printed in ("3/(2\\times 3)=1/2", r"\begin{pmatrix}4&3\\3&9\end{pmatrix}"):
            assert printed in page, f"Population value missing from generated article: {printed}"
        for unopened in ("anderson2003_mva", "wasserman2004", "pearson1896"):
            assert f'data-cite-key="{unopened}"' not in page, f"Unopened source still cited: {unopened}"
    print(f"correlation arithmetic: {len(checks)} checks passed")
