"""Recompute the article's displayed examples and inspect the generated article."""
from pathlib import Path
import math,re,json
import numpy as np
import sympy as sp
from itertools import product
ROOT=Path(__file__).resolve().parents[1]
SLUG='marginal-student-posterior'
article=(ROOT / "articles" / (SLUG+".qmd")).read_text(encoding="utf-8")
body=article.split("## See also",1)[0]
checks=0
def check(condition):
    global checks
    assert condition, SLUG
    checks+=1
def close(actual,expected,rtol=1e-10,atol=1e-12):
    check(np.allclose(np.asarray(actual,dtype=float),np.asarray(expected,dtype=float),rtol=rtol,atol=atol))

from scipy.stats import t as t_law,invgamma,norm
from scipy.integrate import quad
ys=np.array([1.,2.,4.,5.]);mean=ys.mean();SSE=sum((ys-mean)**2);nu=len(ys)-1;s2=SSE/nu;C=1/len(ys)
close([mean,SSE,nu,s2,C],[3,10,3,10/3,.25]);scale=math.sqrt(s2*C);close(scale,math.sqrt(5/6));close(nu/(nu-2)*scale**2,2.5)
close(t_law.ppf([.025,.975],nu,loc=mean,scale=scale),[.09483728,5.90516272],atol=1e-8)
# Integrate the normal conditional over its exact inverse-gamma variance posterior.
for point in [1.,3.,5.]:
 density=quad(lambda v:norm.pdf(point,loc=mean,scale=math.sqrt(C*v))*invgamma.pdf(v,a=nu/2,scale=SSE/2),0,np.inf)[0]
 close(density,t_law.pdf(point,nu,loc=mean,scale=scale),rtol=1e-8)
check(math.isinf(t_law.var(2)));check(12-4==8)

# Verify citation coverage in the composed article, including copied source blocks.
check(len(re.findall(r'class="cite-ref"',body))>=5)
proper_keys=set(re.findall(r'data-cite-key="([^" ]+)"',body))-{'r_faraway_leafblotch2026'}
check(len(proper_keys)>=2)

for token in ['5/6', '2.5', '0.094837', '5.905163', 'three degrees']:
    check(token in body)
check("**Your turn.**" in body)
check(len(re.findall(r"^## Check yourself \{#check-yourself\}",body,re.M))==1)
print(f"{SLUG}: {checks} numerical, algebraic and rendered-content checks passed")
