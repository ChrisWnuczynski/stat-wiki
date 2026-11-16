"""Verify Metropolis–Hastings numeric examples and retained page features."""

from fractions import Fraction as F
from math import e, exp, log, pi, sqrt
from pathlib import Path

from scipy.integrate import quad
from scipy.optimize import brentq
from scipy.special import expit

root = Path(__file__).resolve().parents[1]
page = (root / "articles/metropolis-hastings-update.qmd").read_text()
body = page.split("## See also", 1)[0]

target = (F(7, 10), F(3, 10))
forward, reverse = F(4, 5), F(1, 5)
ratio = target[1] * reverse / (target[0] * forward)
assert ratio == F(3, 28)
assert round(float(ratio), 6) == 0.107143
p01, p10 = forward * ratio, reverse
assert p01 == F(3, 35) and round(float(p01), 6) == 0.085714
assert 1 - p01 == F(32, 35) and 1 - p10 == F(4, 5)
assert target[0] * p01 == target[1] * p10 == F(3, 50)

target2 = (F(1, 4), F(3, 4))
forward2, reverse2 = F(2, 5), F(3, 5)
ratio2 = target2[1] * reverse2 / (target2[0] * forward2)
assert ratio2 == F(9, 2)
assert 1 / ratio2 == F(2, 9)
assert reverse2 / ratio2 == F(2, 15)
assert round(float(F(2, 15)), 6) == 0.133333
assert target2[0] * forward2 == target2[1] * F(2, 15) == F(1, 10)

# The inherited symmetric random-walk example targets x^2 exp(-x).
assert round(9 / (4 * e), 3) == 0.828
assert 4 * e / 9 > 1

# Independent quadrature checks the inherited analytic logit-normal summaries.
def posterior_summary(n, x):
    center = x / n
    offset = (x - 1) * log(center) + (n - x - 1) * log(1 - center)

    def density(t):
        if t <= 0 or t >= 1:
            return 0.0
        value = (x - 1) * log(t) + (n - x - 1) * log(1 - t)
        value -= 0.5 * (log(t / (1 - t)) - 1) ** 2
        return exp(value - offset)

    total = quad(density, 0, 1, epsabs=1e-11)[0]
    mean = quad(lambda t: t * density(t), 0, 1, epsabs=1e-11)[0] / total
    quantiles = tuple(brentq(lambda v: quad(density, 0, v, epsabs=1e-11)[0] / total - p,
                             1e-8, 1 - 1e-8) for p in (0.025, 0.975))
    return mean, quantiles

mean40, interval40 = posterior_summary(40, 16)
mean400, interval400 = posterior_summary(400, 160)
prior_mean = quad(lambda z: expit(z) * exp(-0.5 * (z - 1) ** 2) / sqrt(2 * pi),
                  -10, 12)[0]
assert round(mean40, 4) == 0.4320
assert tuple(round(v, 3) for v in interval40) == (0.291, 0.579)
assert round(mean400, 4) == 0.4035
assert tuple(round(v, 3) for v in interval400) == (0.356, 0.452)
assert round(prior_mean, 4) == 0.6967

for printed in ("3}{28", "0.107143", "3/35", "0.085714", "32/35",
                "0.06", "4.5", "2/9", "2/15", "0.133333", "0.1=",
                "0.828", "0.4320", "0.291", "0.579", "0.4035",
                "0.356", "0.452", "0.6967", "0.294", "0.578",
                "0.355", "0.453"):
    assert printed in body, f"missing printed number: {printed}"
assert body.count('title="Proof"') == 1
assert "## Motivating example" in body and "## Worked example" in body
assert "**Your turn.**" in body and 'title="Answer"' in body
assert "{#assumptions-and-limits}" in body
assert "part1-fig-04-proposal-scale.png" in page
for qid in ("q-05", "q-10", "ex-applied-logitnormal-mh"):
    assert f"#example-{qid}" in body
for qid in ("c-14", "q-19", "ex-gibbs-mh"):
    assert "Worked answer" in (root / f"questions/{qid}.qmd").read_text()
print("Metropolis–Hastings numbers and structure passed")
