"""Exact checks for a conditionally independent, marginally dependent pair."""

from fractions import Fraction


if __name__ == "__main__":
    # Z is fair. Given Z=z, X and Y are independent Bernoulli draws.
    p = {0: Fraction(1, 4), 1: Fraction(3, 4)}
    pz = Fraction(1, 2)

    def joint(x, y):
        return sum(pz * p[z] ** (x + y) * (1 - p[z]) ** (2 - x - y) for z in (0, 1))

    p_x1 = sum(joint(1, y) for y in (0, 1))
    p_y1 = sum(joint(x, 1) for x in (0, 1))
    p_both = joint(1, 1)
    assert p_x1 == Fraction(1, 2)
    assert p_y1 == Fraction(1, 2)
    assert p_both == Fraction(5, 16)
    assert p_x1 * p_y1 == Fraction(1, 4)
    assert p_both != p_x1 * p_y1
    assert p_both / p_y1 == Fraction(5, 8)

    # Given Z=0, Y does not change the conditional law of X.
    assert p[0] == Fraction(1, 4)
    # P(X=1, Y=1, Z=0) / P(Y=1, Z=0) = p[0].
    p_y1_z0 = pz * p[0]
    p_x1_y1_z0 = pz * p[0] * p[0]
    assert p_x1_y1_z0 / p_y1_z0 == p[0]

    checks = [
        p_x1 == Fraction(1, 2),
        p_both == Fraction(5, 16),
        p_both / p_y1 == Fraction(5, 8),
        p_x1_y1_z0 / p_y1_z0 == Fraction(1, 4),
        joint(0, 0) == pz * ((Fraction(3, 4)) ** 2 + (Fraction(1, 4)) ** 2),
        p_both - p_x1 * p_y1 == Fraction(1, 16),
        p[1] == Fraction(3, 4),
        pz * 2 == 1,
        joint(1, 0) == joint(0, 1),
        joint(0, 0) + joint(0, 1) + joint(1, 0) + joint(1, 1) == 1,
    ]
    assert all(checks)
    print(f"conditional-independence arithmetic: {len(checks)} checks passed")
