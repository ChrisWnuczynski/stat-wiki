"""Arithmetic checks for the Newton–Raphson article."""

import math
from pathlib import Path

root = Path(__file__).resolve().parents[1]
prose = (root / "research/content/newton-raphson-method.md").read_text(encoding="utf-8")
article = root / "articles/newton-raphson-method.qmd"
built = article.read_text(encoding="utf-8") if article.is_file() else ""
page = built if "Your turn" in built else prose


def require(text: str) -> None:
    assert text in prose, text
    assert text in page, text


def logistic(beta):
    return 1 / (1 + math.exp(-beta))


def step(beta, n=4, y=1):
    p = logistic(beta)
    score = y - n * p
    hessian = -n * p * (1 - p)
    return beta - score / hessian, p, score


beta1, p0, u0 = step(0.0)
assert abs(p0 - 0.5) < 1e-12 and abs(u0 + 1) < 1e-12 and abs(beta1 + 1) < 1e-12
beta2, p1, u1 = step(beta1)
assert abs(p1 - 1 / (1 + math.e)) < 1e-12
assert abs(u1 - (1 - 4 / (1 + math.e))) < 1e-12
_, p2, u2 = step(beta2)
mle = math.log(1 / 3)
assert abs(mle - math.log(0.25 / 0.75)) < 1e-12
assert abs(beta2 - mle) < 0.003

# Quadratic log-likelihood finishes in one step.
b, c = 4.0, -2.0
for start in (-3.0, 0.0, 2.5):
    critical = -b / (2 * c)
    landed = start - (b + 2 * c * start) / (2 * c)
    assert abs(landed - critical) < 1e-12

require("-1")
require("0.268941")
require("-0.075766")
require("-1.096339")
require("-1.098612")
require("0.250426")
require("-0.001706")
assert f"{p1:.6f}" == "0.268941"
assert f"{u1:.6f}" == "-0.075766"
assert f"{beta2:.6f}" == "-1.096339"
assert f"{mle:.6f}" == "-1.098612"
assert f"{p2:.6f}" == "0.250426"
assert f"{u2:.6f}" == "-0.001706"
print("newton-raphson-method checks passed")
