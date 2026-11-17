"""Recompute numerical examples and exercise answers for range."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SLUG = 'range'
text = (ROOT / "articles" / (SLUG + ".qmd")).read_text(encoding="utf-8")
worked = text.split("{#worked-example}", 1)[1].split("\n## ", 1)[0]
answer = worked.split('title="Answer"}', 1)[1]

import math
import numpy as np
from scipy import stats, special, linalg, integrate

a=np.array([4,8,9,11,13]);b=np.array([4,8,9,11,130])
assert np.ptp(a)==9 and np.ptp(b)==126 and np.median(a)==np.median(b)==9
assert np.ptp(b)/np.ptp(a)==14 and np.diff(np.quantile(a,[.25,.75]))[0]==3
A=np.array([2,4,6,8,10]);B=np.array([2,2,6,10,10])
assert np.ptp(A)==np.ptp(B)==8 and A.mean()==B.mean()==6
assert A.var(ddof=1)==10 and B.var(ddof=1)==16
assert round(A.std(ddof=1),3)==3.162
assert np.diff(np.quantile(A,[.25,.75]))[0]==4 and np.diff(np.quantile(B,[.25,.75]))[0]==8
for x,r in [([3,5,8,12],9),([3,5,8,12,7],9),([3,5,8,12,7,20],17)]:
 assert np.ptp(x)==r and np.ptp(100-2*np.array(x))==2*r
assert np.ptp([1000])==0 and np.ptp([0,1000000])==1000000
assert np.ptp([0,0,0,10,10])==np.ptp([0,4,5,6,10])==10
assert 5-(-2)==7 and math.isclose(1.8*8,14.4)

# Match computed worked-example and practice results to their generated text.
assert f"sample variances are ${A.var(ddof=1):g}$ and ${B.var(ddof=1):g}$" in worked
assert f"approximately ${A.std(ddof=1):.3f}$ and ${B.std(ddof=1):g}$" in worked
exercise_ranges=[np.ptp(z) for z in ([3,5,8,12],[3,5,8,12,7],[3,5,8,12,7,20])]
assert 'giving $'+','.join(f'{2*z:g}' for z in exercise_ranges)+'$' in answer
print("range: numerical checks passed")
