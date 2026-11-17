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

from itertools import product
from fractions import Fraction as F
for p in [F(1,5),F(1,2),F(4,5)]:
    samples=list(product([0,1],repeat=3))
    weights=[p**sum(x)*(1-p)**(3-sum(x)) for x in samples]
    d=[F(sum(x)*(sum(x)-1),6) for x in samples]
    u=[x[0]*x[1] for x in samples]
    assert sum(w*z for w,z in zip(weights,d))==p*p
    if p==F(1,2):
        vd=sum(w*z*z for w,z in zip(weights,d))-p**4
        vu=sum(w*z*z for w,z in zip(weights,u))-p**4
        assert (vd,vu,vu-vd)==(F(5,48),F(3,16),F(1,12))
assert F(2*(2-1),6)==F(1,3)
assert 'title="Proof"' in body and '5/48' in body

print("lehmann-scheffe-theorem checks passed")
