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
var=Fraction(a*b,(a+b)**2*(a+b+1))
assert var==Fraction(1,25)
assert Fraction(6*4,10**2*11)==Fraction(6,275)
assert Fraction(6*6,12**2*13)==Fraction(1,52)
assert Fraction(1+2,1+1+2+5)==Fraction(1,3)
p=sp.symbols('p')
assert sp.integrate(12*p*(1-p)**2,(p,0,1))==1
assert sp.integrate(p*12*p*(1-p)**2,(p,0,1))==sp.Rational(2,5)
assert sp.integrate(p*(1-p)*12*p*(1-p)**2,(p,0,1))-sp.Rational(2,5)*sp.Rational(3,5)==-sp.Rational(1,25)

text = (ROOT / "articles" / "the-beta-distribution-is-the-two-category-dirichlet.qmd").read_text(encoding="utf-8")
assert "## Check yourself {#check-yourself}" in text
assert "Your turn" in text
assert text.count('class="cite-ref"') >= 5
print("the-beta-distribution-is-the-two-category-dirichlet: all recomputed claims and generated-text checks passed")
