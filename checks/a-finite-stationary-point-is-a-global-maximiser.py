"""Independent calculations and generated-output checks."""
from pathlib import Path
import re,sys
import numpy as np
import sympy as s
from scipy import stats
ROOT=Path(__file__).resolve().parents[1]
SLUG='a-finite-stationary-point-is-a-global-maximiser'
NEEDLES=['0.405465', '-3.365058', '-1.2']

from scipy.special import expit
p=3/5;b=np.log(3/2);y=np.array([0,0,1,1,1]);ll=np.sum(y*b-np.logaddexp(0,b))
assert np.isclose(3-5*expit(b),0) and np.isclose(-5*p*(1-p),-1.2)
assert np.isclose(ll,-3.365058335046282)
assert np.isclose(1-2*expit(0),0) and np.isclose(-2*.5*.5,-.5)
for candidate in np.linspace(-20,20,101):assert np.sum(y*candidate-np.logaddexp(0,candidate))<=ll+1e-10
values=[2*(-np.logaddexp(0,-t)) for t in [0,1,2,5,10]]
assert np.all(np.diff(values)>0) and all(v<0 for v in values)
# Full-rank design can nevertheless be separated.
X=np.array([[1,0],[1,1]]);assert np.linalg.matrix_rank(X)==2
for t in [1,2,5]:
 eta=X@np.array([-t,2*t]);assert np.allclose(eta,[-t,t])
# Hessian is negative semidefinite, with a null direction for duplicate columns.
X=np.array([[1,1],[1,1],[1,1]]);W=np.diag([.1,.2,.24]);H=-X.T@W@X
assert np.all(np.linalg.eigvalsh(H)<=1e-10) and np.allclose(H@np.array([1,-1]),0)
q=s.symbols('q');sig=1/(1+s.exp(-q));assert s.simplify(s.diff(sig,q)-sig*(1-sig))==0
# Selected self-check: separated x=1..4, y=0,0,1,1.
for t in [1,3,10]:
 eta=-2.5*t+t*np.arange(1,5);assert np.all((2*np.array([0,0,1,1])-1)*eta>0)

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
