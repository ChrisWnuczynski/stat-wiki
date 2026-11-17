"""Recompute the worked calculations and inspect the generated article."""
from pathlib import Path
import re
root = Path(__file__).resolve().parents[1]
source = (root / "research" / "content" / (Path(__file__).stem + ".md")).read_text()
article = (root / "articles" / (Path(__file__).stem + ".qmd")).read_text()
body = article.split("## See also", 1)[0]
assert len(re.findall(r"\{\{cite:", source)) >= 5
assert len(set(re.findall(r"\{\{cite:([^}]+)", source))) >= 2
assert "Your turn" in body and 'collapse="true"' in body

import itertools
p = .3
mass = lambda x: p ** sum(x) * (1-p) ** (len(x)-sum(x))
assert abs(mass((1,0,1))-.063)<1e-14
assert abs(mass((1,0,0))-.147)<1e-14
assert abs(mass((1,1,0))+mass((1,1,1))-.09)<1e-14
for n in range(1,7):
    assert abs(sum(mass(x) for x in itertools.product([0,1],repeat=n))-1)<1e-12
    for prefix in itertools.product([0,1],repeat=n):
        assert abs(sum(mass(prefix+(z,)) for z in [0,1])-mass(prefix))<1e-14
for number in ['0.063','0.147','0.21','0.09']:
    assert number in body

print("kolmogorov-extension-theorem checks passed")
