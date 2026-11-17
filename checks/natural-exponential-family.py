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

import sympy as sp
from math import log
eta=sp.symbols('eta',real=True)
A=sp.exp(eta)
assert sp.simplify(sp.diff(A,eta,2)-sp.exp(eta))==0
assert sp.diff(6*eta-3*A,eta).subs(eta,sp.log(2))==0
assert -sp.diff(6*eta-3*A,eta,2).subs(eta,sp.log(2))==6
assert abs(log(2)-.6931471805599453)<1e-14
assert abs(log(2/3)+.40546510810816444)<1e-14
r,mu=sp.symbols('r mu',positive=True)
theta=r/(r+mu)
assert sp.simplify((1-theta)-mu/(r+mu))==0
assert '-0.405465' in body and '0.693147' in body


# Natural-to-mean reparameterization of the Poisson score/information.
import sympy as sp
lam,n,total=sp.symbols('lam n total',positive=True)
ell=-n*lam+total*sp.log(lam)
score=sp.diff(ell,lam)
assert sp.simplify(score-(total/lam-n))==0
info=(-sp.diff(score,lam)).subs(total,n*lam)
assert sp.simplify(info-n/lam)==0
assert sp.simplify(1/info-lam/n)==0

print("natural-exponential-family checks passed")
