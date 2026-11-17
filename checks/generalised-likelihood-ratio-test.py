"""Recompute the examples and inspect the generated generalised-likelihood-ratio-test article."""
from pathlib import Path
import re
import numpy as np
import sympy as sp
from scipy import stats

ROOT=Path(__file__).resolve().parents[1]
SLUG='generalised-likelihood-ratio-test'
source=(ROOT / "research" / "content" / (SLUG+".md")).read_text()
body=(ROOT / "articles" / (SLUG+".qmd")).read_text().split("## See also",1)[0]
assert "Your turn" in body and 'collapse="true"' in body
assert "## Check yourself {#check-yourself}" in body
assert len(re.findall('class="cite-ref"',body))>=5

mu,sigma,n=sp.symbols('mu sigma n', real=True, positive=True)
assert sp.simplify(2*(n*mu**2/(2*sigma**2))-n*mu**2/sigma**2)==0
D=16*1**2/2**2
assert D==4 and np.isclose(np.exp(-D/2),0.1353352832366127)
assert np.isclose(2*stats.norm.sf(np.sqrt(D)),0.04550026389635839)
assert 8*(12-13.5)**2+8*(15-13.5)**2==36
assert 36/4==9
assert '0.04550' in body and 'D=4' in body

print(SLUG+": numeric and generated-article checks passed")
