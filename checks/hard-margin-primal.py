"""Recompute the article's displayed examples and inspect the generated article."""
from pathlib import Path
import math,re,json
import numpy as np
import sympy as sp
from itertools import product
ROOT=Path(__file__).resolve().parents[1]
SLUG='hard-margin-primal'
article=(ROOT / "articles" / (SLUG+".qmd")).read_text(encoding="utf-8")
body=article.split("## See also",1)[0]
checks=0
def check(condition):
    global checks
    assert condition, SLUG
    checks+=1
def close(actual,expected,rtol=1e-10,atol=1e-12):
    check(np.allclose(np.asarray(actual,dtype=float),np.asarray(expected,dtype=float),rtol=rtol,atol=atol))

w=sp.Rational(1,3); b=-w
check(2*w-b==1 and 4*w+b==1)
check(w*w/2==sp.Rational(1,18))
check(-b/w==1 and 2/abs(w)==6)
a=sp.Rational(1,18)
check(a*(-1)*(-2)+a*1*4==w)
check(7*w+b==2)
check(sp.Rational(1,2)**2/2==sp.Rational(1,8))
check(2/sp.Rational(1,2)==4)
check(1**2/2==.5 and 2**2/2==2)
check(all(y*(2*x+bb)>=1 for bb,y0 in [(1,1),(-1,-1)] for x,y in [(-1,-1),(1,1),(0,y0)]))
# A duplicate support point can have zero multiplier while all KKT equations hold.
check(sp.Rational(1,18)*(-1)*(-2)+sp.Rational(1,18)*4+0*4==w)
# Opposite labels at one input require incompatible score inequalities.
z=sp.symbols('z',real=True)
check(sp.reduce_inequalities([z>=1,z<=-1],z)==sp.false)

# Verify citation coverage in the composed article, including copied source blocks.
check(len(re.findall(r'class="cite-ref"',body))>=5)
proper_keys=set(re.findall(r'data-cite-key="([^" ]+)"',body))-{'r_faraway_leafblotch2026'}
check(len(proper_keys)>=2)

for token in ['1/18', '1/3', 'six units', '1/8']:
    check(token in body)
check("**Your turn.**" in body)
check(len(re.findall(r"^## Check yourself \{#check-yourself\}",body,re.M))==1)
print(f"{SLUG}: {checks} numerical, algebraic and rendered-content checks passed")
