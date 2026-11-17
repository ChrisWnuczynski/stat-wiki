"""Recompute the article's displayed examples and inspect the generated article."""
from pathlib import Path
import math,re,json
import numpy as np
import sympy as sp
from itertools import product
ROOT=Path(__file__).resolve().parents[1]
SLUG='normal-inverse-gamma-variance-update'
article=(ROOT / "articles" / (SLUG+".qmd")).read_text(encoding="utf-8")
body=article.split("## See also",1)[0]
checks=0
def check(condition):
    global checks
    assert condition, SLUG
    checks+=1
def close(actual,expected,rtol=1e-10,atol=1e-12):
    check(np.allclose(np.asarray(actual,dtype=float),np.asarray(expected,dtype=float),rtol=rtol,atol=atol))

from scipy.stats import invgamma
x=np.array([8.,10.,12.]);mu=10.;Q=sum((x-mu)**2);a=2+len(x)/2;b=3+Q/2
close([Q,a,b],[8,3.5,7]);close(invgamma.mean(a,scale=b),2.8);close(b/(a+1),14/9);close(invgamma.var(a,scale=b),392/75)
close(invgamma.ppf([.05,.95],a,scale=b),[.99522714,6.4595015],atol=1e-8)
close([a+.5,b,b/(a+.5-1)],[4,7,7/3]);check(math.isinf(invgamma.mean(.8,scale=1)))
v,z=sp.symbols('v z',positive=True);aa,bb=sp.symbols('a b',positive=True)
check(sp.simplify((v**(-aa-1)*sp.exp(-bb/v)).subs(v,1/z)/z**2-z**(aa-1)*sp.exp(-bb*z))==0)
check(sp.solve(sp.diff((-aa-1)*sp.log(v)-bb/v,v),v)==[bb/(aa+1)])
close(sum((x-mu)**2),sum((x-x.mean())**2)+len(x)*(x.mean()-mu)**2)

# Verify citation coverage in the composed article, including copied source blocks.
check(len(re.findall(r'class="cite-ref"',body))>=5)
proper_keys=set(re.findall(r'data-cite-key="([^" ]+)"',body))-{'r_faraway_leafblotch2026'}
check(len(proper_keys)>=2)

for token in ['392/75', '0.995227', '6.459501', '7/3', '14/9']:
    check(token in body)
check("**Your turn.**" in body)
check(len(re.findall(r"^## Check yourself \{#check-yourself\}",body,re.M))==1)
print(f"{SLUG}: {checks} numerical, algebraic and rendered-content checks passed")
