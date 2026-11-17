"""Recompute the examples and audit the generated article."""
from pathlib import Path
import re
import numpy as np
import sympy as sp
from scipy import stats
from scipy.special import gammaln,digamma,logsumexp
ROOT=Path(__file__).resolve().parents[1]
SLUG='hard-margin-dual'
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

for X,y,alpha,w,b in [(np.array([[-1.],[1.]]),np.array([-1,1]),np.array([.5,.5]),np.array([1.]),0),(np.array([[-2.],[2.]]),np.array([-1,1]),np.array([.125,.125]),np.array([.5]),0),(np.array([[1.,0.],[3.,1.],[3.,-1.]]),np.array([-1,1,1]),np.array([.5,.25,.25]),np.array([1.,0.]),-2)]:
 margin=y*(X@w+b);assert np.all(margin>=1) and np.isclose(alpha@y,0)
 assert np.allclose((alpha*y)@X,w) and np.allclose(alpha*(margin-1),0)
 assert np.isclose(.5*w@w,alpha.sum()-.5*w@w)
H=(y[:,None]*X)@(y[:,None]*X).T;assert np.linalg.eigvalsh(H).min()>-1e-10
x,z=sp.symbols('x z');assert sp.expand(1+2*x*z+x*x*z*z-(1+x*z)**2)==0
assert np.isclose((.81+2.25)/2,1.53) and np.isclose(1.53-.81,.72)
assert '1/8' in body and '1.53' in body

print(SLUG+": numerical, algebraic and generated-article checks passed")
