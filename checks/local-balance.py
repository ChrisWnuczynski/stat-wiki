"""Printed-value checks for local balance."""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROSE = (ROOT / "research" / "content" / "local-balance.md").read_text(encoding="utf-8")


def weights(lam, mu):
    w = [Fraction(1)]
    for n, birth in enumerate(lam):
        w.append(w[-1] * Fraction(birth) / Fraction(mu[n]))
    return w


def main() -> None:
    w = weights([1, 1, 0], [2, 2, 1])
    # deaths used are μ1, μ2; the extra μ is unused because λ2=0 stops the next weight's birth
    assert w[:3] == [Fraction(1), Fraction(1, 2), Fraction(1, 4)]
    total = sum(w[:3])
    assert total == Fraction(7, 4)
    pi = [weight / total for weight in w[:3]]
    assert pi == [Fraction(4, 7), Fraction(2, 7), Fraction(1, 7)]
    assert pi[0] * 1 == pi[1] * 2 == Fraction(4, 7)
    assert pi[1] * 1 == pi[2] * 2 == Fraction(2, 7)
    w2 = weights([2, 2, 0], [2, 2, 1])
    assert w2[:3] == [1, 1, 1]
    assert pi[2] / pi[1] == Fraction(1, 2)
    for token in ("4/7", "2/7", "1/7", "7/4", "1/3"):
        assert token in PROSE, token
    article = ROOT / "articles" / "local-balance.qmd"
    if article.is_file():
        body = article.read_text(encoding="utf-8")
        assert "4/7" in body and "7/4" in body
    print("local-balance checks passed")


if __name__ == "__main__":
    main()
