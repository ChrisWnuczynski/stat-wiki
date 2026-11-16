"""Exact checks for the event article's die and reliability examples."""

from fractions import Fraction
from itertools import product
from pathlib import Path


PAGE = Path(__file__).resolve().parents[1] / "articles" / "event.qmd"


if __name__ == "__main__":
    page = PAGE.read_text(encoding="utf-8")
    omega = set(range(1, 7))
    even = {2, 4, 6}
    high = {4, 5, 6}
    overlap = even & high
    union = even | high
    neither = omega - union

    outcomes = list(product((False, True), repeat=4))
    works = [x for x in outcomes if (x[0] or x[1]) and (x[2] or x[3])]
    q = Fraction(1, 10)
    aircraft = sum(q ** (4 - sum(x)) * (1 - q) ** sum(x) for x in works)

    checks = [
        len(omega) == 6,
        overlap == {4, 6},
        union == {2, 4, 5, 6},
        neither == {1, 3},
        Fraction(len(overlap), 6) == Fraction(1, 3),
        Fraction(len(union), 6) == Fraction(2, 3),
        Fraction(len(neither), 6) == Fraction(1, 3),
        Fraction(len(even), 6) + Fraction(len(high), 6)
        - Fraction(len(overlap), 6) == Fraction(2, 3),
        Fraction(len(overlap), len(high)) == Fraction(2, 3),
        omega - union == (omega - even) & (omega - high),
        omega - overlap == (omega - even) | (omega - high),
        len(outcomes) == 16,
        len(works) == 9,
        aircraft == Fraction(9801, 10000),
        aircraft == (1 - q * q) ** 2,
        f"${aircraft.numerator / aircraft.denominator:.4f}$" in page,
        "$2^4=16$" in page,
        "$2/6=1/3$" in page,
        "$4/6=2/3$" in page,
        "$3/6+3/6-2/6=4/6$" in page,
        "=(2/6)/(3/6)=2/3$" in page,
        "$(A\\cup B)^c=\\{1,3\\}$" in page,
    ]
    assert all(checks), [index for index, passed in enumerate(checks, 1) if not passed]
    print(f"event arithmetic: {len(checks)} checks passed")
