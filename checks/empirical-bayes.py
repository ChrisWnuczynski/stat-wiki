"""Recompute the examples and audit the generated article."""
from pathlib import Path
import re
import numpy as np
import sympy as sp
from scipy import stats
from scipy.special import gammaln,digamma,logsumexp
ROOT=Path(__file__).resolve().parents[1]
SLUG='empirical-bayes'
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

x=np.array([-1.,1.,3.,5.]);m=x.mean();t=np.mean((x-m)**2)-1
assert m==2 and t==4 and np.allclose(m+t/(t+1)*(x-m),[-.4,1.2,2.8,4.4])
assert np.isclose(.5*(1+25+1+81)-7**2,5)
A=70+25/26*5;B=70+1/3*25;assert np.isclose(A,74.8076923077) and np.isclose(B,78.3333333333) and np.isclose(B-A,3.52564102564)
assert np.isclose(2+4/8*(5-2),3.5) and 4*4/8==2
assert np.isclose(stats.beta.mean(6,14),.3) and np.isclose(stats.beta.mean(42,68),21/55)
assert np.isclose(10/(10+100),1/11)
assert '-0.4' in body and '4.4' in body

print(SLUG+": numerical, algebraic and generated-article checks passed")
