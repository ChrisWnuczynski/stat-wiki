"""Recompute examples independently and inspect the generated article."""
import numpy as np
import math

gap=np.array([.3,.7,1.1,1.15,1.]);se=np.array([.05,.05,.06,.06,.07])
choices=np.flatnonzero(gap[:-1]>=gap[1:]-se[1:])+1
assert choices[0]==3 and gap.argmax()+1==4
logs=np.array([2.2,2.3,2.4,2.5]);B=len(logs)
mean=logs.mean();sd=np.sqrt(np.mean((logs-mean)**2));allowance=sd*math.sqrt(1+1/B)
assert abs(mean-2.35)<1e-14 and abs(mean-1.5-.85)<1e-14
assert abs(sd-.11180339887498944)<1e-14 and abs(allowance-.125)<1e-14
assert abs(mean-1.8-.55)<1e-14
assert abs(math.log(np.exp(logs).prod()**(1/B))-mean)<1e-14
x=np.array([0.,1,4,5]);W1=np.sum((x-x.mean())**2)
W2=sum(np.sum((c-c.mean())**2) for c in [x[:2],x[2:]])
assert W1==17 and W2==1
assert np.sum((x-x)**2)==0
assert logs.std(ddof=1)>sd

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

for token in ['0.111803', '0.125']:
    assert token in body, (slug,token)
print(slug+" checks passed")
