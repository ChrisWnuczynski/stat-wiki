"""Recompute log-link examples and verify the generated article."""

import math
from pathlib import Path


root = Path(__file__).resolve().parents[1]
page = (root / "articles/log-link.qmd").read_text()
body = page.split("## See also", 1)[0]

# Inherited coefficient, rate and exposure examples.
assert round(math.log(2), 3) == .693
assert round(math.exp(1), 1) == 2.7
assert round(math.exp(.01), 2) == 1.01
assert 4 / 2 == 2 and 4 / 8 == .5
assert .01 * 100 == 1

# Worked count model: log t + log 2 + log(1.5)x.
def count(t, x):
    return math.exp(math.log(t) + math.log(2) + math.log(1.5) * x)


assert math.isclose(count(5, 0), 10)
assert math.isclose(count(10, 1), 30)
assert math.isclose(count(5, 1), 15)
assert math.isclose(count(10, 1) / count(5, 0), 3)
assert math.isclose(count(5, 1) / count(5, 0), 1.5)

# Hidden practice: x=2 or 3, same exposure t=3.
rate2 = 4 * 1.25**2
rate3 = 4 * 1.25**3
assert rate2 == 6.25 and rate3 == 7.8125
assert 3 * rate2 == 18.75 and 3 * rate3 == 23.4375
assert rate3 / rate2 == 1.25

# Log of a mean differs from the mean log, even for positive outcomes.
assert round(math.log((1 + 9) / 2), 3) == 1.609
assert round((math.log(1) + math.log(9)) / 2, 3) == 1.099

# The inherited lake and Gamma question answers.
assert round(math.exp(1.5), 2) == 4.48
assert round(math.exp(-.04), 4) == .9608
assert round(100 * (1 - math.exp(-.04)), 2) == 3.92
assert round(2**.6, 3) == 1.516
assert round(100 * (2**.6 - 1), 1) == 51.6
assert round(math.exp(-.08), 4) == .9231
assert round(100 * (1 - math.exp(-.08)), 2) == 7.69

for printed in (
    "$2$", "$0.5$", "0.693", "$-0.693$", "$0.01$",
    "$e^{1}\\approx 2.7$", "$e^{0.01}\\approx 1.01$",
    "5", "10", "30", "$50\\%$", "$15$", "6.25",
    "18.75", "7.8125", "23.4375", "$25\\%$",
    "1.609", "1.099", "$4.48$", "0.9608",
    "3.92\\%", "1.516", "$51.6\\%$", "$0.9231$",
    "7.69\\%",
):
    assert printed in body, f"Missing displayed number {printed}"

assert body.count('title="Proof"') == 1
assert "## Motivating example" in body and "## Worked example" in body
assert "**Your turn.**" in body and "## Check yourself" in body
assert body.count('title="Answer"') >= 3
for qid in ("q-31", "q-55"):
    assert f"../questions/{qid}.qmd" in page
for key in ("mccullagh1992_glm_intro", "rstats_family2026"):
    assert f'data-cite-key="{key}"' in body
print("log-link arithmetic, proof, practice and sources passed")
