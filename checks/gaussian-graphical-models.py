"""Recompute the examples and inspect the generated gaussian-graphical-models article."""
from pathlib import Path
import re
import numpy as np
import sympy as sp
from scipy import stats

ROOT=Path(__file__).resolve().parents[1]
SLUG='gaussian-graphical-models'
source=(ROOT / "research" / "content" / (SLUG+".md")).read_text()
body=(ROOT / "articles" / (SLUG+".qmd")).read_text().split("## See also",1)[0]
assert "Your turn" in body and 'collapse="true"' in body
assert "## Check yourself {#check-yourself}" in body
assert len(re.findall('class="cite-ref"',body))>=5

S = sp.Matrix([[1,sp.Rational(1,2),sp.Rational(1,4)],[sp.Rational(1,2),1,sp.Rational(1,2)],[sp.Rational(1,4),sp.Rational(1,2),1]])
K = S.inv()
assert K == sp.Matrix([[sp.Rational(4,3),sp.Rational(-2,3),0],[sp.Rational(-2,3),sp.Rational(5,3),sp.Rational(-2,3)],[0,sp.Rational(-2,3),sp.Rational(4,3)]])
assert sp.simplify(-K[0,1]/sp.sqrt(K[0,0]*K[1,1])-1/sp.sqrt(5))==0
assert -K[1,0]/K[1,1] == sp.Rational(2,5)
Q=sp.Matrix([[2,-1,0],[-1,3,-1],[0,-1,2]])
assert Q.inv()==sp.Matrix([[5,2,1],[2,4,2],[1,2,5]])/8
for rho in [sp.Rational(3,5),sp.Rational(4,5)]:
 C=sp.Matrix([[rho**abs(i-j) for j in range(4)] for i in range(4)]); P=C.inv()
 assert all(P[i,j]==0 for i in range(4) for j in range(4) if abs(i-j)>1)
C=np.array([[.6**abs(i-j) for j in range(4)] for i in range(4)]);P=np.linalg.inv(C)
assert np.allclose(P,[[1.5625,-.9375,0,0],[-.9375,2.125,-.9375,0],[0,-.9375,2.125,-.9375],[0,0,-.9375,1.5625]])
assert np.isclose(.9375/2.125,.4411764705882353)
assert np.isclose(1/2.125,.47058823529411764)
assert '0.4472' in body

print(SLUG+": numeric and generated-article checks passed")
