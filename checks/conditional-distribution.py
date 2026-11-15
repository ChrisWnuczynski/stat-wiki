"""Exact discrete checks for the conditional-distribution examples."""

from fractions import Fraction
from math import isclose, log, sqrt


if __name__ == "__main__":
    points = [(x, y) for y in range(1, 5) for x in range(1, y + 1)]
    ex = Fraction(sum(x for x, _ in points), len(points))
    ey = Fraction(sum(y for _, y in points), len(points))
    exy = Fraction(sum(x * y for x, y in points), len(points))
    vx = Fraction(sum(x * x for x, _ in points), len(points)) - ex * ex
    vy = Fraction(sum(y * y for _, y in points), len(points)) - ey * ey
    joint = {
        (0, 0): Fraction(1, 10),
        (0, 1): Fraction(2, 10),
        (1, 0): Fraction(3, 10),
        (1, 1): Fraction(4, 10),
    }
    px0 = joint[0, 0] + joint[0, 1]
    px1 = joint[1, 0] + joint[1, 1]
    py0 = joint[0, 0] + joint[1, 0]
    py1 = joint[0, 1] + joint[1, 1]
    checks = [
        len(points) == 10,
        ex == 2,
        ey == 3,
        exy == Fraction(13, 2),
        vx == 1,
        vy == 1,
        exy - ex * ey == Fraction(1, 2),
        Fraction(sum(y for x, y in points if x == 2), 3) == 3,
        px0 == Fraction(3, 10),
        px1 == Fraction(7, 10),
        joint[0, 1] / px0 == Fraction(2, 3),
        joint[1, 1] / px1 == Fraction(4, 7),
        px0 * Fraction(2, 3) + px1 * Fraction(4, 7) == py1 == Fraction(3, 5),
        joint[1, 0] / py0 == Fraction(3, 4),
        sum(joint.values()) == 1,
        20 * 30 == 600,
        20 * 100 + 20 * 900 == 20_000,
        isclose(sqrt(20_000), 141.4213562373095),
        isclose(sqrt(2000), 44.721359549995796),
        isclose(-log(Fraction(1, 2)), log(2)),
    ]
    assert all(checks)
    print(f"conditional-distribution arithmetic: {len(checks)} checks passed")
