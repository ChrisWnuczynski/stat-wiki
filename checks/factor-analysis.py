"""Recompute the examples and audit the generated article."""
from pathlib import Path
import re
import numpy as np
import sympy as sp
from scipy import stats
from scipy.special import gammaln,digamma,logsumexp
ROOT=Path(__file__).resolve().parents[1]
SLUG='factor-analysis'
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

l=np.array([.8,.6,.5]);psi=np.array([.36,.64,.75]);S=np.outer(l,l)+np.diag(psi)
assert np.allclose(S,[[1,.48,.4],[.48,1,.3],[.4,.3,1]]) and np.isclose(.48*.4/.3,.64)
v=1/(1+np.sum(l*l/psi));m=v*np.sum(l*np.array([1,0,-1])/psi)
assert np.isclose(m,.4234404536862) and np.isclose(v,.27221172022684)
assert np.allclose(np.outer(-l,-l)+np.diag(psi),S)
L=np.array([[1.,0.],[0.,1.],[1.,1.]]);q=np.array([[1,-1],[1,1]])/np.sqrt(2);assert np.allclose(L@q@(L@q).T,L@L.T)
assert np.allclose(np.array([[2,0],[1,np.sqrt(2)]])@np.array([[2,0],[1,np.sqrt(2)]]).T,[[4,2],[2,3]])
assert np.allclose(np.linalg.eigvalsh([[1,.4],[.4,1]]),[.6,1.4])
assert '0.423440' in body and '0.272212' in body

print(SLUG+": numerical, algebraic and generated-article checks passed")
