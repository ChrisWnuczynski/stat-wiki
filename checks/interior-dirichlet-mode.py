"""Recompute the article's displayed examples and inspect the generated article."""
from pathlib import Path
import math,re,json
import numpy as np
import sympy as sp
from itertools import product
ROOT=Path(__file__).resolve().parents[1]
SLUG='interior-dirichlet-mode'
article=(ROOT / "articles" / (SLUG+".qmd")).read_text(encoding="utf-8")
body=article.split("## See also",1)[0]
checks=0
def check(condition):
    global checks
    assert condition, SLUG
    checks+=1
def close(actual,expected,rtol=1e-10,atol=1e-12):
    check(np.allclose(np.asarray(actual,dtype=float),np.asarray(expected,dtype=float),rtol=rtol,atol=atol))

a=sp.Matrix([2,3,5]);A=sum(a);K=len(a);mode=(a-sp.ones(K,1))/(A-K)
check(mode==sp.Matrix([sp.Rational(1,7),sp.Rational(2,7),sp.Rational(4,7)]))
check(a/A==sp.Matrix([sp.Rational(1,5),sp.Rational(3,10),sp.Rational(1,2)]))
marg=(a-sp.ones(K,1))/(A-2);check(sum(marg)==sp.Rational(7,8))
post=a+sp.Matrix([3,0,2]);check((post-sp.ones(K,1))/(sum(post)-K)==sp.Matrix([sp.Rational(1,3),sp.Rational(1,6),sp.Rational(1,2)]))
x,y=sp.symbols('x y',positive=True);ell=sp.log(x)+2*sp.log(y)+4*sp.log(1-x-y)
sub={x:mode[0],y:mode[1]}
check(all(sp.diff(ell,z).subs(sub)==0 for z in [x,y]))
H=sp.hessian(ell,[x,y]).subs(sub);check(H[0,0]<0 and H.det()>0)
check(sp.Rational(3-1,9-3)==sp.Rational(1,3));check(3*sp.Rational(2,7)==sp.Rational(6,7))
check(sp.diff(sp.log(x**0*y**0*(1-x-y)**0),x)==0)
# The two-category concentration (1,2) has its mode at the first-coordinate boundary.
check(sp.diff(2*(1-x),x)==-2)
# Explicitly distinguish an unbounded boundary density from a finite interior maximizer.
check(sp.limit(x**(-sp.Rational(1,2))*(1-x),x,0,dir='+')==sp.oo)

# Verify citation coverage in the composed article, including copied source blocks.
check(len(re.findall(r'class="cite-ref"',body))>=5)
proper_keys=set(re.findall(r'data-cite-key="([^" ]+)"',body))-{'r_faraway_leafblotch2026'}
check(len(proper_keys)>=2)

for token in ['1/7', '2/7', '4/7', '7/8', '1/6']:
    check(token in body)
check("**Your turn.**" in body)
check(len(re.findall(r"^## Check yourself \{#check-yourself\}",body,re.M))==1)
print(f"{SLUG}: {checks} numerical, algebraic and rendered-content checks passed")
