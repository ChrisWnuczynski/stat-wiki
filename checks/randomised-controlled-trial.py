"""Independent calculations and generated-output checks."""
from pathlib import Path
import re,sys
import numpy as np
import sympy as s
from scipy import stats
ROOT=Path(__file__).resolve().parents[1]
SLUG='randomised-controlled-trial'
NEEDLES=['5/3', '1/2', '10.7']

from itertools import combinations,product
Y0=np.arange(1,5);Y1=Y0+2
est=[]
for treated in combinations(range(4),2):
 control=sorted(set(range(4))-set(treated));est.append(Y1[list(treated)].mean()-Y0[control].mean())
assert est==[0,1,2,2,3,4] and np.mean(est)==2 and np.isclose(np.var(est),5/3)
blocked=[]
for a,b in product([0,1],[2,3]):
 t=[a,b];c=sorted(set(range(4))-set(t));blocked.append(Y1[t].mean()-Y0[c].mean())
assert blocked==[1,2,2,3] and np.mean(blocked)==2 and np.var(blocked)==.5
# Exact expectation of covariate differences is zero under complete randomisation.
means=[]
for t in combinations(range(4),2):
 c=sorted(set(range(4))-set(t));means.append(Y0[list(t)].mean()-Y0[c].mean())
assert np.mean(means)==0
caffeine=np.array([17,22,21,16,6,-2,27,15,16,20]);decaf=np.array([4,10,7,-9,5,4,5,7,6,12])
assert np.isclose(caffeine.mean(),15.8) and np.isclose(decaf.mean(),5.1) and np.isclose(caffeine.mean()-decaf.mean(),10.7)
assert s.binomial(20,10)==184756

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
