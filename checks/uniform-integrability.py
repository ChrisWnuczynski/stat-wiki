"""Recompute the examples and inspect the generated uniform-integrability article."""
from pathlib import Path
import re
import numpy as np
import sympy as sp
from scipy import stats

ROOT=Path(__file__).resolve().parents[1]
SLUG='uniform-integrability'
source=(ROOT / "research" / "content" / (SLUG+".md")).read_text()
body=(ROOT / "articles" / (SLUG+".qmd")).read_text().split("## See also",1)[0]
assert "Your turn" in body and 'collapse="true"' in body
assert "## Check yourself {#check-yourself}" in body
assert len(re.findall('class="cite-ref"',body))>=5

u=sp.symbols('u',real=True,nonnegative=True)
for n in [1,2,10,100,10000]:
 assert sp.integrate(n,(u,0,sp.Rational(1,n)))==1
 assert sp.integrate(sp.sqrt(n),(u,0,sp.Rational(1,n)))==1/sp.sqrt(n)
 assert sp.integrate(u**n,(u,0,1))==sp.Rational(1,n+1)
for K in [.5,1,5,10,100]:
 n=int(K)+1;assert n>K
 tail=n*(1/n);assert np.isclose(tail,1)
 grid=np.arange(1,100001,dtype=float);val=np.where(np.sqrt(grid)>K,1/np.sqrt(grid),0)
 assert np.max(val)<=1/K
assert '0.1' in body and '1/K' in body

print(SLUG+": numeric and generated-article checks passed")
