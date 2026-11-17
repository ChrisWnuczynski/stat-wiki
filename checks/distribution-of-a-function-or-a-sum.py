"""Recompute the examples and audit the generated article."""
from pathlib import Path
import re
import numpy as np
import sympy as sp
from scipy import stats
from scipy.special import gammaln,digamma,logsumexp
ROOT=Path(__file__).resolve().parents[1]
SLUG='distribution-of-a-function-or-a-sum'
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

y=sp.symbols('y',positive=True)
assert sp.integrate(1/(2*sp.sqrt(y)),(y,0,1))==1
assert sp.integrate(y/(2*sp.sqrt(y)),(y,0,1))==sp.Rational(1,3)
assert np.isclose(np.sqrt(.25),.5)
assert sp.integrate(y,(y,0,sp.Rational(1,2)))==sp.Rational(1,8)
assert sp.integrate(y,(y,0,1))+sp.integrate(2-y,(y,1,sp.Rational(3,2)))==sp.Rational(7,8)
assert np.isclose(2*stats.uniform.var(),1/6)
assert np.isclose(1/(5/1000),200)
for z in [.01,.2,1,4,10]:assert np.isclose(stats.chi2.pdf(z,1),stats.norm.pdf(np.sqrt(z))/np.sqrt(z))
assert sp.integrate(sp.Rational(1,4)*sp.exp(-(y-1)/4),(y,1,sp.oo))==1
assert sp.integrate(y*sp.Rational(1,4)*sp.exp(-(y-1)/4),(y,1,sp.oo))==5
assert 1-.25==.75 and np.isclose(stats.expon.mean(scale=1)*stats.expon.mean(scale=.5),.5)
assert '0.125' in body and '0.875' in body

print(SLUG+": numerical, algebraic and generated-article checks passed")
