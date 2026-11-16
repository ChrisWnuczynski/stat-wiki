"""Exact checks for every numerical claim in the irreducible-chain example."""

from pathlib import Path

import sympy as sp


def main() -> None:
    article = (Path(__file__).resolve().parents[1] / "articles/irreducible-markov-chain.qmd").read_text()
    P = sp.Matrix(
        [
            [0, 1, 0],
            [sp.Rational(1, 2), 0, sp.Rational(1, 2)],
            [sp.Rational(1, 2), sp.Rational(1, 2), 0],
        ]
    )
    assert all(sum(P.row(i)) == 1 for i in range(3))
    assert P**2 == sp.Matrix(
        [
            [sp.Rational(1, 2), 0, sp.Rational(1, 2)],
            [sp.Rational(1, 4), sp.Rational(3, 4), 0],
            [sp.Rational(1, 4), sp.Rational(1, 2), sp.Rational(1, 4)],
        ]
    )
    assert P[0, 1] * P[1, 2] == sp.Rational(1, 2)
    assert P[2, 0] == sp.Rational(1, 2)
    assert (P**2)[1, 1] == sp.Rational(3, 4)
    assert P[1, 0] * P[0, 1] == sp.Rational(1, 2)
    assert P[1, 2] * P[2, 1] == sp.Rational(1, 4)
    pi = sp.Matrix([[sp.Rational(1, 3), sp.Rational(4, 9), sp.Rational(2, 9)]])
    assert pi * P == pi and sum(pi) == 1
    assert pi[0, 1] * P[1, 2] == sp.Rational(2, 9)
    assert (P**2)[0, 0] > 0 and (P**3)[0, 0] > 0
    assert sp.gcd(2, 3) == 1
    reach = sp.zeros(3)
    for n in range(4):
        for i in range(3):
            for j in range(3):
                if (P**n)[i, j] > 0:
                    reach[i, j] = 1
    assert reach == sp.ones(3)
    for printed in (
        "1/2&0&1/2",
        "1/4&3/4&0",
        "1/4&1/2&1/4",
        "(1/3,4/9,2/9)",
        "$(P^2)_{22}=3/4$",
    ):
        assert printed in article, f"Missing worked value: {printed}"
    print("irreducible-markov-chain arithmetic: 13 checks passed")


if __name__ == "__main__":
    main()
