"""Recompute examples independently and inspect the generated article."""
import numpy as np
import math

from itertools import product
from scipy.stats import binom
n=8;p=.3;xs=np.array(list(product([0,1],repeat=n)));tot=xs.sum(axis=1)
pm=p**tot*(1-p)**(n-tot);u=xs[:,0];w=tot/n
assert abs(pm.sum()-1)<1e-12
assert abs(pm@u-p)<1e-12 and abs(pm@w-p)<1e-12
assert abs(pm@((u-p)**2)-.21)<1e-12
assert abs(pm@((w-p)**2)-.02625)<1e-12
assert abs(pm@((u-w)*(w-p)))<1e-12
for s in range(n+1):
 mask=tot==s;assert abs(pm[mask]@u[mask]/pm[mask].sum()-s/n)<1e-12
assert 3/8==.375 and 3*2/12==.5
assert abs(binom.pmf(1,5,.25)-405/1024)<1e-14
assert abs(1.25*math.exp(-1.25)-.35813099607523763)<1e-14
assert 2*(2-1)/6==1/3
for p0 in [.1,.3,.7]:
 s=np.arange(4);assert abs(binom.pmf(s,3,p0)@(s*(s-1)/6)-p0**2)<1e-13

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

for token in ['0.02625', '405/1024']:
    assert token in body, (slug,token)
print(slug+" checks passed")
