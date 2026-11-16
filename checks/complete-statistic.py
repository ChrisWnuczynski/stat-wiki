from pathlib import Path
"""Numerical claims on the complete-statistic page."""
from fractions import Fraction
from math import comb, isclose


def test_printed_values():
    page = (Path(__file__).resolve().parents[1] / "articles" / "complete-statistic.qmd").read_text()
    assert "{#worked-example}" in page and "Your turn" in page
    n, t = 4, 3
    assert n * (n - 1) == 12
    assert t * (t - 1) == 6
    assert Fraction(t * (t - 1), n * (n - 1)) == Fraction(1, 2)
    assert Fraction(1, 2) == 0.50
    assert Fraction(t * t, n * n) == Fraction(9, 16) == 0.5625
    n, t = 5, 2
    assert n * (n - 1) == 20
    assert Fraction(t * (t - 1), n * (n - 1)) == Fraction(1, 10)
    assert isclose(float(Fraction(1, 10)), 0.10)
    assert Fraction(t * t, n * n) == Fraction(4, 25)
    assert isclose(float(Fraction(4, 25)), 0.16)
    for n in (2, 4, 5):
        for p in (Fraction(1, 4), Fraction(1, 2), Fraction(3, 4)):
            mean = sum(Fraction(comb(n, k)) * p**k * (1-p)**(n-k) * Fraction(k*(k-1), n*(n-1)) for k in range(n+1))
            plug = sum(Fraction(comb(n, k)) * p**k * (1-p)**(n-k) * Fraction(k*k,n*n) for k in range(n+1))
            assert mean == p*p
            assert plug == p*p + p*(1-p)/n
            if p == Fraction(1, 2):
                assert sum(Fraction(comb(n,k))*p**k*(1-p)**(n-k)*(k-Fraction(n,2)) for k in range(n+1)) == 0
        assert Fraction(n-1, n+1) == Fraction(n,n+1)-Fraction(1,n+1)
    # New bank question: three trials, two successes.
    assert Fraction(2 * 1, 3 * 2) == Fraction(1, 3)
    assert sum(Fraction(comb(3,k), 2**3) * Fraction(k*(k-1), 6) for k in range(4)) == Fraction(1, 4)
    # New bank counterexample: two trials at p=1/2.
    assert sum(Fraction(comb(2,k), 2**2) * (k-1) for k in range(3)) == 0
    assert Fraction(2 * Fraction(1, 4) - 1) == Fraction(-1, 2)


if __name__ == "__main__":
    test_printed_values()
