"""Recompute the numerical claims and inspect the generated article."""
from pathlib import Path
import math
from fractions import Fraction
from itertools import combinations
import numpy as np
from scipy import stats
import sympy as sp
ROOT = Path(__file__).resolve().parents[1]
sp2=Fraction(5*4+9*9,14);assert sp2==Fraction(101,14)
var=sp2*(Fraction(1,6)+Fraction(1,10));assert var==Fraction(202,105)
se=math.sqrt(var)
assert f'{float(sp2):.6f}'=='7.214286'
assert f'{float(var):.6f}'=='1.923810'
assert f'{se:.6f}'=='1.387015'
assert f'{3/se:.6f}'=='2.162919'
assert f'{2/se:.6f}'=='1.441946'
oldse=2*math.sqrt(.2);q=stats.t.ppf(.975,18)
assert f'{q:.3f}'=='2.101'
assert [round(3-q*oldse,2),round(3+q*oldse,2)]==[1.12,4.88]
assert 8+12-2==18

text = (ROOT / "articles" / "two-sample-t-pivot.qmd").read_text(encoding="utf-8")
assert "## Check yourself {#check-yourself}" in text
assert "Your turn" in text
assert text.count('class="cite-ref"') >= 5
print("two-sample-t-pivot: all recomputed claims and generated-text checks passed")
