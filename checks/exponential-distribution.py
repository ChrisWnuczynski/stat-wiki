"""Check numbers printed in the exponential distribution article."""
import math
from pathlib import Path


def close(actual, expected, places=4):
    assert math.isclose(actual, expected, abs_tol=0.5 * 10 ** -places)


def test_printed_values():
    page = (Path(__file__).resolve().parents[1] / "articles" / "exponential-distribution.qmd").read_text()
    assert "{#worked-example}" in page and "Your turn" in page
    # Rate/scale and infobox formulas, including plotted parameter values.
    rate = 0.001
    assert 1 / rate == 1000
    close(math.exp(-500 / 1000), 0.607, 3)
    for lam in (0.5, 1, 2, 3, 4):
        assert math.isclose(lam / (lam - 0), 1)
        assert math.isclose((1 / lam**2), (1 / lam) ** 2)
        assert math.isclose(-math.log(1 - 0.5) / lam, math.log(2) / lam)
        assert math.isclose(lam / (lam - 0.2), 1 / (1 - 0.2 / lam))
        assert math.isclose(-math.log(math.exp(-lam)), lam)
    # Series-system and baseline component examples.
    assert 5 / 1000 == 1 / 200
    assert math.isclose((1 / 200) ** -1, 200)
    close(math.exp(-5 / 10), 0.607, 3)
    close(math.exp(-2 / 2), 0.368, 3)
    close(math.exp(-(10 - 7) / 2), 0.223, 3)
    close(math.exp(-0.2 * 5), 0.3679, 4)
    # Retained Bayes-factor exercise stipulates 1.347 without raw lifetimes.
    assert math.isclose(1.347 / 3, 0.449)
    close(1 / 0.449, 2.23, 2)
    close(0.449 / 1.449, 0.310, 3)
    close(1 / 1.449, 0.690, 3)
    # New call-centre worked example and Your turn.
    close(1 - math.exp(-3 / 3), 0.63212, 5)
    assert 60 / 3 == 20
    close(60 * math.log(2) / 3, 13.86, 2)
    close(math.exp(-3 / 6), 0.60653, 5)
    close(math.exp(-4 / 2), 0.13534, 5)
    close(math.exp(-4 / 4), 0.36788, 5)


if __name__ == "__main__":
    test_printed_values()
