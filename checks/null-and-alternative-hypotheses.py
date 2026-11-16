"""Check all binomial arithmetic printed on the hypotheses article."""

from fractions import Fraction
from math import comb
from pathlib import Path


def tail(n: int, p: Fraction, cutoff: int) -> Fraction:
    return sum(
        (Fraction(comb(n, k)) * p**k * (1 - p) ** (n - k) for k in range(cutoff, n + 1)),
        Fraction(0),
    )


def main() -> None:
    article = (Path(__file__).resolve().parents[1] / "articles/null-and-alternative-hypotheses.qmd").read_text()
    assert [comb(12, k) for k in (10, 11, 12)] == [66, 12, 1]
    assert tail(12, Fraction(1, 2), 10) == Fraction(79, 4096)
    assert tail(12, Fraction(1, 2), 9) == Fraction(299, 4096)
    assert round(float(Fraction(79, 4096)), 4) == 0.0193
    assert round(float(Fraction(299, 4096)), 4) == 0.0730
    assert Fraction(79, 4096) < Fraction(5, 100) < Fraction(299, 4096)
    power = tail(12, Fraction(7, 10), 10)
    assert round(float(power), 4) == 0.2528
    assert round(float(1 - power), 4) == 0.7472
    assert round(float((1 - Fraction(79, 4096)) * 100), 2) == 98.07
    assert sum(comb(20, k) for k in range(15, 21)) == 21700
    assert 2**20 == 1048576
    assert round(21700 / 1048576, 3) == 0.021
    for printed in (
        "79}{4096}",
        "299/4096",
        "0.0193",
        "0.0730",
        "0.2528",
        "0.7472",
        "98.07",
        "21700}{1048576}",
    ):
        assert printed in article, f"Missing printed value: {printed}"
    print("null-and-alternative-hypotheses arithmetic: 12 checks passed")


if __name__ == "__main__":
    main()
