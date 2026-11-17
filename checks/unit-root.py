"""Recompute the numerical claims and inspect the generated article."""
from pathlib import Path
import math
from fractions import Fraction
from itertools import combinations
import numpy as np
from scipy import stats
import sympy as sp
ROOT = Path(__file__).resolve().parents[1]
assert [t*4 for t in [1,5,20]]==[4,20,80]
assert f'{math.sqrt(20):.6f}'=='4.472136'
assert f'{math.sqrt(80):.6f}'=='8.944272'
assert np.isclose(4/(1-.8**2),100/9)
assert f'{4/(1-.8**2):.6f}'=='11.111111'
assert 10+3*.5==11.5 and 3*4==12
z=sp.symbols('z');assert sp.factor(1-z)==1-z
assert sp.diff((1-z)**2,z).subs(z,1)==0

text = (ROOT / "articles" / "unit-root.qmd").read_text(encoding="utf-8")
assert "## Check yourself {#check-yourself}" in text
assert "Your turn" in text
assert text.count('class="cite-ref"') >= 5
print("unit-root: all recomputed claims and generated-text checks passed")
