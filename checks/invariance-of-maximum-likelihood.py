"""Recompute the examples and inspect the generated invariance-of-maximum-likelihood article."""
from pathlib import Path
import re
import numpy as np
import sympy as sp
from scipy import stats

ROOT=Path(__file__).resolve().parents[1]
SLUG='invariance-of-maximum-likelihood'
source=(ROOT / "research" / "content" / (SLUG+".md")).read_text()
body=(ROOT / "articles" / (SLUG+".qmd")).read_text().split("## See also",1)[0]
assert "Your turn" in body and 'collapse="true"' in body
assert "## Check yourself {#check-yourself}" in body
assert len(re.findall('class="cite-ref"',body))>=5

l=sp.symbols('l',positive=True); ell=4*sp.log(l)-10*l
assert sp.solve(sp.diff(ell,l),l)==[sp.Rational(2,5)]
assert sp.diff(ell,l,2)==-4/l**2
assert np.isclose(np.log(2)/.4,1.7328679513998633)
assert np.isclose(np.exp(-.4*2),.44932896411722156)
eta=np.linspace(0,16,16001)
profile=np.maximum(-(-np.sqrt(eta)+2)**2/2,-(np.sqrt(eta)+2)**2/2)
assert eta[np.argmax(profile)]==4
assert sp.Rational(2,5)/60==sp.Rational(1,150)
assert '1.73287' in body and '0.44933' in body

print(SLUG+": numeric and generated-article checks passed")
