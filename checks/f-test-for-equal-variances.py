"""Recompute the examples and audit the generated article."""
from pathlib import Path
import re
import numpy as np
import sympy as sp
from scipy import stats
from scipy.special import gammaln,digamma,logsumexp
ROOT=Path(__file__).resolve().parents[1]
SLUG='f-test-for-equal-variances'
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

ratio=15**2/12**2;lo,hi=stats.f.ppf([.025,.975],14,9)
p=2*min(stats.f.cdf(ratio,14,9),stats.f.sf(ratio,14,9))
assert ratio==1.5625 and np.allclose([lo,hi],[.3115943956,3.7979524823])
assert np.isclose(p,.50658906346) and np.allclose([ratio/hi,ratio/lo],[.4114058844,5.0145317827])
assert np.isclose(stats.f.ppf(.025,14,9),1/stats.f.ppf(.975,9,14))
assert np.isclose(stats.f.cdf(ratio,14,9),stats.f.sf(1/ratio,9,14))
r=(14.1/14.3)**2;assert np.allclose([r/1.762,r*1.762],[.5517727472,1.7130579490])
assert '0.506589' in body and '5.014532' in body

print(SLUG+": numerical, algebraic and generated-article checks passed")
