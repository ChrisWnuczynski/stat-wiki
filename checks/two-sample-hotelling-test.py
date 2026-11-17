"""Recompute examples independently and inspect the generated article."""
import numpy as np
import math

from scipy.stats import f,t
n1=n2=10;p=2;N=n1+n2;d=np.array([1.5,1.]);S=np.array([[2.,1],[1,2]])
q=d@np.linalg.solve(S,d);T=n1*n2/N*q;F=(N-p-1)/(p*(N-2))*T
assert abs(q-7/6)<1e-14 and abs(T-35/6)<1e-14
assert abs(F-2.7546296296296293)<1e-14
assert abs(f.ppf(.95,2,17)-3.5915305684750805)<1e-12
assert abs(f.sf(F,2,17)-.09199105576054485)<1e-14
A=np.diag([2.,1]);d2=A@d;S2=A@S@A.T
assert np.allclose(d2,[3,1]) and np.allclose(S2,[[8,2],[2,2]])
assert abs(d2@np.linalg.solve(S2,d2)-q)<1e-14
assert abs(f.ppf(.95,1,18)-t.ppf(.975,18)**2)<1e-10
S_pool=(np.array([[18.,6],[6,12]])+np.array([[30.,-9],[-9,24]]))/23
assert np.allclose(S_pool,np.array([[48.,-3],[-3,36]])/23)
assert np.linalg.eigvalsh(S_pool).min()>0

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

for token in ['2.754630', '0.091991']:
    assert token in body, (slug,token)
print(slug+" checks passed")
