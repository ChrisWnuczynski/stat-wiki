"""Numeric comparisons printed on the Bayesian information criterion page."""
import math
from pathlib import Path


def bic(loglik, dimension, n):
    return -2 * loglik + dimension * math.log(n)


def test_printed_values():
    page = (Path(__file__).resolve().parents[1] / "articles" / "bayesian-information-criterion.qmd").read_text()
    assert "{#worked-example}" in page and "Your turn" in page
    # Inherited comparison of BIC and AIC at n=100.
    assert round(math.log(100), 3) == 4.605
    b1, b2 = bic(-140, 2, 100), bic(-136, 5, 100)
    assert round(b1, 2) == 289.21
    assert round(b2, 2) == 295.03
    assert b1 < b2
    assert -2*(-140)+2*2 == 284
    assert -2*(-136)+2*5 == 282
    assert 2*2 == 4 and 2*5 == 10

    # New near tie: two free parameters cost log(150) log-likelihood units.
    b1, b2 = bic(-210, 2, 150), bic(-205, 4, 150)
    assert round(math.log(150), 6) == 5.010635
    assert round(b1, 4) == 430.0213
    assert round(b2, 4) == 430.0425
    assert round(b2-b1, 4) == .0213
    assert -205-(-210) == 5
    assert 5 < math.log(150)

    # Your turn: larger candidate gains seven log-likelihood units.
    b1, b2 = bic(-500, 3, 400), bic(-493, 5, 400)
    assert round(math.log(400), 6) == 5.991465
    assert round(b1, 3) == 1017.974
    assert round(b2, 3) == 1015.957
    assert round(b1-b2, 3) == 2.017
    assert -493-(-500) == 7
    assert 7 > math.log(400)

    # Distinct row and trial counts in a grouped binomial likelihood.
    assert 20*50 == 1000
    assert math.log(20) != math.log(1000)


if __name__ == "__main__":
    test_printed_values()
