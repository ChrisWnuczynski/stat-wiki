"""Recompute the inherited and new Gaussian-kernel density examples."""

from math import exp, pi, sqrt
from pathlib import Path

root = Path(__file__).resolve().parents[1]
page = (root / "articles/kernel-density-estimator.qmd").read_text()
body = page.split("## See also", 1)[0]


def phi(z):
    return exp(-z * z / 2) / sqrt(2 * pi)


def kde(xs, x, h):
    return sum(phi((x - xi) / h) for xi in xs) / (len(xs) * h)


assert round(phi(0), 8) == .39894228
assert round(phi(1), 6) == .241971
assert round(phi(2), 8) == .05399097
assert round(phi(.5), 6) == .352065

# Inherited three-point example and the value at x=2.
inherited = (-1, 0, 2)
assert round(kde(inherited, 0, 1), 3) == .232
assert round(kde(inherited, 2, 1), 3) == .152
assert 1 / .2 == 5
assert 3 * (3 + 1) / 2 == 6  # matrix-bandwidth free entries for p=3

# New worked example with a repeated zero.
worked = (0, 0, 2)
assert round(kde(worked, 0, 1), 8) == .28395851
assert round(kde(worked, 0, 2), 6) == .173309
assert round(2 * phi(0), 6) == .797885  # exact intermediate before rounded display
assert round(2 * .398942, 6) == .797884  # printed approximation

# Hidden practice at the midpoint of two observations.
practice = (0, 2)
assert round(kde(practice, 1, 1), 6) == .241971
assert round(kde(practice, 1, 2), 6) == .176033

for fragment in (
    "## Motivating example", "## Worked example", "**Your turn.**",
    'title="Proof"', 'title="Answer"', "0.39894228", "0.05399097",
    "0.28395851", "0.173309", "0.241971", "0.176033",
    "0.232", "0.152", "## Common misconceptions", "#assumptions-and-limits",
    "../labs/kernel-density.qmd",
):
    assert fragment in body, f"Missing content or calculation: {fragment}"

assert body.count('title="Proof"') == 1
for qid in ("ex-sl-07-5", "ex-sl-07-6", "ex-sl-17-10"):
    assert f"../questions/{qid}.qmd" in page
print("kernel density calculations, lab and inherited links passed")
