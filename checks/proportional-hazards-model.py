"""Recompute the article examples independently and inspect generated prose."""
from pathlib import Path
import re
ROOT = Path(__file__).resolve().parents[1]
SLUG = Path(__file__).stem
source = (ROOT / "research" / "content" / (SLUG + ".md")).read_text()
article = (ROOT / "articles" / (SLUG + ".qmd")).read_text().split("## See also", 1)[0]
assert "Motivating example" in article and "Your turn" in article
assert "## Check yourself {#check-yourself}" in article
assert len(re.findall(r'class="cite-ref"', article)) >= 5
assert len(set(re.findall(r'data-cite-key="([^"]+)"', article))) >= 2
for answer in re.findall(r'::: \{\.callout-tip collapse="true" title="Answer"\}\n(.*?)\n:::', source, re.S):
    assert "{{cite:" not in answer

import math
import sympy as sp
b,x,h0 = sp.symbols("b x h0", real=True, positive=True)
assert sp.simplify(h0*sp.exp(b*(x+1))/(h0*sp.exp(b*x))-sp.exp(b)) == 0
survival = .8**math.exp(.5)
assert abs(survival - .6921853451110332) < 1e-14
assert round(math.exp(.5),4) == 1.6487
assert round((1-survival)/.2,4) == 1.5391
assert round(1-math.exp(-math.exp(.3)),4) == .7407
assert round(1-math.exp(-math.exp(-.5)),4) == .4548
assert abs(.8**2-.64) < 1e-14
assert abs((1-.8**2)/.2-1.8) < 1e-14
for value in ("1.6487", "0.6922", "1.5391", "0.7407", "0.4548"):
    assert value in article, value

print("proportional-hazards-model: numerical, algebra and generated-content checks passed")
