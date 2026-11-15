"""Exact discrete checks for the conditional-distribution examples."""

from fractions import Fraction
from math import isclose, log, sqrt
from pathlib import Path


PAGE = Path(__file__).resolve().parents[1] / "articles" / "conditional-distribution.qmd"


if __name__ == "__main__":
    page = PAGE.read_text(encoding="utf-8")
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
        "10 lattice points" in page,
        "$1/10$" in page,
        "$\\mathbb{E} X=2$" in page,
        "$\\mathbb{E}(XY)=13/2$" in page,
        "$\\rho(X,Y)=1/2$" in page,
        "=30\\times20=600$" in page,
        "=20000," in page,
        "standard deviation is $141$" in page,
        "$\\sqrt{2000}=45$" in page,
        "=(2/10)/(3/10)=2/3$" in page,
        "=(4/10)/(7/10)=4/7$" in page,
        "=6/10=\\mathbb P(Y=1)$" in page,
        "=(3/10)/(4/10)=3/4$" in page,
        "f_{Y\\mid X}(y\\mid x)=1/x$" in page,
        "f_Y(y)=\\int_y^1\\frac{\\,\\mathrm{d} x}x=-\\log y" in page,
    ]
    assert all(checks), [index for index, passed in enumerate(checks, 1) if not passed]
    print(f"conditional-distribution arithmetic: {len(checks)} checks passed")
