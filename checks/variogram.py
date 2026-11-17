"""Recompute the numerical claims and inspect the generated article."""
from pathlib import Path
import math
from fractions import Fraction
from itertools import combinations
import numpy as np
from scipy import stats
import sympy as sp
ROOT = Path(__file__).resolve().parents[1]
x=np.array([1,2,4,3])
assert np.array_equal(np.diff(x)**2,[1,4,1])
assert np.isclose(np.mean((x[1:]-x[:-1])**2)/2,1)
assert np.isclose(np.mean((x[2:]-x[:-2])**2)/2,2.5)
assert np.isclose(np.mean((x[3:]-x[:-3])**2)/2,2)
assert 2*(4-4*.5)==4
assert np.isclose(2*(4-4*.5**100),8)
assert 4*3==12 and 12/2==6 and 2*(5-2)==6
for h in [1,2,10]:assert h*1==h

text = (ROOT / "articles" / "variogram.qmd").read_text(encoding="utf-8")
assert "## Check yourself {#check-yourself}" in text
assert "Your turn" in text
assert text.count('class="cite-ref"') >= 5
print("variogram: all recomputed claims and generated-text checks passed")
