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

from fractions import Fraction as F
vx,vu,beta=F(9),F(3),F(2)
assert vx/(vx+vu)==F(3,4)
assert beta*vx/(vx+vu)==F(3,2)
assert vx/(vx+vu/4)==F(12,13)
assert beta*vx/(vx+vu/4)==F(24,13)
assert min(m for m in range(1,10) if vx/(vx+vu/m)>=F(9,10))==3
assert '1.846154' in body and '0.75' in body


# Signs and squared association in the linked observational-data exercise.
assert (-.26)**2 == .06760000000000001
assert abs(.23**2 - .0529) < 1e-14
assert 4.4 > 1.6 > 0

# Sum-of-squares decomposition in the linked variance-estimation exercise.
import sympy as sp
x=sp.symbols('x0:3');mu=sp.symbols('mu');bar=sum(x)/3
assert sp.expand(sum((v-bar)**2 for v in x)-sum((v-mu)**2 for v in x)+3*(bar-mu)**2)==0

print("measurement-error checks passed")
