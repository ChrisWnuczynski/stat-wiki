"""Recompute examples independently and inspect the generated article."""
import numpy as np
import math

from scipy.stats import poisson,binom
from math import factorial
rate=8;p=3/8
assert rate*p==3 and rate*(1-p)==5
assert abs(math.exp(-8)-.00033546262790251185)<1e-16
assert abs(math.exp(-3)*math.exp(-5)-math.exp(-8))<1e-17
for j in range(8):
 for k in range(8):
  joint=poisson.pmf(j+k,8)*binom.pmf(j,j+k,p)
  assert abs(joint-poisson.pmf(j,3)*poisson.pmf(k,5))<1e-14
assert 8*p==3 and 8*p*(1-p)==15/8
assert abs(poisson.pmf(2,1.5)-.25102143016698353)<1e-14
assert abs(math.exp(-1)-.36787944117144233)<1e-14
assert .5**3==1/8
assert 10*.6==6 and 10*(1-.6)==4
# Duplicate streams fail a Poisson variance check.
assert 4*4==16 and 2*4==8 and 16!=8

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

for token in ['0.000335463', '0.251021']:
    assert token in body, (slug,token)
print(slug+" checks passed")
