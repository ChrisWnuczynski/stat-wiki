"""Recompute the worked calculations and inspect the generated article."""
from pathlib import Path
import re
root = Path(__file__).resolve().parents[1]
source = (root / "research" / "content" / (Path(__file__).stem + ".md")).read_text()
article = (root / "articles" / (Path(__file__).stem + ".qmd")).read_text()
body = article.split("## See also", 1)[0]
assert len(re.findall(r"\{\{cite:", source)) >= 5
assert len(set(re.findall(r"\{\{cite:([^}]+)", source))) >= 2
assert "Your turn" in body and 'collapse="true"' in body

from scipy.stats import invgamma
from scipy.integrate import quad
from math import gamma
import sympy as sp
n,p,R=10,2,16
a,b=(n-p)/2,R/2
assert (a,b)==(4,8)
assert abs(invgamma.mean(a,scale=b)-8/3)<1e-14
assert abs(invgamma.var(a,scale=b)-32/9)<1e-14
v=sp.symbols('v',positive=True)
logf=-(a+1)*sp.log(v)-b/v
assert sp.simplify(sp.diff(logf,v).subs(v,sp.Rational(8,5)))==0
assert abs(quad(lambda x: b**a/gamma(a)*x**(-a-1)*__import__('math').exp(-b/x),0,__import__('math').inf)[0]-1)<1e-9
assert invgamma.mean(1,scale=2)==float('inf')
assert '2.666667' in body and '32/9' in body

print("marginal-variance-posterior checks passed")
