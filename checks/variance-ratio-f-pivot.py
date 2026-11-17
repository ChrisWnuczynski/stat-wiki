"""Recompute examples independently and inspect the generated article."""
import numpy as np
import math

from scipy.stats import f
q=f.ppf([.025,.975],8,8);interval=4/q[::-1]
assert np.allclose(q,[.22556764660698236,4.433259889182374])
assert np.allclose(interval,[.90227058642793,17.733039556729505])
assert np.allclose(1/interval[::-1],[.05639191165174559,1.1083149722955934])
assert abs(q.prod()-1)<1e-13 and abs(f.median(8,8)-1)<1e-13
assert abs(f.mean(8,8)-4/3)<1e-14
ratio=(14.1/14.3)**2
assert abs(ratio-.9722235806151889)<1e-14
assert np.allclose([ratio/1.762,ratio*1.762],[.5517727472276894,1.7130579490439628])
# Orthogonal transformation of a standard normal sample isolates the mean.
v=np.ones(9)/3;Q=np.linalg.qr(np.c_[v,np.eye(9)[:,1:]])[0]
assert np.allclose(Q.T@Q,np.eye(9))
z=np.arange(9.)-1
assert abs(np.sum((z-z.mean())**2)-np.sum((Q.T@z)[1:]**2))<1e-12

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

for token in ['0.902271', '17.733040']:
    assert token in body, (slug,token)
print(slug+" checks passed")
