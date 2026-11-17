"""Recompute the displayed examples and practice answers."""
import math
from fractions import Fraction
import numpy as np
from scipy import stats, optimize
from pathlib import Path

def decision(p,fp,fn):return int((1-p)*fp<p*fn)
assert decision(.2,1,9)==1 and decision(.05,1,9)==0
assert math.isclose((1-.2),.8) and math.isclose(.2*9,1.8)
assert math.isclose((1-.05),.95) and math.isclose(.05*9,.45)
assert 4/(4+1)==.8 and decision(.7,4,1)==0
assert math.isclose((1-.7)*4,1.2)
for p in np.linspace(0,1,101):
 assert decision(p,4,1)==decision(p,40,10)

# Compare recomputed results with the generated worked example and practice answer.
ROOT = Path(__file__).resolve().parents[1]
SLUG = 'classification-with-unequal-costs'
article = (ROOT / "articles" / (SLUG + ".qmd")).read_text(encoding="utf-8")
worked_section = article.split("{#worked-example}", 1)[1].split("\n## ", 1)[0]
worked_example, your_turn = worked_section.split("**Your turn.**", 1)

for expected_cost in ((1-.2)*1,.2*9):
 assert f"${expected_cost:.1f}$" in worked_example
assert f"1/10={1/(1+9):.1f}" in worked_example
assert f"4/(4+1)={4/(4+1):.1f}" in your_turn
assert f"0.3(4)={(1-.7)*4:.1f}" in your_turn
assert 'so predict zero' in your_turn and decision(.7,4,1)==0

print("classification-with-unequal-costs: numerical checks passed")
