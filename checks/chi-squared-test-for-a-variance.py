"""Recompute the displayed examples and practice answers."""
import math
from fractions import Fraction
import numpy as np
from scipy import stats, optimize
from pathlib import Path

t=6*.488/1.1
assert round(t,2)==2.66 and round(stats.chi2.cdf(t,6),4)==.1501
q=stats.chi2.ppf(.05,6)
assert round(q,3)==1.635 and round(1.1*q/6,4)==.2998
assert round(stats.chi2.sf(15,10),4)==.1321
assert stats.chi2.cdf(q*1.1/.55,6)>.05
assert round(6*.488/1.1,4)==2.6618
assert round(stats.chi2.ppf(.05,6),4)==1.6354

# Compare recomputed results with the generated worked example and practice answer.
ROOT = Path(__file__).resolve().parents[1]
SLUG = 'chi-squared-test-for-a-variance'
article = (ROOT / "articles" / (SLUG + ".qmd")).read_text(encoding="utf-8")
worked_section = article.split("{#worked-example}", 1)[1].split("\n## ", 1)[0]
worked_example, your_turn = worked_section.split("**Your turn.**", 1)

for value in (t,stats.chi2.cdf(t,6),q,1.1*q/6):
 assert f"{value:.4f}" in worked_example, (SLUG,value)
assert f"{stats.chi2.sf(10*6/4,10):.4f}" in your_turn
assert f"10(6)/4={10*6/4:g}" in your_turn

print("chi-squared-test-for-a-variance: numerical checks passed")
