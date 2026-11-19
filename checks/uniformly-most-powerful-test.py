"""Independent calculations and generated-output checks for this article."""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tools.shown import shown
import re
ROOT=Path(__file__).resolve().parents[1]
import numpy as np
from scipy.stats import norm,poisson
z=norm.ppf(.95);z2=norm.ppf(.975)
assert abs(10+.4*z-10.657941450780589)<1e-12
assert abs(norm.sf(z-2.5)-.803764940015494)<1e-12
assert abs(norm.sf(z2-2.5)+norm.cdf(-z2-2.5)-.7054180011138003)<1e-12
assert abs(norm.sf(z-2)-.6387600313123353)<1e-12
assert abs(norm.sf(z2-2)+norm.cdf(-z2-2)-.5160052739761748)<1e-12
assert abs(norm.sf(z)-.05)<1e-14
powers=[norm.sf(z-(mu-10)/.4) for mu in np.linspace(8,12,81)]
assert all(a<=b for a,b in zip(powers,powers[1:]))

source=(ROOT/"research/content/uniformly-most-powerful-test.md").read_text()
source = shown(source, "uniformly-most-powerful-test")
article=(ROOT/"articles/uniformly-most-powerful-test.qmd").read_text().split("## See also",1)[0]
for needle in ['0.803765', '0.705418', '0.638760', '0.516005']:
    assert needle in source and needle in article, needle
assert len(re.findall(r"\{\{cite:[^}]+\}\}", source))>=5
assert len(set(re.findall(r"\{\{cite:([^}]+)\}\}",source)))>=2
assert "Your turn" in article and 'collapse="true" title="Answer"' in article
assert "## Check yourself {#check-yourself}" in article
print("uniformly-most-powerful-test: calculations and article checks passed")
