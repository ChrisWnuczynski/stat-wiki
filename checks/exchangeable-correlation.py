"""Recompute the examples and audit the generated article."""
from pathlib import Path
import re
import numpy as np
import sympy as sp
from scipy import stats
from scipy.special import gammaln,digamma,logsumexp
ROOT=Path(__file__).resolve().parents[1]
SLUG='exchangeable-correlation'
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

K=4;rho=.3;R=(1-rho)*np.eye(K)+rho*np.ones((K,K))
assert np.allclose(np.linalg.eigvalsh(R),[.7,.7,.7,1.9]) and np.isclose(np.linalg.det(R),.6517)
assert np.allclose(np.linalg.inv(R),(np.eye(K)-rho/(1+(K-1)*rho)*np.ones((K,K)))/(1-rho))
assert np.isclose(np.ones(K)@R@np.ones(K)/K**2,.475)
assert np.allclose(np.linalg.eigvalsh(1.5*np.eye(4)-.5*np.ones((4,4))),[-.5,1.5,1.5,1.5])
assert np.isclose(3/(3+7),.3) and 1+4*(-.3)<0
assert '0.6517' in body and '0.475' in body

print(SLUG+": numerical, algebraic and generated-article checks passed")
