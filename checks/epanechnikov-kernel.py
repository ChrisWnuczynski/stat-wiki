"""Recompute the examples and audit the generated article."""
from pathlib import Path
import re
import numpy as np
import sympy as sp
from scipy import stats
from scipy.special import gammaln,digamma,logsumexp
ROOT=Path(__file__).resolve().parents[1]
SLUG='epanechnikov-kernel'
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

u=sp.symbols('u');K=sp.Rational(3,4)*(1-u*u)
assert sp.integrate(K,(u,-1,1))==1 and sp.integrate(u*K,(u,-1,1))==0
assert sp.integrate(u*u*K,(u,-1,1))==sp.Rational(1,5)
assert sp.integrate(K*K,(u,-1,1))==sp.Rational(3,5)
def kde(x,h):
 z=(x-np.array([0.,1.,2.]))/h
 return np.where(abs(z)<=1,.75*(1-z*z),0).sum()/(3*h)
assert kde(1,1)==.25 and kde(1,2)==.3125 and kde(1,.5)==.5
assert np.isclose((stats.norm.pdf(1)+stats.norm.pdf(0)+stats.norm.pdf(2))/3,.231634657144588)
# Check the variational comparison on two different equal-second-moment kernels.
assert 1/(2*np.sqrt(.6))>.6 and np.sqrt(5)/(2*np.sqrt(np.pi))>.6
assert '0.3125' in body and '1/5' in body

print(SLUG+": numerical, algebraic and generated-article checks passed")
