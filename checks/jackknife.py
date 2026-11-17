"""Independent calculations and generated-output checks."""
from pathlib import Path
import re,sys
import numpy as np
import sympy as s
from scipy import stats
ROOT=Path(__file__).resolve().parents[1]
SLUG='jackknife'
NEEDLES=['167/18', '49/6', '0.912871', '1009/6']

y=np.array([1.,2.,4.,5.]);n=len(y);theta=y.mean()**2
loo=np.array([np.delete(y,i).mean()**2 for i in range(n)]);mean=loo.mean();bias=(n-1)*(mean-theta);corrected=theta-bias
assert np.isclose(mean,167/18) and np.isclose(bias,5/6) and np.isclose(corrected,49/6)
assert np.isclose(corrected,theta-y.var(ddof=1)/n)
means=np.array([np.delete(y,i).mean() for i in range(n)])
assert np.isclose(means.mean(),y.mean())
var=(n-1)/n*np.sum((means-means.mean())**2)
assert np.isclose(var,5/6) and np.isclose(np.sqrt(var),.9128709291752769)
trans=y+10;lt=np.array([np.delete(trans,i).mean()**2 for i in range(n)])
assert np.isclose(3*(lt.mean()-trans.mean()**2),5/6)
assert np.isclose(trans.mean()**2-5/6,1009/6)
# Recompute the five-point variance example in the source text.
y=np.array([2.,4.,4.,6.,9.]);theta=y.var();l=np.array([np.delete(y,i).var() for i in range(5)])
assert np.isclose(theta,5.6) and np.isclose(l.mean(),5.25)
assert np.allclose(l,[4.1875,6.6875,6.6875,6.6875,2])
assert np.isclose(theta-4*(l.mean()-theta),7)
assert np.isclose(np.sum((l-l.mean())**2),17.890625)
assert np.isclose(np.sqrt(4/5*np.sum((l-l.mean())**2)),np.sqrt(14.3125))
n,a,b,th=s.symbols('n a b th',positive=True)
f=lambda n:th+a/n+b/n**2
assert s.simplify(n*f(n)-(n-1)*f(n-1)-th)==-b/(n*(n-1))

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
