"""Recompute the examples and inspect the generated hypergeometric-distribution article."""
from pathlib import Path
import re
import numpy as np
import sympy as sp
from scipy import stats

ROOT=Path(__file__).resolve().parents[1]
SLUG='hypergeometric-distribution'
source=(ROOT / "research" / "content" / (SLUG+".md")).read_text()
body=(ROOT / "articles" / (SLUG+".qmd")).read_text().split("## See also",1)[0]
assert "Your turn" in body and 'collapse="true"' in body
assert "## Check yourself {#check-yourself}" in body
assert len(re.findall('class="cite-ref"',body))>=5

from math import comb
pmf=np.array([comb(5,x)*comb(15,4-x)/comb(20,4) for x in range(5)])
x=np.arange(5)
assert np.isclose(pmf.sum(),1) and np.isclose(pmf@x,1)
assert np.isclose(pmf@((x-1)**2),12/19)
assert np.isclose(pmf[0],1365/4845) and np.isclose(pmf[2],1050/4845)
assert sp.Rational(3,4)+12*sp.Rational(-3,304)==sp.Rational(12,19)
assert np.isclose(stats.hypergeom.pmf(3,100,50,5),.3189107570550869)
assert np.isclose(stats.hypergeom.pmf(1,52,4,5),.2994736356080894)
assert np.isclose(5*50/100,2.5)
assert np.isclose(stats.hypergeom.pmf(3,52,4,3),comb(4,3)/comb(52,3))
assert '0.28173' in body and '0.21672' in body

print(SLUG+": numeric and generated-article checks passed")
