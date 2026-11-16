"""Check held-out error estimates, intervals and generated practice."""

import math
from pathlib import Path


root = Path(__file__).resolve().parents[1]
page = (root / "articles/a-held-out-test-set.qmd").read_text()
body = page.split("## See also", 1)[0]


def wald(error_count, n):
    p = error_count / n
    se = math.sqrt(p * (1 - p) / n)
    return p, se, (p - 1.96 * se, p + 1.96 * se)


# Inherited test-size example and its round-up to a whole observation.
p, se, interval = wald(18, 120)
assert p == .15 and round(se, 4) == .0326
assert round(p * (1 - p) / 120, 7) == .0010625
assert tuple(round(x, 3) for x in interval) == (.086, .214)
needed = 1.96**2 * p * (1 - p) / .03**2
assert round(needed) == 544 and math.ceil(needed) == 545
assert round(1.96**2, 4) == 3.8416 and p * (1 - p) == .1275

# Worked total and class-specific rates.
assert 20 + 80 == 100 and 5 + 8 == 13
assert 5 / 20 == .25 and 8 / 80 == .10
p, se, interval = wald(13, 100)
assert p == .13 and round(se, 5) == .03363
assert tuple(round(x, 3) for x in interval) == (.064, .196)

# Hidden practice.
assert 30 + 120 == 150 and 6 + 12 == 18
assert 6 / 30 == .20 and 12 / 120 == .10
p, se, interval = wald(18, 150)
assert p == .12 and round(se, 5) == .02653
assert tuple(round(x, 3) for x in interval) == (.068, .172)

for printed in (
    "18/120=0.15", "0.13", "5/20=0.25", "8/80=0.10",
    "0.03363", "(0.064,0.196)", "18/150=0.12",
    "6/30=0.20", "12/120=0.10", "0.02653",
    "(0.068,0.172)", "$545$", "0.0010625", "0.0326",
    "(0.086,0.214)", "3.8416", "0.1275", "544",
):
    assert printed in body, f"Missing displayed number {printed}"

assert "is a set of untouched cases" in body
assert body.count('title="Proof"') == 1
assert "## Motivating example" in body and "## Worked example" in body
assert "**Your turn.**" in body and "## Check yourself" in body
assert body.count('title="Answer"') >= 3
for qid in ("ex-sl-09-7", "ex-sl-12-7"):
    assert f"../questions/{qid}.qmd" in page
for key in ("cawley_talbot2010", "dodge2008", "efron1983"):
    assert f'data-cite-key="{key}"' in body
print("held-out set arithmetic, proof and practice passed")
