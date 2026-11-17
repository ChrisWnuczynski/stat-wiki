"""Recompute the article's displayed examples and inspect the generated article."""
from pathlib import Path
import math,re,json
import numpy as np
import sympy as sp
from itertools import product
ROOT=Path(__file__).resolve().parents[1]
SLUG='log-partition-moment-identities'
article=(ROOT / "articles" / (SLUG+".qmd")).read_text(encoding="utf-8")
body=article.split("## See also",1)[0]
checks=0
def check(condition):
    global checks
    assert condition, SLUG
    checks+=1
def close(actual,expected,rtol=1e-10,atol=1e-12):
    check(np.allclose(np.asarray(actual,dtype=float),np.asarray(expected,dtype=float),rtol=rtol,atol=atol))

e=sp.symbols('eta',real=True);A=sp.log(1+sp.exp(e));p=sp.exp(e)/(1+sp.exp(e))
check(sp.simplify(sp.diff(A,e)-p)==0);check(sp.simplify(sp.diff(A,e,2)-p*(1-p))==0)
check(sp.simplify(sp.diff(A,e).subs(e,sp.log(3)))==sp.Rational(3,4))
check(sp.simplify(sp.diff(A,e,2).subs(e,sp.log(3)))==sp.Rational(3,16))
check(sp.simplify(A.subs(e,sp.log(3)))==sp.log(4));close(math.log(4),1.386294,atol=.0000005)
loglik=3*e-4*A;check(sp.simplify(sp.diff(loglik,e).subs(e,sp.log(3)))==0)
check(sp.simplify(sp.diff(loglik,e,2).subs(e,sp.log(3)))==-sp.Rational(3,4))
check(sp.simplify(4-4*p)>0)
Pois=sp.exp(e);check(sp.diff(Pois,e)==Pois and sp.diff(Pois,e,2)==Pois);check(Pois.subs(e,sp.log(2))==2)
C=sp.Rational(3,16)*sp.Matrix([[1,2],[2,4]]);check(C.det()==0 and C*sp.Matrix([2,-1])==sp.zeros(2,1))

# Verify citation coverage in the composed article, including copied source blocks.
check(len(re.findall(r'class="cite-ref"',body))>=5)
proper_keys=set(re.findall(r'data-cite-key="([^" ]+)"',body))-{'r_faraway_leafblotch2026'}
check(len(proper_keys)>=2)

for token in ['3/16', '0.75', '0.1875', '3/4', '2,-1']:
    check(token in body)
check("**Your turn.**" in body)
check(len(re.findall(r"^## Check yourself \{#check-yourself\}",body,re.M))==1)
print(f"{SLUG}: {checks} numerical, algebraic and rendered-content checks passed")
