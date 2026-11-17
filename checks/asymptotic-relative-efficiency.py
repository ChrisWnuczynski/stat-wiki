"""Recompute examples independently and inspect the generated article."""
import numpy as np
import math

from scipy.stats import norm,binom
f0=norm.pdf(0);median_constant=1/(4*f0**2)
assert abs(median_constant-math.pi/2)<1e-14
assert abs(1/median_constant-2/math.pi)<1e-14
assert abs(2/math.pi-.6366197723675814)<1e-14
assert abs(64*math.pi/2-100.53096491487338)<1e-12
assert math.ceil(64*math.pi/2)==101
# Exact binomial tails converge to the derived median limit.
for t in [-1.,0.,1.]:
 n=10001;p0=norm.cdf(t/math.sqrt(n))
 cdf=binom.sf((n+1)//2-1,n,p0)
 target=norm.cdf(2*f0*t)
 assert abs(cdf-target)<.0001
assert 2/3==1/(3/2)
for n in [2,10,1000]:
 probability=1/n
 assert n*probability==1 and n*n*probability==n
 assert probability<=1/2
 assert abs(math.sqrt(n)/n-1/math.sqrt(n))<1e-14

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

for token in ['0.636620', '100.530965']:
    assert token in body, (slug,token)
print(slug+" checks passed")
