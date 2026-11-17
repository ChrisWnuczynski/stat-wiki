"""Recompute the numerical claims and inspect the generated article."""
from pathlib import Path
import math
from fractions import Fraction
from itertools import combinations
import numpy as np
from scipy import stats
import sympy as sp
ROOT = Path(__file__).resolve().parents[1]
lam=sp.symbols('lam',positive=True);h=sp.exp(-lam)
assert sp.diff(h,lam)==-sp.exp(-lam)
assert sp.simplify(lam*sp.diff(h,lam)**2)==lam*sp.exp(-2*lam)
se=math.exp(-2)*math.sqrt(2/100)
assert f'{se:.6f}'=='0.019139'
assert f'{math.exp(-2):.6f}'=='0.135335'
assert f'{se/2:.6f}'=='0.009570'
assert np.isclose(math.exp(-2)*math.sqrt(2/400),se/2)
assert 4*3**2==36
x=np.array([0,2,1,4,1,0,3]);assert x.sum()==11 and np.isclose(x.mean(),11/7)
assert np.isfinite(math.exp(-x.mean())*math.sqrt(x.mean()/len(x)))

text = (ROOT / "articles" / "delta-method.qmd").read_text(encoding="utf-8")
assert "## Check yourself {#check-yourself}" in text
assert "Your turn" in text
assert text.count('class="cite-ref"') >= 5
print("delta-method: all recomputed claims and generated-text checks passed")
