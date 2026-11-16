"""Numerical claims in credible-region constructions, including inherited examples."""
import math
from pathlib import Path


def test_printed_values():
    page = (Path(__file__).resolve().parents[1] / "articles" / "credible-region-constructions.qmd").read_text()
    assert "{#worked-example}" in page and "Your turn" in page
    # Existing definitions and posterior-draw summary.
    assert math.isclose(.025 + .95 + .025, 1)
    assert 500 + 501 == 1001
    assert (25 / 1000, 975 / 1000) == (.025, .975)

    # Existing increasing-density question, whose CDF is F(t)=t^2.
    assert math.isclose(.125 + .75 + .125, 1)
    assert math.isclose(math.sqrt(1/8)**2, .125)
    assert math.isclose(math.sqrt(7/8)**2, .875)
    assert math.isclose(1 - .5**2, .75)
    assert math.isclose((1 - .5), .5)

    # Existing tank-production example: max data value, posterior parameters,
    # mean, and 95% upper endpoint.
    data = (19, 40, 42, 60)
    assert (len(data), max(data), max(50, max(data))) == (4, 60, 60)
    shape, scale = 1 + len(data), max(50, max(data))
    assert (shape, scale) == (5, 60)
    assert shape * scale / (shape - 1) == 75
    upper = scale * 20**(1/shape)
    assert round(upper, 1) == 109.2
    assert math.isclose(1 - (scale/upper)**shape, .95)
    assert math.isclose(1/(shape+1), 1/6)

    # New rate-two exponential example.
    lo, hi = -math.log(.95)/2, -math.log(.05)/2
    hpd_hi = -math.log(.10)/2
    assert (round(lo, 5), round(hi, 5)) == (.02565, 1.49787)
    assert round(hpd_hi, 5) == 1.15129
    assert math.isclose((1-math.exp(-2*hi))-(1-math.exp(-2*lo)), .90)
    assert math.isclose(1-math.exp(-2*hpd_hi), .90)
    assert hpd_hi < hi-lo

    # New practice rate-one exponential example.
    lo, hi = -math.log(.90), -math.log(.10)
    hpd_hi = -math.log(.20)
    assert (round(lo, 5), round(hi, 5)) == (.10536, 2.30259)
    assert round(hpd_hi, 5) == 1.60944
    assert math.isclose((1-math.exp(-hi))-(1-math.exp(-lo)), .80)
    assert math.isclose(1-math.exp(-hpd_hi), .80)

    # Proposed bank item on discrete posterior mass and minimum cardinality.
    probs = {1: .50, 2: .30, 3: .20}
    assert math.isclose(sum(probs.values()), 1)
    assert math.isclose(probs[1] + probs[2], .80)
    assert max(probs.values()) < .80


if __name__ == "__main__":
    test_printed_values()
