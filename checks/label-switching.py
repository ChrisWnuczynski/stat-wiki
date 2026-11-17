"""Recompute the examples and inspect the generated label-switching article."""
from pathlib import Path
import re
import numpy as np
import sympy as sp
from scipy import stats

ROOT=Path(__file__).resolve().parents[1]
SLUG='label-switching'
source=(ROOT / "research" / "content" / (SLUG+".md")).read_text()
body=(ROOT / "articles" / (SLUG+".qmd")).read_text().split("## See also",1)[0]
assert "Your turn" in body and 'collapse="true"' in body
assert "## Check yourself {#check-yourself}" in body
assert len(re.findall('class="cite-ref"',body))>=5

x=np.linspace(-6,6,101)
a=.3*stats.norm.pdf(x,-2,1)+.7*stats.norm.pdf(x,2,1)
b=.7*stats.norm.pdf(x,2,1)+.3*stats.norm.pdf(x,-2,1)
assert np.allclose(a,b)
assert np.isclose(stats.norm.pdf(0,-2,1),.05399096651318806)
assert np.isclose(stats.norm.pdf(0),.3989422804014327)
assert np.isclose(.3*-2+.7*2,.8)
assert np.isclose(.3*1+.7*4+.3*(0-2.8)**2+.7*(4-2.8)**2,6.46)
alloc=np.array([1,1,2]); swapped=np.array([2,2,1])
assert np.array_equal(alloc[:,None]==alloc[None,:],swapped[:,None]==swapped[None,:])
assert '0.398942' in body

print(SLUG+": numeric and generated-article checks passed")
