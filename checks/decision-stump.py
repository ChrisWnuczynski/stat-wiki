"""Independent calculations and generated-output checks."""
from pathlib import Path
import re,sys
import numpy as np
import sympy as s
from scipy import stats
ROOT=Path(__file__).resolve().parents[1]
SLUG='decision-stump'
NEEDLES=['0.549306', '0.866025', '0.693147']

x=np.arange(1,6); y=np.array([1,1,-1,-1,1]); weights=np.ones(5)/5
errors=[]
for t in np.arange(.5,6):
 for a in [-1,1]:errors.append(np.sum(weights[np.where(x<t,a,-a)!=y]))
assert np.isclose(min(errors),.2)
h=np.where(x<2.5,1,-1);error=np.sum(weights[h!=y]);alpha=.5*np.log((1-error)/error)
z=np.sum(weights*np.exp(-alpha*y*h));new=weights*np.exp(-alpha*y*h)/z
assert np.isclose(alpha,np.log(2)) and np.isclose(z,.8)
assert np.allclose(new,[.125,.125,.125,.125,.5])
assert np.isclose(np.sum(new[h!=y]),.5)
assert np.isclose(np.sum(new[np.where(x<4.5,-1,1)!=y]),.25)
assert np.isclose(.5*np.log(3),.5493061443340549)
assert np.isclose(2*np.sqrt(.25*.75),.8660254037844386)
# Recompute the ten-point, three-round source example.
x=np.arange(1,11);y=np.array([1,1,1,-1,-1,-1,1,1,1,-1]);w=np.ones(10)/10;score=np.zeros(10)
for t,a,expected in [(3.5,1,.3),(9.5,1,3/14),(6.5,-1,2/11)]:
 h=np.where(x<t,a,-a);e=np.sum(w[h!=y]);assert np.isclose(e,expected)
 alpha=.5*np.log((1-e)/e);score+=alpha*h;w*=np.exp(-alpha*y*h);w/=w.sum()
assert np.all(np.sign(score)==y)
assert np.allclose(score, np.repeat([.3212517,-.5260461,.9780313,-.3212517],[3,3,3,1]),atol=1e-6)
assert np.isclose(1*.25+0, .25)

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
