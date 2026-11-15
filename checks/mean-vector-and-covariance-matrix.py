"""Recompute the page's population and sample covariance examples."""

from fractions import Fraction
from math import isclose, sqrt


if __name__ == "__main__":
    pairs = ((1, 2), (3, 4), (5, 0))
    mean = tuple(Fraction(sum(row[j] for row in pairs), len(pairs)) for j in range(2))
    centered = tuple((x - mean[0], y - mean[1]) for x, y in pairs)
    s00 = sum(x * x for x, _ in centered) / 2
    s01 = sum(x * y for x, y in centered) / 2
    s11 = sum(y * y for _, y in centered) / 2
    contrasts = tuple(x - y for x, y in pairs)
    sums = tuple(x + y for x, y in pairs)
    checks = [
        mean == (3, 2),
        centered == ((-2, 0), (0, 2), (2, -2)),
        s00 == 4,
        s01 == -2,
        s11 == 4,
        contrasts == (-1, -1, 5),
        sum((x - 1) ** 2 for x in contrasts) / 2 == 12,
        s00 + s11 - 2 * s01 == 12,
        sum((x - 5) ** 2 for x in sums) / 2 == 4,
        s00 + s11 + 2 * s01 == 4,
        isclose(2 / sqrt(4 * 9), 1 / 3),
        4 + 9 - 2 * 2 == 9,
        10 * 10 * 4 == 400,
        10 * 2 == 20,
        4 + 9 == 13,
    ]
    assert all(checks)
    print(f"mean-vector-and-covariance-matrix arithmetic: {len(checks)} checks passed")
