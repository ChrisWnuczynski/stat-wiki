"""Recompute the numerical claims and inspect the generated article."""
from pathlib import Path
import math
from fractions import Fraction
from itertools import combinations
import numpy as np
from scipy import stats
import sympy as sp
ROOT = Path(__file__).resolve().parents[1]
w=np.array([.05,.15,.30,.50]);err=np.array([True,True,False,False])
e=w[err].sum();alpha=.5*math.log((1-e)/e)
assert np.isclose(alpha,math.log(2)) and f'{alpha:.6f}'=='0.693147'
u=w*np.where(err,math.exp(alpha),math.exp(-alpha))
assert np.allclose(u,[.1,.3,.15,.25]) and np.isclose(u.sum(),.8)
v=u/u.sum();assert np.allclose(v,[.125,.375,.1875,.3125])
assert np.isclose(v[err].sum(),.5)
u2=w*np.where(err,math.exp(alpha/2),math.exp(-alpha/2));assert np.isclose(u2[err].sum()/u2.sum(),1/3)
for e in [.1,.2,.3,.5,.7,.9]:
 a=.5*math.log((1-e)/e);assert np.isclose(e*math.exp(a)/((1-e)*math.exp(-a)+e*math.exp(a)),.5)

text = (ROOT / "articles" / "the-reweighted-error-is-one-half.qmd").read_text(encoding="utf-8")
assert "## Check yourself {#check-yourself}" in text
assert "Your turn" in text
assert text.count('class="cite-ref"') >= 5
print("the-reweighted-error-is-one-half: all recomputed claims and generated-text checks passed")
