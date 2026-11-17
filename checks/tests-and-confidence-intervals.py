"""Recompute numerical examples and exercise answers for tests-and-confidence-intervals."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SLUG = 'tests-and-confidence-intervals'
text = (ROOT / "articles" / (SLUG + ".qmd")).read_text(encoding="utf-8")
worked = text.split("{#worked-example}", 1)[1].split("\n## ", 1)[0]
answer = worked.split('title="Answer"}', 1)[1]

import math
import numpy as np
from scipy import stats, special, linalg, integrate

c=stats.t.ppf(.975,15);lo,hi=12-c,12+c
assert round(c,5)==2.13145 and round(lo,5)==9.86855 and round(hi,5)==14.13145
assert round(2*stats.t.sf(2,15),5)==.06395 and round(2*stats.t.sf(3,15),5)==.00897
assert round(stats.t.sf(2,15),5)==.03197 and round(12-stats.t.ppf(.95,15),5)==10.24695
for null in np.linspace(5,20,100):assert (abs(12-null)>c)==(null<lo or null>hi)
assert [2.1<=x<=4.7 for x in [2,3,5]]==[False,True,False]
assert 1-.01==.99

# Match computed worked-example and practice results to their generated text.
assert f"[{lo:.5f},{hi:.5f}]" in worked
assert rf"p\approx{2*stats.t.sf(2,15):.5f}" in worked and rf"p\approx{2*stats.t.sf(3,15):.5f}" in worked
assert rf"\approx{12-stats.t.ppf(.95,15):.5f}" in worked
exercise_nulls=np.array([2,3,5]);rejected=exercise_nulls[(exercise_nulls<2.1)|(exercise_nulls>4.7)];accepted=exercise_nulls[(exercise_nulls>=2.1)&(exercise_nulls<=4.7)]
assert f"reject ${rejected[0]}$ and ${rejected[1]}$ and do not reject ${accepted[0]}$" in answer
print("tests-and-confidence-intervals: numerical checks passed")
