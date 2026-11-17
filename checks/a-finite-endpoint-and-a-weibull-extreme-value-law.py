"""Recompute the numerical claims and inspect the generated article."""
from pathlib import Path
import math
from fractions import Fraction
from itertools import combinations
import numpy as np
from scipy import stats
import sympy as sp
ROOT = Path(__file__).resolve().parents[1]
exact=.96**50;lim=math.exp(-2)
assert f'{exact:.6f}'=='0.129886'
assert f'{lim:.6f}'=='0.135335'
assert f'{lim-exact:.6f}'=='0.005449'
assert f'{.95**50:.6f}'=='0.076945'
assert f'{50/51:.6f}'=='0.980392'
assert f'{.98**100:.6f}'=='0.132620'
x,n=sp.symbols('x n',positive=True)
assert sp.integrate(50*x**50,(x,0,1))==sp.Rational(50,51)
a,b,m=sp.symbols('a b m')
assert sp.simplify((b-(a+(b-a)*m))/(b-a)-(1-m))==0
for n in [100,1000,10000]:assert (1-2/n)**n<lim
assert np.isclose(3*100*((3*100)**(-.5)*2)**2,4)

text = (ROOT / "articles" / "a-finite-endpoint-and-a-weibull-extreme-value-law.qmd").read_text(encoding="utf-8")
assert "## Check yourself {#check-yourself}" in text
assert "Your turn" in text
assert text.count('class="cite-ref"') >= 5
print("a-finite-endpoint-and-a-weibull-extreme-value-law: all recomputed claims and generated-text checks passed")
