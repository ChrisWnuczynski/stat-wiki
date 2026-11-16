"""Verify GEE worked scores and printed standard errors."""
import math
from pathlib import Path

assert (10*2 + 10*0 + 10*1)/60 == .5
assert math.isclose(math.sqrt(.25/60), .06455, abs_tol=5e-6)
assert 60*.25 == 15
assert 10*1**2+10*(-1)**2 == 20
assert math.isclose(20/15**2, .08889, abs_tol=5e-6)
assert math.isclose(.25*math.sqrt(20/15**2), .07454, abs_tol=5e-6)
assert (10*2)/40 == .5
assert math.isclose(math.sqrt(.25/40), .07906, abs_tol=5e-6)
assert 40*.25 == 10 and 20/10**2 == .2
assert math.isclose(.25*math.sqrt(.2), .11180, abs_tol=5e-6)
root = Path(__file__).resolve().parents[1]
body = (root / "research/content/generalised-estimating-equations.md").read_text()
for value in ("0.06455", "0.08889", "0.07454", "0.07906", "0.11180"):
    assert value in body
page = root / "articles/generalised-estimating-equations.qmd"
if page.exists():
    rendered = page.read_text()
    for old in ("../questions/c-38.qmd", "../questions/c-39.qmd",
                "../questions/c-40.qmd", "../questions/c-41.qmd"):
        assert old in rendered
