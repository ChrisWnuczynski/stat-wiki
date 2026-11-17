"""Independent calculations and generated-output checks."""
from pathlib import Path
import re,sys
import numpy as np
import sympy as s
from scipy import stats
ROOT=Path(__file__).resolve().parents[1]
SLUG='expected-duration-of-a-random-walk'
NEEDLES=['1100', '133', '8.270677']

def linear_duration(d,p):
 Q=np.zeros((d-1,d-1))
 for i in range(1,d):
  if i+1<d:Q[i-1,i]=p
  if i-1>0:Q[i-1,i-2]=1-p
 return np.linalg.solve(np.eye(d-1)-Q,np.ones(d-1))
assert np.isclose(linear_duration(6,.5)[1],8)
assert np.isclose(linear_duration(6,.6)[1],1100/133)
assert np.isclose((1-(2/3)**2)/(1-(2/3)**6),81/133)
assert np.isclose(linear_duration(12,.5)[3],32)
assert np.isclose(linear_duration(8,.5)[4],15)
x,d=s.symbols('x d',integer=True);e=lambda x:x*(d-x)
assert s.expand(1+(e(x+1)+e(x-1))/2-e(x))==0
assert e(0)==0 and e(d)==0
r=s.symbols('r',positive=True);p=1/(1+r);q=r/(1+r);h=lambda x:(1-r**x)/(1-r**d)
assert s.simplify(p*h(x+1)+q*h(x-1)-h(x))==0
E=lambda x:(x-d*h(x))/(q-p)
assert s.simplify(1+p*E(x+1)+q*E(x-1)-E(x))==0
# Source comparison: biased walk on four steps from one.
assert np.isclose(linear_duration(4,.6)[0],43/13)

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
