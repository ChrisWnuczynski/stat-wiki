"""Recompute the examples and inspect the generated bradley-terry-model article."""
from pathlib import Path
import re
import numpy as np
import sympy as sp
from scipy import stats

ROOT=Path(__file__).resolve().parents[1]
SLUG='bradley-terry-model'
source=(ROOT / "research" / "content" / (SLUG+".md")).read_text()
body=(ROOT / "articles" / (SLUG+".qmd")).read_text().split("## See also",1)[0]
assert "Your turn" in body and 'collapse="true"' in body
assert "## Check yourself {#check-yourself}" in body
assert len(re.findall('class="cite-ref"',body))>=5

a=np.array([3,2,1]);prob=a[:,None]/(a[:,None]+a[None,:])
assert np.isclose(prob[0,1],.6) and np.isclose(prob[1,2],2/3) and np.isclose(prob[0,2],.75)
l=np.log(a)
assert np.isclose(np.exp(l[0]-l[1])*np.exp(l[1]-l[2]),np.exp(l[0]-l[2]))
assert np.allclose(np.exp(l[:,None]-l[None,:]),np.exp((l+5)[:,None]-(l+5)[None,:]))
assert np.isclose(np.exp(.3957),1.4854236236135576)
assert np.isclose(np.exp(2*.3957),2.206483341589232)
assert np.isclose(stats.logistic.cdf(.2292+.3957),.6513321551518594)
assert '2.20648' in body

print(SLUG+": numeric and generated-article checks passed")
