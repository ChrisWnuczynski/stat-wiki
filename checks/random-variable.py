"""Enumerate the coin and dice examples in the random-variable article."""

from fractions import Fraction
from itertools import product
from pathlib import Path


PAGE = Path(__file__).resolve().parents[1] / "articles" / "random-variable.qmd"


if __name__ == "__main__":
    page = PAGE.read_text(encoding="utf-8")
    coin_space = list(product((0, 1), repeat=2))
    heads = {outcome: sum(outcome) for outcome in coin_space}
    first_head = {outcome: outcome[0] for outcome in coin_space}
    dice_space = list(product(range(1, 7), repeat=2))
    sums = {outcome: sum(outcome) for outcome in dice_space}
    high = {outcome: int(total >= 10) for outcome, total in sums.items()}
    checks = [
        len(coin_space) == 4,
        sum(heads[o] == 1 for o in coin_space) == 2,
        Fraction(sum(heads[o] <= 1 for o in coin_space), 4) == Fraction(3, 4),
        Fraction(sum(heads.values()), 4) == 1,
        Fraction(sum(first_head[o] == 1 and heads[o] == 2 for o in coin_space), 4)
        == Fraction(1, 4),
        Fraction(sum(first_head.values()), 4) * Fraction(sum(heads[o] == 2 for o in coin_space), 4)
        == Fraction(1, 8),
        len(dice_space) == 36,
        sum(total == 7 for total in sums.values()) == 6,
        sum(total <= 4 for total in sums.values()) == 6,
        Fraction(sum(sums.values()), 36) == 7,
        sum(high.values()) == 6,
        all(high[o] == int(sums[o] >= 10) for o in dice_space),
        {o for o in dice_space if sums[o] >= 11} == {(5, 6), (6, 5), (6, 6)},
        Fraction(sum(total >= 11 for total in sums.values()), 36) == Fraction(1, 12),
        Fraction(sum(high.values()), 36) == Fraction(1, 6),
        "$1/4$" in page,
        "$1/2$" in page,
        "$3/4$" in page,
        "=1/8$" in page,
        "$\\mathbb P(X=7)=6/36=1/6$" in page,
        "$F_X(4)=\\mathbb P(X\\le4)=6/36=1/6$" in page,
        "$\\mathbb E X=7$" in page,
        "$\\mathbb P(Y=1)=6/36=1/6$" in page,
        "$\\mathbb P(X\\ge11)=3/36=1/12$" in page,
    ]
    assert all(checks), [index for index, passed in enumerate(checks, 1) if not passed]
    print(f"random-variable arithmetic: {len(checks)} checks passed")
