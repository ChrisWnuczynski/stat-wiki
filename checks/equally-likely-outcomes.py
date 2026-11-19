"""Recompute the examples and audit the generated article."""
from pathlib import Path
import re
import numpy as np
import sympy as sp
from scipy import stats
from scipy.special import gammaln,digamma,logsumexp
ROOT=Path(__file__).resolve().parents[1]
SLUG='equally-likely-outcomes'
body=(ROOT/"articles"/(SLUG+'.qmd')).read_text().split('## See also',1)[0]
assert 'Your turn' in body and 'collapse="true"' in body
assert '## Check yourself {#check-yourself}' in body
assert len(re.findall('class="cite-ref"',body))>=5
assert len(set(re.findall('data-cite-key="([^"]+)',body)))>=2
assert len(re.findall(r'\{#self-check-[^}]+\}',body)) in (2,3)
assert '{{cite:' not in body

# Inspect every copied and new inline citation, beyond the minimum count.
for cite in re.finditer(r'<sup[^>]*class="cite-ref"[^>]*>.*?</sup>',body):
    assert re.search(r'data-locator="(?:&quot;|[Cc]h\.|Chs\.|§|Thm\.|Lem\.|Lems\.|p\.|pp\.|Glossary|Ex\.|Summary|Def\.|Sec\.|Props\.|biography,|Introduction|Description|Basic Theory|Convergence|Vector Spaces|Assumptions|Sampling|[“"])', cite.group(0)), cite.group(0)[:220]
for answer in re.findall(r':{3,} \{\.callout-tip collapse="true" title="Answer"\}(.*?)(?=\n:{3,})',body,re.S):
    assert 'class="cite-ref"' not in answer and '{{cite:' not in answer

from itertools import product
pairs=list(product(range(1,7),repeat=2));B=[z for z in pairs if 6 in z]
assert len(B)==11 and sum(sum(z)==7 for z in B)==2
coins=list(product([0,1],repeat=3));assert [sum(sum(z)==k for z in coins) for k in range(4)]==[1,3,3,1]
assert [sum(sum(z)==k for z in product([0,1],repeat=2)) for k in range(3)]==[1,2,1]
for n,target in [(23,.5072972343),(40,.8912318098),(50,.9703735796)]:assert np.isclose(1-np.prod(1-np.arange(n)/365),target)
assert 23*22//2==253
for z in range(2,13):assert sum(sum(q)==z for q in pairs)==6-abs(z-7)
assert '2/11' in body and '0.97037' in body
# Recompute both automatically embedded examples as well.
from math import comb
assert sum(i==j for i,j in pairs)==6
small=[(i,j) for i,j in pairs if i+j<=4]
assert len(small)==6 and sum(i==j for i,j in small)==2
assert np.isclose(4**4/comb(52,4),stats.multivariate_hypergeom.pmf([1,1,1,1,0],[4,4,4,4,36],4))

print(SLUG+": numerical, algebraic and generated-article checks passed")
