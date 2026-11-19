"""Recompute the examples and audit the generated article."""
from pathlib import Path
import re
import numpy as np
import sympy as sp
from scipy import stats
from scipy.special import gammaln,digamma,logsumexp
ROOT=Path(__file__).resolve().parents[1]
SLUG='fold-cross-validation'
body=(ROOT/"articles"/(SLUG+'.qmd')).read_text().split('## See also',1)[0]
assert 'Your turn' in body and 'collapse="true"' in body
assert '## Check yourself {#check-yourself}' in body
assert len(re.findall('class="cite-ref"',body))>=5
assert len(set(re.findall('data-cite-key="([^"]+)',body)))>=2
assert len(re.findall(r'\{#self-check-[^}]+\}',body)) in (2,3)
assert '{{cite:' not in body

# Inspect every copied and new inline citation, beyond the minimum count.
for cite in re.finditer(r'<sup[^>]*class="cite-ref"[^>]*>.*?</sup>',body):
    assert re.search(r'data-locator="[^"]+"', cite.group(0)), cite.group(0)[:220]
for answer in re.findall(r':{3,} \{\.callout-tip collapse="true" title="Answer"\}(.*?)(?=\n:{3,})',body,re.S):
    assert 'class="cite-ref"' not in answer and '{{cite:' not in answer

assert 5/40==.125 and np.isclose((2/10+3/30)/2,.15)
assert (4+9)/5==2.6 and (4/2+9/3)/2==2.5
I=np.arange(12).reshape(3,4);training=[set(range(12))-set(i) for i in I]
assert all(len(t)==8 for t in training) and all(sum(i in t for t in training)==2 for i in range(12))
assert 10*(9*5+1)==460 and 10*5+1==51 and 460+51==511
assert 1000+1==1001 and 10+1==11
assert '0.125' in body and '2.6' in body

print(SLUG+": numerical, algebraic and generated-article checks passed")
