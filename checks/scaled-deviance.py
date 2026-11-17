"""Independent calculations and generated-output checks."""
from pathlib import Path
import re,sys
import numpy as np
import sympy as s
from scipy import stats
ROOT=Path(__file__).resolve().parents[1]
SLUG='scaled-deviance'
NEEDLES=['0.105573', '7.2', '0.9']

x=np.arange(4);y=np.array([1,2,2,5]);X=np.c_[np.ones(4),x];beta=np.linalg.lstsq(X,y,rcond=None)[0]
rss1=np.sum((y-X@beta)**2);rss0=np.sum((y-y.mean())**2);ph=rss1/(4-2);F=(rss0-rss1)/ph
assert np.allclose(beta,[.7,1.2]) and np.isclose(rss0,9) and np.isclose(rss1,1.8)
assert np.isclose(ph,.9) and np.isclose(F,8)
assert np.isclose(stats.f.sf(F,1,2),.1055728090000841)
y10=10*y;b10=np.linalg.lstsq(X,y10,rcond=None)[0];r10=np.sum((y10-X@b10)**2)
assert np.isclose(r10/2,90) and np.isclose((np.sum((y10-y10.mean())**2)-r10)/(r10/2),8)
assert np.isclose((4-.4)/(.4/3),27)
assert (8*8/16)*(15-12)**2==36 and 36/4==9
# Orthogonal projection decomposition, independently from the regression fit.
Q,_=np.linalg.qr(X,mode='complete');coords=Q.T@y
assert np.isclose(np.sum(coords[2:]**2),rss1)
assert np.isclose(coords[1]**2,rss0-rss1)

if '--math-only' not in sys.argv:
 source=(ROOT/'research/content'/f'{SLUG}.md').read_text()
 article=(ROOT/"articles"/f'{SLUG}.qmd').read_text().split('## See also',1)[0]
 for needle in NEEDLES:assert needle in article,(SLUG,needle)
 assert len(re.findall(r'\{\{cite:[^}]+\}\}',source))>=5
 assert len(set(re.findall(r'\{\{cite:([^}]+)\}\}',source)))>=2
 assert 'Your turn' in article and 'collapse="true" title="Answer"' in article
 assert '## Check yourself {#check-yourself}' in article
 section=article.split('## Check yourself {#check-yourself}',1)[1].split('\n## ',1)[0]
 ids=re.findall(r'(?m)^### .*\{#self-check-([^}]+)\}',section)
 assert len(ids) in (2,3) and section.count('collapse="true" title="Answer"')==len(ids),(SLUG,ids)
 for qid in ids:assert (ROOT/'questions'/f'{qid}.qmd').exists()
 for ans in re.findall(r'::: \{[^\n]*title="Answer"[^\n]*\}\n(.*?)\n:::',article,re.S):assert 'cite-ref' not in ans
print(SLUG+': independent calculations and article checks passed')
