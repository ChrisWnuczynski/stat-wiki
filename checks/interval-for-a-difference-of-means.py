"""Recompute the displayed examples and practice answers."""
import math
from fractions import Fraction
import numpy as np
from scipy import stats, optimize
from pathlib import Path

sp=(9*4+14*9)/23;se=math.sqrt(sp*(1/10+1/15));half=stats.t.ppf(.975,23)*se
print('constructed mean interval',se,half,3-half,3+half)
assert round(se,4)==1.0835
se2=2*math.sqrt(.2);h=stats.t.ppf(.975,18)*se2
assert round(se2,4)==.8944 and round(h,4)==1.8791
sp_safety=(14.1**2+14.3**2)/2; se_safety=math.sqrt(sp_safety*.04);h2=stats.t.ppf(.975,98)*se_safety
assert math.isclose(sp_safety,201.65) and round(se_safety,4)==2.8401
assert round(-17-h2,2)==-22.64 and round(-17+h2,2)==-11.36
assert round(2*stats.t.cdf(1,98)-1,2)==.68
a,b=4/10,9/15;dfw=(a+b)**2/(a*a/9+b*b/14)
assert 9<dfw<=23
assert math.isclose(math.sqrt((14.1**2+14.3**2)/50),se_safety)
assert round(half,4)==2.2413 and round(3-half,4)==.7587 and round(3+half,4)==5.2413
assert round(stats.t.ppf(.975,23),4)==2.0687 and round(stats.t.ppf(.975,18),4)==2.1009

# Compare recomputed results with the generated worked example and practice answer.
ROOT = Path(__file__).resolve().parents[1]
SLUG = 'interval-for-a-difference-of-means'
article = (ROOT / "articles" / (SLUG + ".qmd")).read_text(encoding="utf-8")
worked_section = article.split("{#worked-example}", 1)[1].split("\n## ", 1)[0]
worked_example, your_turn = worked_section.split("**Your turn.**", 1)

for value in (se,stats.t.ppf(.975,23),half,3-half,3+half):
 assert f"{value:.4f}" in worked_example
for value in (se2,stats.t.ppf(.975,18),h,1-h,1+h):
 assert f"{value:.4f}" in your_turn

print("interval-for-a-difference-of-means: numerical checks passed")
