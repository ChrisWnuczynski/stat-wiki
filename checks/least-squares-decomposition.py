"""Recompute worked examples and inspect generated mathematical claims."""
from pathlib import Path
import re
import sympy as sp
ROOT=Path(__file__).resolve().parents[1]
text=(ROOT / "articles" / "least-squares-decomposition.qmd").read_text(encoding="utf-8")
assert "Your turn" in text
assert "## Check yourself {#check-yourself}" in text
assert len(re.findall('class="cite-ref"',text))>=5
assert len(set(re.findall('data-cite-key="([^\"]+)',text)))>=2

X=sp.Matrix([[1,0],[1,1],[1,2]]);y=sp.Matrix([1,2,2]);hat=(X.T*X).inv()*X.T*y
assert hat==sp.Matrix([sp.Rational(7,6),sp.Rational(1,2)])
r=y-X*hat;assert r==sp.Matrix([-sp.Rational(1,6),sp.Rational(1,3),-sp.Rational(1,6)]) and X.T*r==sp.zeros(2,1)
b=sp.Matrix([1,1]);d=b-hat;assert (r.T*r)[0]==sp.Rational(1,6)
assert ((y-X*b).T*(y-X*b))[0]==1 and ((X*d).T*(X*d))[0]==sp.Rational(5,6)
assert (r.T*X*d)[0]==0
assert (r.T*r)[0]+sum(v*v for v in X*sp.Matrix([1,0]))==sp.Rational(19,6)
for token in ['19/6','5/6','1/6']:assert token in text,token

print("least-squares-decomposition: symbolic/numerical recomputation and article assertions passed")
