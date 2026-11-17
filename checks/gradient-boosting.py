"""Recompute the examples and audit the generated article."""
from pathlib import Path
import re
import numpy as np
import sympy as sp
from scipy import stats
from scipy.special import gammaln,digamma,logsumexp
ROOT=Path(__file__).resolve().parents[1]
SLUG='gradient-boosting'
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

y=np.array([0.,0.,2.,2.]);F=np.ones(4);assert np.mean(.5*(y-F)**2)==.5
for expected in [.125,.03125]:r=y-F;gamma=r@r/(r@r);F+=.5*gamma*r;assert np.mean(.5*(y-F)**2)==expected
assert np.allclose(F,[.25,.25,1.75,1.75])
z=sp.symbols('z');a=sp.symbols('a',real=True);e=sp.Rational(1,5)
obj=(1-e)*sp.exp(-a)+e*sp.exp(a);assert sp.simplify(sp.diff(obj,a).subs(a,sp.log(2)))==0
assert np.allclose(np.array([.1,.1,.1,.1,.4])/.8,[.125,.125,.125,.125,.5])
assert np.isclose(2*np.sqrt(.2*.8),.8)
for t in [0,1]:assert sp.simplify(sp.diff(sp.log(1+sp.exp(z))-t*z,z)-(1/(1+sp.exp(-z))-t))==0
assert '0.03125' in body and '0.125' in body

print(SLUG+": numerical, algebraic and generated-article checks passed")
