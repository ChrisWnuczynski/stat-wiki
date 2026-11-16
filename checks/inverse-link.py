"""Check reciprocal-link calculations, domain examples and page structure."""

from math import isclose, sqrt
from pathlib import Path

root = Path(__file__).resolve().parents[1]
page = (root / "articles/inverse-link.qmd").read_text()
body = page.split("## See also", 1)[0]

def mean(eta):
    assert eta > 0
    return 1 / eta

assert mean(.25) == 4
assert mean(.05) == 20
assert isclose(mean(1 / 20) / mean(1 / 10), 2)
assert mean(.5 - .1 * 4) == 10 or isclose(mean(.5 - .1 * 4), 10)
assert isclose(.5 - .1 * 5, 0, abs_tol=1e-12)
assert isclose(.5 - .1 * 6, -.1)
assert isclose(1 / (.5 - .1 * 6), -10)

eta10 = .02 + .003 * 10
eta20 = .02 + .003 * 20
assert isclose(eta10, .05) and isclose(eta20, .08)
assert isclose(mean(eta10), 20) and isclose(mean(eta20), 12.5)
assert isclose(mean(eta20) - mean(eta10), -7.5)
assert isclose(-.003 / eta10**2, -1.2)
assert isclose(mean(.02), 50)

eta5 = .04 + .002 * 5
eta15 = .04 + .002 * 15
assert isclose(eta5, .05) and isclose(eta15, .07)
assert isclose(mean(eta5), 20)
assert isclose(mean(eta15), 100 / 7)
assert round(mean(eta15), 3) == 14.286
assert isclose(mean(eta15) / mean(eta5), 5 / 7)
assert round(mean(eta15) / mean(eta5), 4) == .7143
assert isclose(-.002 / eta5**2, -.8)
assert isclose(1 / sqrt(.04), 5)

for fragment in (
    "## Motivating example", "## Worked example", "**Your turn.**",
    'title="Proof"', 'title="Answer"', "## Common misconceptions",
    "14.286", "0.7143", "-1.2", "-0.8", "## Assumptions and limits",
):
    assert fragment in body, f"Missing section or calculation: {fragment}"
assert body.count('title="Proof"') == 1
for qid in ("q-36", "q-38", "q-57", "ex-cholesterol-gam", "c-17"):
    assert f"../questions/{qid}.qmd" in page
print("inverse-link reciprocal, derivative and domain calculations passed")
