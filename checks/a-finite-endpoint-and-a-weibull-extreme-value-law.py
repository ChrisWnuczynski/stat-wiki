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

# Deepened research calculations.
import sympy as sp
n, y, c, a = sp.symbols("n y c a", positive=True)
mean = sp.integrate(n*x*x**(n-1), (x, 0, 1))
second = sp.integrate(n*x**2*x**(n-1), (x, 0, 1))
var = sp.simplify(second - mean**2)
assert sp.simplify(var - n/((n+1)**2*(n+2))) == 0
assert sp.simplify(n*c*( (c*n)**(-sp.Integer(1)/a) * y )**a) == y**a
assert sp.limit(n*sp.log(1-y/n), n, sp.oo) == -y
assert sp.integrate(2*(1-x), (x, 0, 1)) == 1
assert f"{50/135252:.6f}" == "0.000370"
assert f"{125000/135252:.6f}" == "0.924201"
assert f"{0.99**100:.6f}" == "0.366032"
assert f"{math.exp(-1):.6f}" == "0.367879"
assert f"{0.96**100:.6f}" == "0.016870"
assert f"{math.exp(-4):.6f}" == "0.018316"
assert f"{0.94**50:.6f}" == "0.045331"

text = (ROOT / "articles" / "a-finite-endpoint-and-a-weibull-extreme-value-law.qmd").read_text(encoding="utf-8")
assert "## Check yourself {#check-yourself}" in text
assert "Your turn" in text
assert text.count('class="cite-ref"') >= 5
print("a-finite-endpoint-and-a-weibull-extreme-value-law: all recomputed claims and generated-text checks passed")
