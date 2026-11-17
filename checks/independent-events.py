"""Recompute the article's displayed examples and inspect the generated article."""
from pathlib import Path
import math,re,json
import numpy as np
import sympy as sp
from itertools import product
ROOT=Path(__file__).resolve().parents[1]
SLUG='independent-events'
article=(ROOT / "articles" / (SLUG+".qmd")).read_text(encoding="utf-8")
body=article.split("## See also",1)[0]
checks=0
def check(condition):
    global checks
    assert condition, SLUG
    checks+=1
def close(actual,expected,rtol=1e-10,atol=1e-12):
    check(np.allclose(np.asarray(actual,dtype=float),np.asarray(expected,dtype=float),rtol=rtol,atol=atol))

outcomes=list(product([0,1],repeat=2))
A={o for o in outcomes if o[0]==1}; B={o for o in outcomes if o[1]==1};C={o for o in outcomes if o[0]==o[1]}
P=lambda x:sp.Rational(len(x),len(outcomes))
check(all(P(e)==sp.Rational(1,2) for e in [A,B,C]))
check(all(P(e&f)==P(e)*P(f) for e,f in [(A,B),(A,C),(B,C)]))
check(P(A&B&C)==sp.Rational(1,4) and P(A)*P(B)*P(C)==sp.Rational(1,8))
check(P(A&C)/P(C)==sp.Rational(1,2) and P(A&B&C)/P(C)==sp.Rational(1,2))
check(P(A&(set(outcomes)-C))==sp.Rational(1,4))
q=sp.Rational(1,10)
check((1-q*q)**2==sp.Rational(9801,10000));close(1/float(1-(1-q*q)**2),50,rtol=.01)
check((1-q)*(1-q*q)==sp.Rational(891,1000))
check(sp.Rational(1,5)*sp.Rational(3,10)==sp.Rational(3,50))
check(sp.Rational(1,10)*sp.Rational(1,5)==sp.Rational(1,50))

# Verify citation coverage in the composed article, including copied source blocks.
check(len(re.findall(r'class="cite-ref"',body))>=5)
proper_keys=set(re.findall(r'data-cite-key="([^" ]+)"',body))-{'r_faraway_leafblotch2026'}
check(len(proper_keys)>=2)

for token in ['0.02', '1/8', '1/4', 'Pairwise', 'probability zero']:
    check(token in body)
check("**Your turn.**" in body)
check(len(re.findall(r"^## Check yourself \{#check-yourself\}",body,re.M))==1)
print(f"{SLUG}: {checks} numerical, algebraic and rendered-content checks passed")
