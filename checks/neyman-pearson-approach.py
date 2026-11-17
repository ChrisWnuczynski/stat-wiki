"""Recompute the examples and inspect the generated neyman-pearson-approach article."""
from pathlib import Path
import re
import numpy as np
import sympy as sp
from scipy import stats

ROOT=Path(__file__).resolve().parents[1]
SLUG='neyman-pearson-approach'
source=(ROOT / "research" / "content" / (SLUG+".md")).read_text()
body=(ROOT / "articles" / (SLUG+".qmd")).read_text().split("## See also",1)[0]
assert "Your turn" in body and 'collapse="true"' in body
assert "## Check yourself {#check-yourself}" in body
assert len(re.findall('class="cite-ref"',body))>=5

z=stats.norm.ppf(.95);cut=z/5
assert np.isclose(cut,.3289707253902944)
assert np.isclose(stats.norm.sf(z-2),.6387600313123353)
assert np.isclose(stats.binom.sf(12,15,.6),.02711400077721599)
assert np.isclose(stats.binom.sf(12,15,.9),.8159389308936091)
assert np.isclose(127-1.960*7/np.sqrt(101),125.6348089750319)
assert '0.63876' in body

print(SLUG+": numeric and generated-article checks passed")
