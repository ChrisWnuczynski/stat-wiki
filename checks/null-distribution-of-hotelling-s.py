"""Recompute the article's displayed examples and inspect the generated article."""
from pathlib import Path
import math,re,json
import numpy as np
import sympy as sp
from itertools import product
ROOT=Path(__file__).resolve().parents[1]
SLUG='null-distribution-of-hotelling-s'
article=(ROOT / "articles" / (SLUG+".qmd")).read_text(encoding="utf-8")
body=article.split("## See also",1)[0]
checks=0
def check(condition):
    global checks
    assert condition, SLUG
    checks+=1
def close(actual,expected,rtol=1e-10,atol=1e-12):
    check(np.allclose(np.asarray(actual,dtype=float),np.asarray(expected,dtype=float),rtol=rtol,atol=atol))

from scipy.stats import f as f_law,t as t_law
n=20;p=2;T2=10;F=(n-p)/(p*(n-1))*T2
close(F,90/19);close(f_law.ppf(.95,p,n-p),3.554557145661787);close(f_law.sf(F,p,n-p),np.float64(0.022243361879432016))
critical=p*(n-1)/(n-p)*f_law.ppf(.95,p,n-p);close(critical,np.float64(7.504065085285995))
close((n-p)/(p*(n-1))*5,45/19);check(45/19<f_law.ppf(.95,p,n-p))
# One dimension gives the square of the usual t statistic and the same tail probability.
close((n-1)/(1*(n-1)),1);close(t_law.ppf(.975,n-1)**2,f_law.ppf(.95,1,n-1))
# Exact affine invariance of the quadratic form and rank bound for centered observations.
y=sp.Matrix([2,3]);S=sp.Matrix([[2,sp.Rational(1,2)],[sp.Rational(1,2),1]]);A=sp.Matrix([[2,1],[-1,3]])
check((y.T*S.inv()*y)[0]==((A*y).T*(A*S*A.T).inv()*(A*y))[0])
rng=np.random.default_rng(162);Z=rng.normal(size=(4,6));Z-=Z.mean(axis=0);check(np.linalg.matrix_rank(Z.T@Z)<=3)

# Verify citation coverage in the composed article, including copied source blocks.
check(len(re.findall(r'class="cite-ref"',body))>=5)
proper_keys=set(re.findall(r'data-cite-key="([^" ]+)"',body))-{'r_faraway_leafblotch2026'}
check(len(proper_keys)>=2)

for token in ['90/19', '0.022243', '7.504065', '45/19']:
    check(token in body)
check("**Your turn.**" in body)
check(len(re.findall(r"^## Check yourself \{#check-yourself\}",body,re.M))==1)
print(f"{SLUG}: {checks} numerical, algebraic and rendered-content checks passed")
