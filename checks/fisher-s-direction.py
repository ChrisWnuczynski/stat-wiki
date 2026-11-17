"""Recompute the examples and audit the generated article."""
from pathlib import Path
import re
import numpy as np
import sympy as sp
from scipy import stats
from scipy.special import gammaln,digamma,logsumexp
ROOT=Path(__file__).resolve().parents[1]
SLUG='fisher-s-direction'
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

def J(a,d,S):return (a@d)**2/(2*a@S@a)
S=np.array([[2.,1.],[1.,2.]]);d=np.array([2.,1.]);a=np.linalg.solve(S,d)
assert np.allclose(a,[1,0]) and J(a,d,S)==1 and J(d,d,S)==25/28
S=np.diag([2.,1.]);d=np.array([2.,2.]);a=np.linalg.solve(S,d);assert np.allclose(a,[1,2]) and J(a,d,S)==3 and J(d,d,S)==8/3
S=np.array([[4/3,2/3],[2/3,2/3]]);d=np.array([-3.,-2.]);a=np.linalg.solve(S,d)
assert np.allclose(a,[-1.5,-1.5]) and np.isclose(J(a,d,S),3.75) and np.isclose(J(d,d,S),507/136)
for a in np.random.default_rng(417).normal(size=(30,2)):assert J(a,d,S)<=d@np.linalg.solve(S,d)/2+1e-10
assert '0.892857' in body and '25/28' in body

print(SLUG+": numerical, algebraic and generated-article checks passed")
