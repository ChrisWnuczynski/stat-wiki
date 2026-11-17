"""Recompute the numerical claims and inspect the generated article."""
from pathlib import Path
import math
from fractions import Fraction
from itertools import combinations
import numpy as np
from scipy import stats
import sympy as sp
ROOT = Path(__file__).resolve().parents[1]
a,b=2,3
assert Fraction(4+a,5+a+b)==Fraction(3,5)
assert Fraction(1+a,5+a+b)==Fraction(3,10)
assert Fraction(6*4,10**2*11)==Fraction(6,275)
assert Fraction(3*7,10**2*11)==Fraction(21,1100)
assert f'{6/275:.6f}'=='0.021818'
assert f'{21/1100:.6f}'=='0.019091'
assert Fraction(3,5)*Fraction(3,10)==Fraction(18,100)
assert (2+2,8-2+3)==(4,9)
assert Fraction(4+8,5+20)==Fraction(12,25)
p=sp.symbols('p',positive=True)
assert sp.integrate(p**5*(1-p)**3,(p,0,1))==sp.Rational(1,504)

text = (ROOT / "articles" / "study-rate-full-conditional.qmd").read_text(encoding="utf-8")
assert "## Check yourself {#check-yourself}" in text
assert "Your turn" in text
assert text.count('class="cite-ref"') >= 5
print("study-rate-full-conditional: all recomputed claims and generated-text checks passed")
