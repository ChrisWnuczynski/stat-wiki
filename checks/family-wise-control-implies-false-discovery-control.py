"""Recompute the examples and audit the generated article."""
from pathlib import Path
import re
import numpy as np
import sympy as sp
from scipy import stats
from scipy.special import gammaln,digamma,logsumexp
ROOT=Path(__file__).resolve().parents[1]
SLUG='family-wise-control-implies-false-discovery-control'
body=(ROOT/"articles"/(SLUG+'.qmd')).read_text().split('## See also',1)[0]
assert 'Your turn' in body and 'collapse="true"' in body
assert '## Check yourself {#check-yourself}' in body
assert len(re.findall('class="cite-ref"',body))>=5
assert len(set(re.findall('data-cite-key="([^"]+)',body)))>=2
assert len(re.findall(r'\{#self-check-[^}]+\}',body)) in (2,3)
assert '{{cite:' not in body

# Inspect every copied and new inline citation, beyond the minimum count.
for cite in re.finditer(r'<sup[^>]*class="cite-ref"[^>]*>.*?</sup>',body):
    assert re.match(r'^\s*\((?:[Cc]h\.|Chs\.|§|Thm\.|Lem\.|Lems\.|p\.|pp\.|Glossary|Ex\.|Summary|Def\.|Sec\.|Props\.|biography,|Introduction|Description|Basic Theory|Convergence|Vector Spaces|Assumptions|Sampling|[“"])',body[cite.end():cite.end()+60]), body[cite.end():cite.end()+100]
for answer in re.findall(r':{3,} \{\.callout-tip collapse="true" title="Answer"\}(.*?)(?=\n:{3,})',body,re.S):
    assert 'class="cite-ref"' not in answer and '{{cite:' not in answer

for V in range(7):
 for R in range(max(V,1),8):assert 0<=V/R<=int(V>=1)
assert 1/50==.02 and .1/20==.005 and .05/100==.0005
thresholds=np.arange(1,6)*.05/5;p=np.array([.001,.025,.026,.027,.8]);k=np.flatnonzero(p<=thresholds).max()+1
assert k==4 and p[1]>thresholds[1] and np.allclose(thresholds,[.01,.02,.03,.04,.05])
assert .05/5000==1e-5 and np.isclose(stats.norm.isf(5e-6),4.41717341347)
assert np.isclose(5*.05/5000,5e-5) and 100*.05/5000==.001
assert '0.005' in body and '0.0005' in body

print(SLUG+": numerical, algebraic and generated-article checks passed")
