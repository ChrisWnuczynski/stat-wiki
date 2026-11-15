"""Recompute the article's variance, regression, and table counts."""

from fractions import Fraction
from pathlib import Path


if __name__ == "__main__":
    root = Path(__file__).resolve().parents[1]
    prose = (root / "research/content/degrees-of-freedom.md").read_text()
    for printed in ("-2,-1,0,1,2", "2.5", "12-3=9", "18/9=2", "(4-1)(5-1)=12", "8-1-1=6", "10-1-2=7", "10-1=9"):
        assert printed in prose, f"Worked value missing from article source: {printed}"
    values = (8, 9, 10, 11, 12)
    mean = Fraction(sum(values), len(values))
    residuals = tuple(value - mean for value in values)
    rss = sum(residual * residual for residual in residuals)
    assert mean == 10
    assert residuals == (-2, -1, 0, 1, 2)
    assert sum(residuals) == 0
    assert rss == 10
    assert rss / (len(values) - 1) == Fraction(5, 2)
    assert rss / len(values) == 2
    assert 12 - 3 == 9
    assert Fraction(18, 12 - 3) == 2
    assert (4 - 1) * (5 - 1) == 12
    assert 8 - 1 - 1 == 6
    assert 10 - 1 - 2 == 7
    assert 10 - 1 == 9
    for n, rho in ((5, Fraction(0)), (5, Fraction(1, 4)), (7, Fraction(-1, 6))):
        sigma2 = 3
        mean_variance = Fraction(sigma2 * (1 + (n - 1) * rho), n)
        assert n * sigma2 - n * mean_variance == (n - 1) * sigma2 * (1 - rho)
    print("degrees-of-freedom arithmetic and printed values passed")
