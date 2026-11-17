"""Recompute the examples and inspect the generated bagging article."""
from pathlib import Path
import re
import numpy as np
import sympy as sp
from scipy import stats

ROOT=Path(__file__).resolve().parents[1]
SLUG='bagging'
source=(ROOT / "research" / "content" / (SLUG+".md")).read_text()
body=(ROOT / "articles" / (SLUG+".qmd")).read_text().split("## See also",1)[0]
assert "Your turn" in body and 'collapse="true"' in body
assert "## Check yourself {#check-yourself}" in body
assert len(re.findall('class="cite-ref"',body))>=5

assert np.isclose(9*(.2+.8/25),2.088)
assert np.isclose(9*(.2+.8/100),1.872)
assert np.isclose(9*.2,1.8)
assert np.isclose((9/10)**10,.3486784401)
assert np.isclose(10*(1-(9/10)**10),6.513215599)
B=sp.symbols('B',positive=True);rho,var=sp.symbols('rho var',real=True)
assert sp.simplify((B*var+B*(B-1)*rho*var)/B**2-var*(rho+(1-rho)/B))==0
assert '2.088' in body and '1.872' in body

print(SLUG+": numeric and generated-article checks passed")
