"""Independent calculations and generated-output checks for this article."""
from pathlib import Path
import re
ROOT=Path(__file__).resolve().parents[1]
import itertools
import numpy as np
from scipy.stats import binom,norm
from scipy.optimize import linprog
k=np.arange(5);p0=binom.pmf(k,4,.5);p1=binom.pmf(k,4,.75)
gamma=(.1-p0[4])/p0[3];phi=np.array([0,0,0,gamma,1])
assert abs(gamma-.15)<1e-14 and abs(p0@phi-.1)<1e-14
assert abs(p1@phi-.3796875)<1e-14
opt=linprog(-p1,A_ub=[p0],b_ub=[.1],bounds=[(0,1)]*5,method="highs")
assert opt.success and abs(-opt.fun-p1@phi)<1e-12
assert abs(p1[4]-.31640625)<1e-14
assert abs(binom.sf(12,15,.6)-.027114000777216)<1e-14
assert abs(binom.sf(12,15,.9)-.815938930893609)<1e-14
z=norm.ppf(.95)
assert abs(10+.4*z-10.657941450780589)<1e-12
assert abs(norm.sf(z-2.5)-.803764940015494)<1e-12

source=(ROOT/"research/content/neyman-pearson-lemma.md").read_text()
article=(ROOT/"articles/neyman-pearson-lemma.qmd").read_text().split("## See also",1)[0]
for needle in ['0.3796875', '0.31640625', '0.15']:
    assert needle in source and needle in article, needle
assert len(re.findall(r"\{\{cite:[^}]+\}\}", source))>=5
assert len(set(re.findall(r"\{\{cite:([^}]+)\}\}",source)))>=2
assert "Your turn" in article and 'collapse="true" title="Answer"' in article
assert "## Check yourself {#check-yourself}" in article
print("neyman-pearson-lemma: calculations and article checks passed")
