"""Independent numerical and algebraic checks for gaussian-process."""
import math
from pathlib import Path
import numpy as np


k=math.exp(-.5);K=np.array([[1,k],[k,1.]])
assert np.linalg.eigvalsh(K).min()>0
mean=2*k/1.25;var=1-k*k/1.25
assert abs(mean-.9704490555402134)<1e-14
assert abs(var-.7056964470628462)<1e-14
assert np.allclose(np.linalg.solve(np.array([[1.25]]),[2])*k,[mean])
C=np.minimum.outer([0.,1.,2.],[0.,1.,2.]);assert np.linalg.eigvalsh(C).min()>=0
assert abs(np.linalg.det(np.array([[1,.9,.9],[.9,1,-.9],[.9,-.9,1]]))+2.888)<1e-12

assert abs(var+.25-.9556964470628462)<1e-14

import sympy as sp
A=sp.Matrix([[2,1],[1,3]]); k=sp.Matrix([sp.Rational(1,2),sp.Rational(1,3)])
joint=A.row_join(k).col_join(k.T.row_join(sp.Matrix([[1]])))
T=sp.eye(3); T[2,0:2]=-k.T*A.inv(); transformed=T*joint*T.T
assert transformed[2,0]==transformed[2,1]==0 and transformed[2,2]>0

root=Path(__file__).resolve().parents[1]
body=(root / "articles" / "gaussian-process.qmd").read_text()
source=(root / "research/content" / "gaussian-process.md").read_text()
assert "**Your turn.**" in body
assert len(__import__("re").findall(r"\{\{cite:",source)) >= 5
for token in ['0.970449', '0.705696', '0.955696']:
    assert token in body, (token, "gaussian-process")
print("gaussian-process: numerical and algebraic checks passed")
