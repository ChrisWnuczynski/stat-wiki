"""Check all new numerical expectation examples with exact fractions."""

from fractions import Fraction


if __name__ == "__main__":
    assert Fraction(3, 10) * 100 == 30
    assert sum(range(1, 7)) / 6 == Fraction(7, 2)
    assert Fraction(1, 6) * 6 + Fraction(5, 6) * -2 == Fraction(-2, 3)
    assert Fraction(1, 3) * Fraction(9, 2) + Fraction(2, 3) * Fraction(-3, 2) == Fraction(1, 2)
    assert Fraction(1, 36) * 36 == 1
    assert Fraction(1, 36) ** -1 == 36
    for n in (1, 2, 10, 100):
        assert n * Fraction(1, n) == 1
        assert n * n * Fraction(1, n) == n
        assert 2**n * Fraction(1, 2**n) == 1
    print("expectation arithmetic: 18 exact checks passed")
