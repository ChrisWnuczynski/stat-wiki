"""Exact checks for the conditional-expectation examples."""

from fractions import Fraction
from pathlib import Path


def expectation(pairs):
    return sum(y * p for _, y, p in pairs)


if __name__ == "__main__":
    article = (Path(__file__).resolve().parents[1] / "articles/conditional-expectation.qmd").read_text()
    assert r"m(x)=\frac{\int y\,f(x,y)\,\mathrm dy}{\int f(x,y)\,\mathrm dy}" in article
    for printed in (r"\frac54", r"\tfrac98", "19/32", "1/64", "39/64", r"\tfrac{27}{4}", "4/3", "6/5"):
        assert printed in article, f"Worked value missing from article: {printed}"
    joint = [
        (0, 0, Fraction(1, 8)),
        (0, 1, Fraction(2, 8)),
        (0, 2, Fraction(1, 8)),
        (1, 0, Fraction(1, 8)),
        (1, 1, Fraction(1, 8)),
        (1, 2, Fraction(2, 8)),
    ]
    assert sum(p for _, _, p in joint) == 1
    px = {0: sum(p for x, _, p in joint if x == 0), 1: sum(p for x, _, p in joint if x == 1)}
    assert px == {0: Fraction(1, 2), 1: Fraction(1, 2)}

    def cond_mean(x):
        return sum(y * p for xx, y, p in joint if xx == x) / px[x]

    assert cond_mean(0) == 1
    assert cond_mean(1) == Fraction(5, 4)
    tower = sum(cond_mean(x) * px[x] for x in px)
    ey = expectation(joint)
    assert tower == ey == Fraction(9, 8)

    def cond_second(x):
        return sum(y * y * p for xx, y, p in joint if xx == x) / px[x]

    var0 = cond_second(0) - cond_mean(0) ** 2
    var1 = cond_second(1) - cond_mean(1) ** 2
    assert var0 == Fraction(1, 2)
    assert var1 == Fraction(11, 16)
    mean_var = var0 * px[0] + var1 * px[1]
    var_mean = sum((cond_mean(x) - ey) ** 2 * px[x] for x in px)
    assert mean_var == Fraction(19, 32)
    assert var_mean == Fraction(1, 64)
    assert mean_var + var_mean == Fraction(39, 64)

    mu_y, sigma_x, sigma_y, rho, x = 1, 2, 3, Fraction(1, 2), 4
    cond = mu_y + rho * sigma_y / sigma_x * (x - 0)
    cond_var = sigma_y ** 2 * (1 - rho ** 2)
    assert cond == 4
    assert cond_var == Fraction(27, 4)

    exercise = [
        (0, 0, Fraction(1, 5)),
        (0, 2, Fraction(2, 5)),
        (1, 1, Fraction(2, 5)),
    ]
    assert sum(p for _, _, p in exercise) == 1
    ex = {
        0: sum(y * p for x, y, p in exercise if x == 0) / Fraction(3, 5),
        1: sum(y * p for x, y, p in exercise if x == 1) / Fraction(2, 5),
    }
    assert ex[0] == Fraction(4, 3)
    assert ex[1] == 1
    assert ex[0] * Fraction(3, 5) + ex[1] * Fraction(2, 5) == expectation(exercise) == Fraction(6, 5)

    xs = (0, 1, 2, 3)
    ys = (1, 1, 3, 3)
    n = len(xs)
    xbar = Fraction(sum(xs), n)
    ybar = Fraction(sum(ys), n)
    sxx = sum((x - xbar) ** 2 for x in xs)
    syx = sum((x - xbar) * (y - ybar) for x, y in zip(xs, ys))
    slope = syx / sxx
    # Normal equations for a + b x.
    # Sum of residuals zero and weighted by x.
    def sse(a, b):
        return sum((y - a - b * x) ** 2 for x, y in zip(xs, ys))

    a = ybar - slope * xbar
    assert slope == Fraction(4, 5)
    assert sse(a, slope) < sse(a, slope + 1)
    assert sse(a, slope) < sse(a + 1, slope)

    checks = [
        cond_mean(0) == 1,
        cond_mean(1) == Fraction(5, 4),
        tower == Fraction(9, 8),
        mean_var + var_mean == Fraction(39, 64),
        cond == 4,
        cond_var == Fraction(27, 4),
        ex[0] == Fraction(4, 3),
        expectation(exercise) == Fraction(6, 5),
        slope == Fraction(4, 5),
        var_mean == Fraction(1, 64),
    ]
    assert all(checks)
    print(f"conditional-expectation arithmetic: {len(checks)} checks passed")
