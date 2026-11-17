"""Recompute article examples independently; public lidar data are from SemiPar."""
from pathlib import Path
import re
import sympy as sp
ROOT=Path(__file__).resolve().parents[1]
text=(ROOT / "articles" / "mean-and-variance-of-an-exponential-family.qmd").read_text(encoding="utf-8")
assert "Your turn" in text
assert "## Check yourself {#check-yourself}" in text
assert len(re.findall('class="cite-ref"',text))>=5
assert len(set(re.findall('data-cite-key="([^\"]+)',text)))>=2

e=sp.symbols('e',real=True)
A=sp.log(1+sp.exp(e));m=sp.diff(A,e);v=sp.diff(A,e,2)
assert sp.simplify(m.subs(e,sp.log(4)))==sp.Rational(4,5)
assert sp.simplify(v.subs(e,sp.log(4)))==sp.Rational(4,25)
assert 5*sp.Rational(4,5)==4 and 5*sp.Rational(4,25)==sp.Rational(4,5)
G=-3*sp.log(-e)
assert sp.diff(G,e).subs(e,-sp.Rational(1,2))==6 and sp.diff(G,e,2).subs(e,-sp.Rational(1,2))==12
assert sp.diff(sp.exp(e),e).subs(e,sp.log(3))==3
# Normal, Poisson and binomial examples in the theorem's copied derivation.
n=sp.symbols('n',positive=True);c=-n*sp.log(1+sp.exp(e));p=sp.exp(e)/(1+sp.exp(e))
assert sp.simplify(-sp.diff(c,e)-n*p)==0
assert sp.simplify(-sp.diff(c,e,2)-n*p*(1-p))==0
assert -sp.diff(-e**2/2,e)==e and -sp.diff(-e**2/2,e,2)==1
assert -sp.diff(-sp.exp(e),e,2)==sp.exp(e)

# Recompute the Gamma log-link worked answer symbolically.
y,mu,k,phi=sp.symbols('y mu k phi',positive=True)
logf=k*sp.log(k)-sp.loggamma(k)-k*sp.log(mu)+(k-1)*sp.log(y)-k*y/mu
reprf=(-y/mu-sp.log(mu))/phi+sp.log(1/phi)/phi-sp.loggamma(1/phi)+(1/phi-1)*sp.log(y)
assert sp.simplify(logf-reprf.subs(phi,1/k))==0
assert sp.simplify(sp.diff(logf,mu)*mu-k*(y/mu-1))==0
assert k/(k/mu)==mu and sp.simplify(k/(k/mu)**2-mu**2/k)==0
print("mean-and-variance-of-an-exponential-family: numerical examples and generated-article assertions passed")
