"""Recompute examples independently and inspect the generated article."""
import numpy as np
import math

omega=.02;alpha=.1;beta=.85;phi=alpha+beta
v=omega/(1-phi);first=omega+alpha*2**2+beta*v
assert abs(v-.4)<1e-14 and abs(first-.76)<1e-14
forecast=first
for j in range(1,11):
 assert abs(forecast-(v+phi**(j-1)*(first-v)))<1e-13
 if j==10:assert abs(forecast-.6268897875008592)<1e-13
 forecast=omega+phi*forecast
assert abs(math.log(.5)/math.log(phi)-13.513407333964874)<1e-12
v2=.02/(1-.1-.8);assert abs(v2-.2)<1e-14
assert abs(.02+.1*4+.8*v2-.58)<1e-14
# An initial finite variance is still finite when persistence exceeds one.
v3=1.
for _ in range(20):v3=.02+1.1*v3;assert math.isfinite(v3)
assert v3>1
assert abs(9/(1-.4**2)-75/7)<1e-13
assert abs(.4*75/7-30/7)<1e-13 and abs(.4**2-.16)<1e-14

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

for token in ['0.626890', '13.5134']:
    assert token in body, (slug,token)
print(slug+" checks passed")
