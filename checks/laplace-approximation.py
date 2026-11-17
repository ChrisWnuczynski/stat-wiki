"""Independent calculations and generated-output checks."""
from pathlib import Path
import re,sys
import numpy as np
import sympy as s
from scipy import stats
ROOT=Path(__file__).resolve().parents[1]
SLUG='laplace-approximation'
NEEDLES=['3.6288', '0.991704', '0.999167']

from scipy.integrate import quad
from scipy.special import gammaln
for n,target in [(10,.9917040395560642),(100,.9991670165679232)]:
 logI=gammaln(n+1)-(n+1)*np.log(n);logL=-n+.5*np.log(2*np.pi/n)
 assert np.isclose(np.exp(logL-logI),target)
assert np.isclose(np.exp(gammaln(11)-11*np.log(10)),3.6288e-5)
assert np.isclose(np.exp(-10)*np.sqrt(2*np.pi/10),3.598695618741036e-5)
assert np.isclose(quad(lambda x:np.exp(-2*(x-2)**2),-np.inf,np.inf)[0],np.sqrt(np.pi/2))
# Determinant factor by a non-diagonal positive definite quadratic.
H=np.array([[2.,1.],[1.,3.]]);assert np.isclose(np.prod(np.linalg.eigvalsh(H)),np.linalg.det(H))
assert np.isclose((2*np.pi)/np.sqrt(np.linalg.det(H)),(2*np.pi)/np.sqrt(5))
assert np.isclose(6*(.25/.75),2) and np.isclose(2/(1+2),2/3)
x=s.symbols('x',positive=True);f=s.log(x)-x
assert s.diff(f,x).subs(x,1)==0 and s.diff(f,x,2).subs(x,1)==-1

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
