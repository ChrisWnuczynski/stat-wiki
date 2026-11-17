"""Recompute the article's displayed examples and inspect the generated article."""
from pathlib import Path
import math,re,json
import numpy as np
import sympy as sp
from itertools import product
ROOT=Path(__file__).resolve().parents[1]
SLUG='non-negative-matrix-factorisation'
article=(ROOT / "articles" / (SLUG+".qmd")).read_text(encoding="utf-8")
body=article.split("## See also",1)[0]
checks=0
def check(condition):
    global checks
    assert condition, SLUG
    checks+=1
def close(actual,expected,rtol=1e-10,atol=1e-12):
    check(np.allclose(np.asarray(actual,dtype=float),np.asarray(expected,dtype=float),rtol=rtol,atol=atol))

V=np.array([[1.,2.],[3.,4.]]);W=np.ones((2,1));H=np.ones((1,2));loss=lambda: .5*np.sum((V-W@H)**2)
close(loss(),7);H*= (W.T@V)/(W.T@W@H);close(H,[[2,3]]);close(loss(),2)
W*= (V@H.T)/(W@H@H.T);close(W,[[8/13],[18/13]]);close(W@H,[[16/13,24/13],[36/13,54/13]]);close(loss(),1/13)
close(np.linalg.det(V),-2);check(np.linalg.matrix_rank(V)==2)
close((W*2)@(H/2),W@H)
U=np.array([[1.,2.],[2.,4.]]);close(np.array([[1.],[2.]])@np.array([[1.,2.]]),U)
# A zero factor entry remains zero under a multiplicative update with finite positive denominator.
w=np.array([[0.,1.],[1.,1.]]);h=np.array([[2.,3.],[1.,1.]]);denominator=w@h@h.T;check(np.all(denominator>0));new_w=w*((V@h.T)/denominator);close(new_w[0,0],0)

# Verify citation coverage in the composed article, including copied source blocks.
check(len(re.findall(r'class="cite-ref"',body))>=5)
proper_keys=set(re.findall(r'data-cite-key="([^" ]+)"',body))-{'r_faraway_leafblotch2026'}
check(len(proper_keys)>=2)

for token in ['8/13', '18/13', '1/13', 'seven', 'two']:
    check(token in body)
check("**Your turn.**" in body)
check(len(re.findall(r"^## Check yourself \{#check-yourself\}",body,re.M))==1)
print(f"{SLUG}: {checks} numerical, algebraic and rendered-content checks passed")
