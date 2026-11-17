"""Recompute the examples and inspect the generated regression-effect article."""
from pathlib import Path
import re
import numpy as np
import sympy as sp
from scipy import stats

ROOT=Path(__file__).resolve().parents[1]
SLUG='regression-effect'
source=(ROOT / "research" / "content" / (SLUG+".md")).read_text()
body=(ROOT / "articles" / (SLUG+".qmd")).read_text().split("## See also",1)[0]
assert "Your turn" in body and 'collapse="true"' in body
assert "## Check yourself {#check-yourself}" in body
assert len(re.findall('class="cite-ref"',body))>=5

b,r,sx,sy=sp.symbols('b r sx sy',real=True,positive=True)
error=sy**2-2*b*r*sx*sy+b*b*sx*sx
assert sp.solve(sp.diff(error,b),b)==[r*sy/sx]
assert sp.simplify(error.subs(b,r*sy/sx)-sy**2*(1-r*r))==0
assert np.isclose(.6*-2,-1.2) and np.isclose(np.sqrt(1-.6**2),.8)
assert 68+.5*(71-67)==70 and 68+.5*(63-67)==66
assert '0.8' in body and '-1.2' in body

print(SLUG+": numeric and generated-article checks passed")
