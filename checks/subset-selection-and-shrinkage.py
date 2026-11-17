"""Recompute examples independently and inspect the generated article."""
import numpy as np
import math

from itertools import product
b=np.array([2.4,-.9,.5,-.1]);lam=2
candidates=[b*np.array(mask) for mask in product([0,1],repeat=4)]
obj=lambda x:np.sum((b-x)**2)+lam*np.count_nonzero(x)
best=min(candidates,key=obj)
assert np.allclose(best,[2.4,0,0,0])
assert np.allclose(np.sign(b)*np.maximum(abs(b)-lam/2,0),[1.4,0,0,0])
assert np.allclose(b/(1+lam),[.8,-.3,1/6,-1/30])
assert 2**20==1048576 and 1+sum(range(1,21))==211
assert 2**30==1073741824 and 2**100>10**30
b0=np.array([1.,.5]);pairs=[b0*np.array(mask) for mask in product([0,1],repeat=2)]
values=[np.sum((x-b0)**2)+np.count_nonzero(x) for x in pairs]
mins=[x for x,v in zip(pairs,values) if abs(v-min(values))<1e-13]
assert {tuple(x) for x in mins}=={(0.,0.),(1.,0.)}
assert np.count_nonzero(2*b)==np.count_nonzero(b)

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

for token in ['1,048,576', '211']:
    assert token in body, (slug,token)
print(slug+" checks passed")
