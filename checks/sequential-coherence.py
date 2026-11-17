"""Recompute examples independently and inspect the generated article."""
import numpy as np
import math

from scipy.special import betaln
from scipy.stats import beta
prior=np.array([2,3]);increments=np.array([[4,6],[3,2]])
assert np.array_equal(prior+increments.sum(axis=0),[9,11])
for order in [[0,1],[1,0]]:
 cur=prior.copy()
 for i in order:cur+=increments[i]
 assert np.array_equal(cur,[9,11])
assert abs(beta.mean(9,11)-.45)<1e-14
assert abs(beta.var(9,11)-.011785714285714286)<1e-14
assert abs(math.exp(betaln(11,11)-betaln(9,11))-3/14)<1e-14
assert abs(.45**2-.2025)<1e-14
assert np.array_equal(prior+[1+2,3+1],[5,7])
assert abs(5/12-.4166666666666667)<1e-14
assert np.array_equal(np.array([1,1])+[3+2,7+3],[6,11])
assert np.array_equal(np.array([2,2])+[3+4,2+1],[9,5])
# Normalised products give the same density as adding both exponents at once.
grid=np.linspace(.01,.99,99)
logk=beta.logpdf(grid,2,3)+7*np.log(grid)+8*np.log1p(-grid)
logpost=beta.logpdf(grid,9,11)
assert np.ptp(logk-logpost)<1e-12

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

for token in ['0.0117857', '0.214286']:
    assert token in body, (slug,token)
print(slug+" checks passed")
