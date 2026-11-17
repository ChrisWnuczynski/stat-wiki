"""Recompute the examples and inspect the generated hazard-rate article."""
from pathlib import Path
import re
import numpy as np
import sympy as sp
from scipy import stats

ROOT=Path(__file__).resolve().parents[1]
SLUG='hazard-rate'
source=(ROOT / "research" / "content" / (SLUG+".md")).read_text()
body=(ROOT / "articles" / (SLUG+".qmd")).read_text().split("## See also",1)[0]
assert "Your turn" in body and 'collapse="true"' in body
assert "## Check yourself {#check-yourself}" in body
assert len(re.findall('class="cite-ref"',body))>=5

t=sp.symbols('t',positive=True); S=sp.exp(-t*t)
assert sp.simplify(-sp.diff(S,t)/S-2*t)==0
assert np.isclose(1-np.exp(-.21),.18941575402981292)
assert np.isclose(np.sqrt(np.log(2)),.8325546111576977)
assert np.isclose(float(sp.integrate(sp.exp(-t*t),(t,0,sp.oo))),np.sqrt(np.pi)/2)
assert np.isclose(np.exp(-3),.049787068367863944)
assert np.isclose(np.exp(-.5),.6065306597126334)
assert '0.18942' in body

print(SLUG+": numeric and generated-article checks passed")
