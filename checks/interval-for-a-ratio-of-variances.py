"""Recompute the displayed examples and practice answers."""
import math
from fractions import Fraction
import numpy as np
from scipy import stats, optimize
from pathlib import Path

r=14.1**2/14.3**2;q=stats.f.ppf(.975,49,49)
assert round(r,3)==.972 and round(q,3)==1.762
assert round(r/q,3)==.552 and round(r*q,3)==1.713
q8=stats.f.ppf(.975,8,8)
assert round(q8,2)==4.43
assert round(4/q8,3)==.902 and round(4*q8,2)==17.73
assert round(math.sqrt(4/q8),2)==.95 and round(math.sqrt(4*q8),2)==4.21
lo=2.25/stats.f.ppf(.975,12,8);hi=2.25/stats.f.ppf(.025,12,8)
print('unequal df interval:',lo,hi)
assert math.isclose(stats.f.ppf(.025,12,8)*stats.f.ppf(.975,8,12),1)
assert 1/8==.125 and 1/.5==2
assert round(lo,4)==.5358 and round(hi,4)==7.9015
assert math.isclose((r/q)*(r*q),r*r)

# Compare recomputed results with the generated worked example and practice answer.
ROOT = Path(__file__).resolve().parents[1]
SLUG = 'interval-for-a-ratio-of-variances'
article = (ROOT / "articles" / (SLUG + ".qmd")).read_text(encoding="utf-8")
worked_section = article.split("{#worked-example}", 1)[1].split("\n## ", 1)[0]
worked_example, your_turn = worked_section.split("**Your turn.**", 1)

assert f"({lo:.4f},{hi:.4f})" in worked_example
assert f"(1/8,1/0.5)=({1/8:.3f},{1/.5:g})" in your_turn
assert f"({math.sqrt(.5):.4f},{math.sqrt(8):.4f})" in your_turn

print("interval-for-a-ratio-of-variances: numerical checks passed")
