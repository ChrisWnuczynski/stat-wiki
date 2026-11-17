"""Recompute the article's displayed examples and inspect the generated article."""
from pathlib import Path
import math,re,json
import numpy as np
import sympy as sp
from itertools import product
ROOT=Path(__file__).resolve().parents[1]
SLUG='normal-normal-conjugacy'
article=(ROOT / "articles" / (SLUG+".qmd")).read_text(encoding="utf-8")
body=article.split("## See also",1)[0]
checks=0
def check(condition):
    global checks
    assert condition, SLUG
    checks+=1
def close(actual,expected,rtol=1e-10,atol=1e-12):
    check(np.allclose(np.asarray(actual,dtype=float),np.asarray(expected,dtype=float),rtol=rtol,atol=atol))

from scipy.stats import norm
P=.25;h=0.
for x in [8.,12.]:P+=.25;h+=x/4
close([P,h,h/P,1/P],[.75,5,20/3,4/3]);close(norm.ppf([.025,.975],loc=h/P,scale=math.sqrt(1/P)),[4.4034952,8.92983813],atol=1e-8)
close([(8/4)/(.25+.25),1/(.25+.25)],[4,2])
close([(h+10/4)/(P+.25),1/(P+.25)],[7.5,1]);close(4/4,1)
m=sp.symbols('mu',real=True);P0,H0,ndata,s2,sumx=sp.symbols('P0 H0 n s2 sumx',positive=True)
Pn=P0+ndata/s2;hn=H0+sumx/s2
check(sp.simplify(sp.diff(-sp.Rational(1,2)*(Pn*m*m-2*hn*m)+Pn*(m-hn/Pn)**2/2,m))==0)
# Unequal known variances and batch-order independence.
vs=np.array([1.,4.,9.]);xs=np.array([2.,4.,8.]);pp=.5+sum(1/vs);hh=1+sum(xs/vs)
for perm in product([0,1,2],repeat=3):
 if len(set(perm))==3:close([.5+sum(1/vs[list(perm)]),1+sum(xs[list(perm)]/vs[list(perm)])],[pp,hh])

# Verify citation coverage in the composed article, including copied source blocks.
check(len(re.findall(r'class="cite-ref"',body))>=5)
proper_keys=set(re.findall(r'data-cite-key="([^" ]+)"',body))-{'r_faraway_leafblotch2026'}
check(len(proper_keys)>=2)

for token in ['20/3', '4/3', '4.403495', '8.929838', '7.5']:
    check(token in body)
check("**Your turn.**" in body)
check(len(re.findall(r"^## Check yourself \{#check-yourself\}",body,re.M))==1)
print(f"{SLUG}: {checks} numerical, algebraic and rendered-content checks passed")
