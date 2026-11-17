"""Recompute the article's displayed examples and inspect the generated article."""
from pathlib import Path
import math,re,json
import numpy as np
import sympy as sp
from itertools import product
ROOT=Path(__file__).resolve().parents[1]
SLUG='least-squares-estimators-are-unbiased'
article=(ROOT / "articles" / (SLUG+".qmd")).read_text(encoding="utf-8")
body=article.split("## See also",1)[0]
checks=0
def check(condition):
    global checks
    assert condition, SLUG
    checks+=1
def close(actual,expected,rtol=1e-10,atol=1e-12):
    check(np.allclose(np.asarray(actual,dtype=float),np.asarray(expected,dtype=float),rtol=rtol,atol=atol))

X=sp.Matrix([[1,0],[1,1],[1,2]]); A=(X.T*X).inv()*X.T
check(A==sp.Matrix([[sp.Rational(5,6),sp.Rational(1,3),-sp.Rational(1,6)],[-sp.Rational(1,2),0,sp.Rational(1,2)]]))
check(A*X==sp.eye(2)); beta=sp.Matrix([1,2])
fits=[A*(X*beta+sp.Matrix(e)) for e in product([-1,1],repeat=3)]
check(sum(fits,sp.zeros(2,1))/len(fits)==beta)
cov=sum([(b-beta)*(b-beta).T for b in fits],sp.zeros(2))/len(fits)
check(cov==sp.Matrix([[sp.Rational(5,6),-sp.Rational(1,2)],[-sp.Rational(1,2),sp.Rational(1,2)]]))
check(A*sp.Matrix([0,1,2])==sp.Matrix([0,1]))
check(A*sp.ones(3,1)/2==sp.Matrix([sp.Rational(1,2),0]))
check(A*sp.diag(1,4,9)*A.T==sp.Matrix([[sp.Rational(25,18),-sp.Rational(7,6)],[-sp.Rational(7,6),sp.Rational(5,2)]]))
# The source's simple-regression slope weights sum to zero and have weighted x sum one.
xs=[sp.Rational(i) for i in [0,1,2]]; xb=sum(xs)/3;ss=sum((x-xb)**2 for x in xs);weights=[(x-xb)/ss for x in xs]
check(sum(weights)==0 and sum(w*x for w,x in zip(weights,xs))==1)

# Verify citation coverage in the composed article, including copied source blocks.
check(len(re.findall(r'class="cite-ref"',body))>=5)
proper_keys=set(re.findall(r'data-cite-key="([^" ]+)"',body))-{'r_faraway_leafblotch2026'}
check(len(proper_keys)>=2)

for token in ['5/6', '1/2', 'eight equally likely', '(0,1)', '0.5']:
    check(token in body)
check("**Your turn.**" in body)
check(len(re.findall(r"^## Check yourself \{#check-yourself\}",body,re.M))==1)
print(f"{SLUG}: {checks} numerical, algebraic and rendered-content checks passed")
