"""Check random-intercept covariance, pooling and predictive calculations."""

from math import isclose
from pathlib import Path

root = Path(__file__).resolve().parents[1]
page = (root / "articles/random-intercept-model.qmd").read_text()
body = page.split("## See also", 1)[0]

tau2, sigma2, m = 9, 16, 2
rho = tau2 / (tau2 + sigma2)
assert rho == .36
assert tau2 + sigma2 == 25
assert tau2 + sigma2 / m == 17
w = tau2 / (tau2 + sigma2 / m)
assert isclose(w, 9 / 17) and round(w, 4) == .5294
assert (110 + 114) / 2 == 112
assert 112 - 100 == 12
effect = 12 * w
assert isclose(effect, 108 / 17) and round(effect, 4) == 6.3529
assert round(100 + effect, 4) == 106.3529
post_var = 1 / (1 / tau2 + m / sigma2)
assert isclose(post_var, 72 / 17) and round(post_var, 4) == 4.2353
assert round(sigma2 + post_var, 4) == 20.2353

tau2, sigma2, m = 4, 9, 3
w = tau2 / (tau2 + sigma2 / m)
assert isclose(w, 4 / 7) and round(w, 4) == .5714
assert isclose(3 * w, 12 / 7) and round(3 * w, 4) == 1.7143
assert round(50 + 3 * w, 4) == 51.7143
assert isclose(tau2 / (tau2 + sigma2), 4 / 13)
assert round(tau2 / (tau2 + sigma2), 4) == .3077

assert isclose(-1 / (3 - 1), -.5)
assert isclose(1 + (3 - 1) * -.5, 0)
assert isclose(1 + (4 - 1) * .36, 2.08)

for fragment in (
    "## Motivating example", "## Worked example", "**Your turn.**",
    'title="Proof"', 'title="Answer"', "## Common misconceptions",
    "0.5294", "6.3529", "106.3529", "20.2353", "51.7143",
    "08-random-intercepts-shared-intercept.png", "## Assumptions and limits",
):
    assert fragment in body, f"Missing section or calculation: {fragment}"
assert body.count('title="Proof"') == 1
for qid in ("q-39", "q-40", "q-41", "ex-toenail-glmm", "ex-orthodont-lmm", "c-35"):
    assert f"../questions/{qid}.qmd" in page
print("random-intercept covariance and pooling calculations passed")
