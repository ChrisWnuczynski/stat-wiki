"""Recompute the numerical claims and inspect the generated article."""
from pathlib import Path
import math
from fractions import Fraction
from itertools import combinations
import numpy as np
from scipy import stats
import sympy as sp
ROOT = Path(__file__).resolve().parents[1]
from scipy.stats import rankdata
x=np.array([[1,10],[2,0],[4,5],[3,7]],dtype=float)
r=np.column_stack([rankdata(x[:,j]) for j in range(2)])
assert np.array_equal(r,[[1,4],[2,1],[4,2],[3,3]])
diff=np.abs(r[:-1]-r[-1]);assert np.array_equal(diff.max(axis=1),[2,2,1])
assert np.array_equal(diff.sum(axis=1),[3,3,2])
for transform in [lambda a:100*a,lambda a:-a,lambda a:a**3]:
 rt=np.column_stack([rankdata(transform(x[:,j])) for j in range(2)])
 assert np.array_equal(np.abs(rt[:-1]-rt[-1]).max(axis=1),[2,2,1])

# Deepened research calculations.
assert max(4, 1) == 4 and 4+1 == 5
assert max(3, 3) == 3 and 3+3 == 6
assert max(5, 2) == 5 and 5+2 == 7
assert max(6, 0) == 6 and 6+0 == 6
assert abs((7-1)-(7-4)) == abs(1-4)

text = (ROOT / "articles" / "rank-distance.qmd").read_text(encoding="utf-8")
assert "## Check yourself {#check-yourself}" in text
assert "Your turn" in text
assert text.count('class="cite-ref"') >= 5
print("rank-distance: all recomputed claims and generated-text checks passed")
