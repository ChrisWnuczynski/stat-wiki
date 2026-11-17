"""Recompute examples independently and inspect the generated article."""
import numpy as np
import math

w=np.array([3.,4]);b=-5.;x=np.array([2.,1]);score=w@x+b
norm=np.linalg.norm(w);dist=score/norm;projection=x-score/(w@w)*w
assert dist==1 and np.allclose(projection,[1.4,.2])
assert abs(w@projection+b)<1e-13
assert b/norm==-1 and 2/norm==.4
for c in [.1,2.,-2.]:
 wc=c*w;bc=c*b
 assert np.allclose(x-(wc@x+bc)/(wc@wc)*wc,projection)
 assert abs((wc@x+bc)/np.linalg.norm(wc)-math.copysign(1,c)*dist)<1e-13
for t in [-3.,-.1,0,7.]:
 z=projection+t*np.array([-4.,3])
 assert abs(np.linalg.norm(x-z)**2-(dist**2+np.linalg.norm(projection-z)**2))<1e-10
assert (np.array([3.,0])@np.array([5.,4])-6)/3==3
assert abs(2/3-.6666666666666666)<1e-14

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

for token in ['1.4', '0.2']:
    assert token in body, (slug,token)
print(slug+" checks passed")
