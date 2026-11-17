"""Recompute the article's displayed examples and inspect the generated article."""
from pathlib import Path
import math,re,json
import numpy as np
import sympy as sp
from itertools import product
ROOT=Path(__file__).resolve().parents[1]
SLUG='metropolis-hastings-invariance'
article=(ROOT / "articles" / (SLUG+".qmd")).read_text(encoding="utf-8")
body=article.split("## See also",1)[0]
checks=0
def check(condition):
    global checks
    assert condition, SLUG
    checks+=1
def close(actual,expected,rtol=1e-10,atol=1e-12):
    check(np.allclose(np.asarray(actual,dtype=float),np.asarray(expected,dtype=float),rtol=rtol,atol=atol))

pi=np.array([.8,.2]);Q=np.array([[.1,.9],[.2,.8]])
alpha=np.minimum(1,(pi[None,:]*Q.T)/(pi[:,None]*Q))
close(alpha,[[1,1/18],[1,1]])
P=Q*alpha
for i in range(2):P[i,i]+=1-P[i].sum()
close(P,[[.95,.05],[.2,.8]]);close(pi@P,pi);close(pi[:,None]*P,(pi[:,None]*P).T);close(pi[0]*P[0,1],.04)
accept=(Q*alpha).sum(axis=1);close(accept,[.15,1]);jump=(Q*alpha)/accept[:,None];jump_pi=pi*accept;jump_pi/=jump_pi.sum()
close(jump_pi,[3/8,5/8]);close(jump_pi@jump,jump_pi)
practice=np.array([[.75,.25],[1,0]]);close(pi@practice,pi);close(pi@np.eye(2),pi)
check(np.array_equal(np.eye(2)[0],[1,0]))

# Verify citation coverage in the composed article, including copied source blocks.
check(len(re.findall(r'class="cite-ref"',body))>=5)
proper_keys=set(re.findall(r'data-cite-key="([^" ]+)"',body))-{'r_faraway_leafblotch2026'}
check(len(proper_keys)>=2)

for token in ['1/18', '0.95', '0.05', '0.04', '3/8', '5/8']:
    check(token in body)
check("**Your turn.**" in body)
check(len(re.findall(r"^## Check yourself \{#check-yourself\}",body,re.M))==1)
print(f"{SLUG}: {checks} numerical, algebraic and rendered-content checks passed")
