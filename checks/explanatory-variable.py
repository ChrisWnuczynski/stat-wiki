"""Recompute the regression examples and assert values printed in the article."""

from fractions import Fraction
from math import exp, isclose


if __name__ == "__main__":
    from pathlib import Path

    root = Path(__file__).resolve().parents[1]
    prose = (root / "research/content/explanatory-variable.md").read_text()
    for printed in ("175/3", "S_{xx}=(-1)^2+0^2+1^2=2", "S_{xy}=15", "15/2=7.5", "305/6", "745/12", "62.08", "9.5", "0.961", "1.516"):
        assert printed in prose, f"Worked value missing from article source: {printed}"
    xs = (0, 1, 2)
    ys = (50, 60, 65)
    xbar = Fraction(sum(xs), len(xs))
    ybar = Fraction(sum(ys), len(ys))
    sxx = sum((x - xbar) ** 2 for x in xs)
    sxy = sum((x - xbar) * (y - ybar) for x, y in zip(xs, ys))
    slope = sxy / sxx
    intercept = ybar - slope * xbar
    assert xbar == 1
    assert ybar == Fraction(175, 3)
    assert sxx == 2
    assert sxy == 15
    assert slope == Fraction(15, 2)
    assert intercept == Fraction(305, 6)
    assert intercept + slope * Fraction(3, 2) == Fraction(745, 12)
    challenge = (5, 8, 11)
    assert Fraction(challenge[-1] - challenge[0], xs[-1] - xs[0]) == 3
    assert 5 + 3 * Fraction(3, 2) == Fraction(19, 2)
    shoe_t = 1.0048 / 0.2178
    assert isclose(shoe_t, 4.613, abs_tol=0.001)
    assert isclose(shoe_t ** 2, 21.28, abs_tol=0.005)
    assert isclose(shoe_t ** 2 / (shoe_t ** 2 + 98), 0.178, abs_tol=0.001)
    assert round(exp(-0.04), 3) == 0.961
    assert round(2 ** 0.60, 3) == 1.516
    page = root / "articles/explanatory-variable.qmd"
    if page.exists():
        generated = page.read_text()
        for printed in ("1.0048/0.2178=4.61", "4.613^2=21.28", "17.8%"):
            assert printed in generated, f"Regression value missing from generated page: {printed}"
    print("explanatory-variable arithmetic: 12 checks passed")
