"""Recompute the numerical claims and inspect the generated article."""
from pathlib import Path
import math
from fractions import Fraction
from itertools import combinations
import numpy as np
from scipy import stats
import sympy as sp
ROOT = Path(__file__).resolve().parents[1]
ranks=range(1,7);ss=np.array([sum(c) for c in combinations(ranks,3)])
assert len(ss)==math.comb(6,3)==20
assert np.isclose(ss.mean(),10.5)
assert np.isclose(ss.var(),3*3*7/12)
assert sum(ss<=8)==4 and sum(ss<=8)/20==.2
assert 2*sum(ss<=8)/20==.4
assert 8-3*4/2==2
r=[1,2.5,2.5,4];v=np.array([sum(c) for c in combinations(r,2)])
assert np.array_equal(np.sort(v),[3.5,3.5,5,5,6.5,6.5])
assert np.isclose(v.var(),1.5) and v.var()<2*2*5/12

# Deepened research calculations.
assert 4*11/2 == 22
assert 5*11/2 == 27.5
assert 3*3*7/12 == 5.25
assert 1.5 < 5/3

text = (ROOT / "articles" / "wilcoxon-rank-sum-test.qmd").read_text(encoding="utf-8")
assert "## Check yourself {#check-yourself}" in text
assert "Your turn" in text
assert text.count('class="cite-ref"') >= 5
print("wilcoxon-rank-sum-test: all recomputed claims and generated-text checks passed")
