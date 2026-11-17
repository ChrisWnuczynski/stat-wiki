"""Recompute examples independently and inspect the generated article."""
import numpy as np
import math

from scipy.optimize import minimize_scalar
b=np.array([2.4,-.9,.5,-.1]);lam=2
soft=lambda x,t:np.sign(x)*np.maximum(np.abs(x)-t,0)
lasso=soft(b,lam/2);ridge=b/(1+lam);hard=b*(abs(b)>math.sqrt(lam))
assert np.allclose(lasso,[1.4,0,0,0])
assert np.allclose(ridge,[.8,-.3,1/6,-1/30])
assert np.allclose(hard,[2.4,0,0,0])
assert np.allclose(soft(b,2.4),0)
assert np.allclose(soft(b,1)/2,[.7,0,0,0])
for bj,beta in zip(b,lasso):
 grid=np.linspace(-4,4,20001)
 obj=(grid-bj)**2+lam*abs(grid)
 assert (beta-bj)**2+lam*abs(beta)<=obj.min()+1e-10
 if beta==0:assert abs(2*bj)<=lam
 else:assert abs(2*(beta-bj)+lam*np.sign(beta))<1e-14
X=np.ones((2,2));y=np.array([1.,3])
assert np.allclose(np.linalg.eigvalsh(X.T@X),[0,4])
assert np.allclose(np.linalg.solve(X.T@X+np.eye(2),X.T@y),[.8,.8])
old=np.array([3,-1.5,.8,-.3,.1])
assert np.allclose(soft(old,.5),[2.5,-1,.3,0,0])

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

for token in ['1.4', '0.7']:
    assert token in body, (slug,token)
print(slug+" checks passed")
