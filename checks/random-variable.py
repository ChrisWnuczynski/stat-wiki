"""Enumerate the coin and dice examples in the random-variable article."""

from fractions import Fraction
from itertools import product


if __name__ == "__main__":
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
    ]
    assert all(checks)
    print(f"random-variable arithmetic: {len(checks)} checks passed")
