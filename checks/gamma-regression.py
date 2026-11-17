"""Independent calculations and generated-output checks."""
from pathlib import Path
import re,sys
import numpy as np
import sympy as s
from scipy import stats
ROOT=Path(__file__).resolve().parents[1]
SLUG='gamma-regression'
NEEDLES=['0.575364', '2.301457', '1.386294']

y=np.array([2.,4.,6.]);mu=y.mean();phi=np.sum((y-mu)**2/mu**2)/(len(y)-1)
D=2*np.sum((y-mu)/mu-np.log(y/mu))
assert mu==4 and phi==.25 and np.isclose(np.log(mu),1.3862943611198906)
assert np.isclose(D,-2*np.log(.75)) and np.isclose(D,.5753641449035618)
assert np.isclose(D/phi,2.301456579614247)
assert np.isclose(stats.gamma.mean(a=1/phi,scale=phi*mu),4)
assert np.isclose(stats.gamma.std(a=1/phi,scale=phi*mu),2)
assert np.isclose(np.sqrt(phi)*(2*mu),4)
b,x,z,ph=s.symbols('b x z ph',positive=True)
li=-(z*s.exp(-x*b)+x*b)/ph
assert s.simplify(s.diff(li,b)-x*(z/s.exp(x*b)-1)/ph)==0
assert s.simplify(s.diff(li,b,2)+x*x*z*s.exp(-x*b)/ph)==0
q=s.symbols('q',real=True);sig=1/(1+s.exp(-q))
assert s.simplify(s.diff(sig,q)-sig*(1-sig))==0
assert s.simplify(sig.subs(q,-q)-(1-sig))==0
n,v=s.symbols('n v',positive=True);assert s.simplify((n-1)*v/n-v)==-v/n

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
