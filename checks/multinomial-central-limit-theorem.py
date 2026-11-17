"""Recompute the article's displayed examples and inspect the generated article."""
from pathlib import Path
import math,re,json
import numpy as np
import sympy as sp
from itertools import product
ROOT=Path(__file__).resolve().parents[1]
SLUG='multinomial-central-limit-theorem'
article=(ROOT / "articles" / (SLUG+".qmd")).read_text(encoding="utf-8")
body=article.split("## See also",1)[0]
checks=0
def check(condition):
    global checks
    assert condition, SLUG
    checks+=1
def close(actual,expected,rtol=1e-10,atol=1e-12):
    check(np.allclose(np.asarray(actual,dtype=float),np.asarray(expected,dtype=float),rtol=rtol,atol=atol))

p=np.array([.2,.3,.5]);S=np.diag(p)-np.outer(p,p)
close(S,[[.16,-.06,-.10],[-.06,.21,-.15],[-.10,-.15,.25]]);close(S@np.ones(3),0);check(np.linalg.matrix_rank(S)==2);close(np.linalg.det(S),0)
c=np.array([1,-1,0.]);close(c@p,-.1);close(c@S@c/100,.0049);close(math.sqrt(c@S@c/100),.07)
close((S[0,0]+S[1,1])/100,.0037);close(S[0,1]/100,-.0006)
u=np.array([1,1,0.]);close(u@S@u/100,.0025)
# Enumerate one categorical indicator to verify all moments used by Cramér–Wold.
ind=np.eye(3);close(p@ind,p);close(sum(p[i]*np.outer(ind[i]-p,ind[i]-p) for i in range(3)),S)
# Boundary categories have zero rather than positive variance.
p0=np.array([0.,.4,.6]);S0=np.diag(p0)-np.outer(p0,p0);check(np.array_equal(S0[0],np.zeros(3)))

# Verify citation coverage in the composed article, including copied source blocks.
check(len(re.findall(r'class="cite-ref"',body))>=5)
proper_keys=set(re.findall(r'data-cite-key="([^" ]+)"',body))-{'r_faraway_leafblotch2026'}
check(len(proper_keys)>=2)

for token in ['0.16', '-0.06', '0.0049', '0.07', '0.0025']:
    check(token in body)
check("**Your turn.**" in body)
check(len(re.findall(r"^## Check yourself \{#check-yourself\}",body,re.M))==1)
print(f"{SLUG}: {checks} numerical, algebraic and rendered-content checks passed")
