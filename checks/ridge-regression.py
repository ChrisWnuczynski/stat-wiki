"""Ridge objective and printed examples."""
from pathlib import Path
from math import isclose

root = Path(__file__).resolve().parents[1]
page = (root / "articles/ridge-regression.qmd").read_text()
source = (root / "research/content/ridge-regression.md").read_text()

def near(a, b):
    assert isclose(a, b, abs_tol=1e-10), (a, b)

assert 2*2-2*2 == 0
assert 3*3-2*2 == 5
near((3*4-2*4)/5, .8)
near(.8+.8, 1.6)
for lam, target in [(0,2), (2,4/3), (4,1)]:
    near(8/(4+lam), target)
for val, target in [(2.4,.8), (-.9,-.3), (.5,1/6), (-.1,-1/30)]:
    near(val/3, target)
assert "::: {.callout-note collapse=\"true\" title=\"Proof\"}" in page
assert "::: {.callout-tip collapse=\"true\" title=\"Answer\"}" in page
assert "## Worked example {#worked-example}" in page
assert "Lead context" not in source
print("ridge regression checks passed")
