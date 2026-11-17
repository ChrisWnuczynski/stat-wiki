"""Recompute the examples and inspect the generated nonhomogeneous-poisson-process article."""
from pathlib import Path
import re
import numpy as np
import sympy as sp
from scipy import stats

ROOT=Path(__file__).resolve().parents[1]
SLUG='nonhomogeneous-poisson-process'
source=(ROOT / "research" / "content" / (SLUG+".md")).read_text()
body=(ROOT / "articles" / (SLUG+".qmd")).read_text().split("## See also",1)[0]
assert "Your turn" in body and 'collapse="true"' in body
assert "## Check yourself {#check-yourself}" in body
assert len(re.findall('class="cite-ref"',body))>=5

t=sp.symbols('t',nonnegative=True);H=2*t+t*t/2
assert sp.diff(H,t)==2+t and H.subs(t,2)==6
assert H.subs(t,2)-H.subs(t,1)==sp.Rational(7,2)
assert sp.simplify(H.subs(t,sp.sqrt(6)-2)-1)==0
assert sp.simplify(H.subs(t,sp.sqrt(8)-2)-2)==0
assert np.isclose(np.sqrt(8)-np.sqrt(6),.3789373819630124)
assert np.isclose(stats.poisson.pmf(2,1.5),.25102143016698353)
assert '0.449490' in body and '0.002479' in body

print(SLUG+": numeric and generated-article checks passed")
