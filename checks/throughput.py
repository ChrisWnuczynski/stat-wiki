"""Recompute the examples and inspect the generated throughput article."""
from pathlib import Path
import re
import numpy as np
import sympy as sp
from scipy import stats

ROOT=Path(__file__).resolve().parents[1]
SLUG='throughput'
source=(ROOT / "research" / "content" / (SLUG+".md")).read_text()
body=(ROOT / "articles" / (SLUG+".qmd")).read_text().split("## See also",1)[0]
assert "Your turn" in body and 'collapse="true"' in body
assert "## Check yourself {#check-yourself}" in body
assert len(re.findall('class="cite-ref"',body))>=5

pi=np.array([1,2,4])/7
Q=np.array([[-4,4,0],[2,-6,4],[0,2,-2]])
assert np.allclose(pi@Q,0) and np.isclose(pi.sum(),1)
rate=4*(1-pi[2]); departure=2*(1-pi[0]);L=pi@np.arange(3)
assert np.isclose(rate,12/7) and np.isclose(departure,rate)
assert np.isclose(L,10/7) and np.isclose(L/rate,5/6)
assert np.isclose((1/3)*(1/2)+(2/3)*(2/2),5/6)
assert np.isclose(2*(1-1/3),4/3)
assert np.isclose(2/(3-2),2) and np.isclose(6/2,3)
assert np.isclose(L/4,5/14)
assert np.isclose((L/4)/(L/rate),3/7)
assert '12/7' in body and '5/6' in body

print(SLUG+": numeric and generated-article checks passed")
