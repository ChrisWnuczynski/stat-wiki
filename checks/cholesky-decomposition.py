"""Recompute examples independently and inspect the generated article."""
import numpy as np
import math

A=np.array([[4.,2],[2,3]]);L=np.linalg.cholesky(A)
assert np.allclose(L,[[2,0],[1,math.sqrt(2)]])
assert np.allclose(L@L.T,A) and not np.allclose(L@L,A)
b=np.array([1.,2]);v=np.linalg.solve(L,b);x=np.linalg.solve(L.T,v)
assert np.allclose(x,[-1/8,3/4])
assert abs(b@x-11/8)<1e-14 and abs(v@v-11/8)<1e-14
assert abs(np.linalg.det(A)-8)<1e-13
assert abs(2*np.log(L.diagonal()).sum()-2.0794415416798357)<1e-14
vals,U=np.linalg.eigh(A);B=U@np.diag(np.sqrt(vals))
assert np.allclose(B@B.T,A)
assert np.allclose(vals,[(7-math.sqrt(17))/2,(7+math.sqrt(17))/2])
A2=np.array([[9.,3],[3,2]]);assert np.allclose(np.linalg.cholesky(A2),[[3,0],[1,1]])
assert abs(np.linalg.det(A2)-9)<1e-12
rng=np.random.default_rng(17);X=rng.normal(size=(80,100));X-=X.mean(axis=0)
assert np.linalg.matrix_rank(X.T@X)<=79
# Verify the block construction used in the induction.
a=4.;r=np.array([2.]);C=np.array([[3.]])-np.outer(r,r)/a
assert C[0,0]==2

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

for token in ['2.079442', '1.375']:
    assert token in body, (slug,token)
print(slug+" checks passed")
