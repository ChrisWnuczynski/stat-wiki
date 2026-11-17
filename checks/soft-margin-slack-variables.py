"""Recompute examples independently and inspect the generated article."""
import numpy as np
import math

from scipy.optimize import linprog
m=np.array([1.5,.4,-.2]);xi=np.maximum(0,1-m)
assert np.allclose(xi,[0,.6,1.2]) and abs(xi.sum()-1.8)<1e-14
assert abs(2*xi.sum()-3.6)<1e-14
assert 1-m[2]>1 and 0<m[1]<1
# The fixed-score slack subproblem is a linear program.
lp=linprog(np.ones(3),A_ub=-np.eye(3),b_ub=m-1,bounds=[(0,None)]*3,method='highs')
assert lp.success and np.allclose(lp.x,xi)
for b in np.linspace(-2,2,81):
 loss=max(0,1-b)+max(0,1+b)
 assert loss>=2-1e-14
 if abs(b)<=1:assert abs(loss-2)<1e-14
assert (1-.25)*4==3
C=2
for alpha,margin,slack in [(0,1.5,0),(1.3,1,0),(2,.4,.6)]:
 mu=C-alpha
 assert mu>=0 and abs(mu*slack)<1e-14
 assert abs(alpha*(margin-1+slack))<1e-14

# Generated article checks.
from pathlib import Path
import re
root=Path(__file__).resolve().parents[1]
slug=Path(__file__).stem
source=(root/"research"/"content"/(slug+".md")).read_text()
body=(root/"articles"/(slug+".qmd")).read_text().split("## See also",1)[0]
assert len(re.findall(r"\{\{cite:",source))>=5
assert len(set(re.findall(r"\{\{cite:([^}]+)",source)))>=2
assert "Your turn" in body and "## Check yourself" in body
check=body.split("## Check yourself",1)[1]
assert check.count('collapse="true" title="Answer"') in {2,3}
assert len(set(re.findall(r"../questions/([\w-]+)\.qmd",check))) in {2,3}

for token in ['3.6', '1.8']:
    assert token in body, (slug,token)
print(slug+" checks passed")
