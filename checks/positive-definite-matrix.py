"""Check positive-definiteness examples and their printed values."""

from fractions import Fraction
from pathlib import Path


PAGE = Path(__file__).resolve().parents[1] / "articles" / "positive-definite-matrix.qmd"


def quadratic(a, matrix):
    return sum(a[i] * matrix[i][j] * a[j]
               for i in range(len(a)) for j in range(len(a)))


def det3(m):
    return (m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
            - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
            + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0]))


if __name__ == "__main__":
    page = PAGE.read_text(encoding="utf-8")
    a = ((2, 1), (1, 2))
    b = ((1, 2), (2, 1))
    r = Fraction(9, 10)
    impossible = ((1, r, r), (r, 1, -r), (r, -r, 1))
    checks = [
        a[0][0] == 2,
        a[0][0] * a[1][1] - a[0][1] * a[1][0] == 3,
        quadratic((1, 1), a) == 6,
        quadratic((1, -1), a) == 2,
        quadratic((0, 1), a) == 2,
        a[0][1] / Fraction(2, 1) == Fraction(1, 2),
        b[0][0] * b[1][1] - b[0][1] * b[1][0] == -3,
        quadratic((1, -1), b) == -2,
        quadratic((0, 1), ((0, 0), (0, -1))) == -1,
        1 - r * r == Fraction(19, 100),
        det3(impossible) == Fraction(-361, 125),
        quadratic((1, -1, -1), impossible) < 0,
        quadratic((1, -1), ((3, 1), (1, 3))) == 4,
        "$\\det A=3$" in page,
        "eigenvalues are $1$ and $3$" in page,
        "correlation $1/2$" in page,
        "$1-4=-3<0$" in page,
        "$\\mathbf a^\\top B\\mathbf a=-2$" in page,
        "leading minors $0$ and $0$" in page,
    ]
    assert all(checks), [index for index, passed in enumerate(checks, 1) if not passed]
    print(f"positive-definite-matrix arithmetic: {len(checks)} checks passed")
