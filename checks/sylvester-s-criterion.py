"""Independent calculations and generated-output checks for this article."""
from pathlib import Path
import re
ROOT=Path(__file__).resolve().parents[1]
import sympy as s
import numpy as np
A=s.Matrix([[2,1,0],[1,2,1],[0,1,2]])
minor=[A[:k,:k].det() for k in range(1,4)]
assert minor==[2,3,4]
assert A.eigenvals()=={2:1,2-s.sqrt(2):1,2+s.sqrt(2):1}
assert [minor[i]/([1]+minor)[i] for i in range(3)]==[2,s.Rational(3,2),s.Rational(4,3)]
B=s.diag(0,-1);assert B[0,0]==0 and B.det()==0 and B[1,1]==-1
C=-s.eye(2);assert C.det()==1 and C[0,0]==-1
K=np.exp(-((np.arange(3)[:,None]-np.arange(3)[None,:])**2)/2)
assert abs(np.linalg.det(K)-.345499615504109)<1e-14
assert all(np.linalg.det(K[:k,:k])>0 for k in range(1,4))

# Verify the diagonal-perturbation determinant expansion by principal minors.
from itertools import combinations
eps=s.symbols('eps');aa,bb,cc,dd,ee,ff=s.symbols('aa bb cc dd ee ff')
G=s.Matrix([[aa,dd,ee],[dd,bb,ff],[ee,ff,cc]])
expanded=eps**3
for size in range(1,4):
    expanded+=eps**(3-size)*sum(G.extract(indices,indices).det() for indices in combinations(range(3),size))
assert s.expand((G+eps*s.eye(3)).det()-expanded)==0
source=(ROOT/"research/content/sylvester-s-criterion.md").read_text()
article=(ROOT/"articles/sylvester-s-criterion.qmd").read_text().split("## See also",1)[0]
for needle in ['2-\\sqrt2', '3/2', '4/3']:
    assert needle in source and needle in article, needle
assert len(re.findall(r"\{\{cite:[^}]+\}\}", source))>=5
assert len(set(re.findall(r"\{\{cite:([^}]+)\}\}",source)))>=2
assert "Your turn" in article and 'collapse="true" title="Answer"' in article
assert "## Check yourself {#check-yourself}" in article
print("sylvester-s-criterion: calculations and article checks passed")
