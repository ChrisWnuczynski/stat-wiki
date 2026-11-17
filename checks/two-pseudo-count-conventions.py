"""Recompute the numerical claims and inspect the generated article."""
from pathlib import Path
import math
from fractions import Fraction
from itertools import combinations
import numpy as np
from scipy import stats
import sympy as sp
ROOT = Path(__file__).resolve().parents[1]
assert Fraction(8+5,10+10)==Fraction(13,20)
assert Fraction(8+5-1,10+10-2)==Fraction(2,3)
assert Fraction(10*Fraction(4,5)+8*Fraction(1,2),18)==Fraction(2,3)
assert Fraction(8+1,10+2)==Fraction(3,4)
assert Fraction(8,10)==Fraction(4,5)
assert (2+3,4+6-3)==(5,7)
assert Fraction(5-1,5+7-2)==Fraction(2,5)
assert Fraction(2+3,2+4+6)==Fraction(5,12)
assert Fraction(5+1,5+5+1)==Fraction(6,11)
x=sp.symbols('x',positive=True)
assert sp.simplify(sp.diff(12*sp.log(x)+6*sp.log(1-x),x).subs(x,sp.Rational(2,3)))==0

text = (ROOT / "articles" / "two-pseudo-count-conventions.qmd").read_text(encoding="utf-8")
assert "## Check yourself {#check-yourself}" in text
assert "Your turn" in text
assert text.count('class="cite-ref"') >= 5
print("two-pseudo-count-conventions: all recomputed claims and generated-text checks passed")
