"""Recompute the displayed examples and practice answers."""
import math
from fractions import Fraction
import numpy as np
from scipy import stats, optimize
from pathlib import Path

a=24*1.3**2;lo=a/stats.chi2.ppf(.975,24);hi=a/stats.chi2.ppf(.025,24)
print('tablet',lo,hi,math.sqrt(lo),math.sqrt(hi))
assert round(a,2)==40.56
assert round(stats.chi2.ppf(.025,24),2)==12.40 and round(stats.chi2.ppf(.975,24),2)==39.36
assert round(lo,2)==1.03 and round(hi,2)==3.27
assert round(math.sqrt(lo),2)==1.02 and round(math.sqrt(hi),2)==1.81
lo2=36/stats.chi2.ppf(.975,9);hi2=36/stats.chi2.ppf(.025,9)
print('exercise',lo2,hi2,math.sqrt(lo2),math.sqrt(hi2))
assert math.isclose(stats.chi2.cdf(a/lo,24)-stats.chi2.cdf(a/hi,24),.95)
assert round(lo,4)==1.0304 and round(hi,4)==3.2707
assert round(math.sqrt(lo),4)==1.0151 and round(math.sqrt(hi),4)==1.8085
assert round(lo2,4)==1.8925 and round(hi2,4)==13.3314
assert round(math.sqrt(lo2),4)==1.3757 and round(math.sqrt(hi2),4)==3.6512

# Compare recomputed results with the generated worked example and practice answer.
ROOT = Path(__file__).resolve().parents[1]
SLUG = 'interval-for-a-normal-variance'
article = (ROOT / "articles" / (SLUG + ".qmd")).read_text(encoding="utf-8")
worked_section = article.split("{#worked-example}", 1)[1].split("\n## ", 1)[0]
worked_example, your_turn = worked_section.split("**Your turn.**", 1)

for value in (lo,hi,math.sqrt(lo),math.sqrt(hi)):
 assert f"{value:.4f}" in worked_example
for value in (lo2,hi2,math.sqrt(lo2),math.sqrt(hi2)):
 assert f"{value:.4f}" in your_turn

print("interval-for-a-normal-variance: numerical checks passed")
