"""Independent calculations and generated-output checks."""
from pathlib import Path
import re,sys
import numpy as np
import sympy as s
from scipy import stats
ROOT=Path(__file__).resolve().parents[1]
SLUG='m-m-queue'
NEEDLES=['0.184737', '0.049787', '0.002479']

from math import factorial
rho=12/4
pmf=np.array([np.exp(-rho)*rho**n/factorial(n) for n in range(40)])
assert np.isclose(pmf.sum(),1) and np.isclose(np.arange(40)@pmf,3)
assert np.isclose(np.exp(-3),.049787068367863944)
assert np.isclose(stats.poisson.sf(4,3),.18473675547622787)
assert 3/12==1/4 and 6/24==1/4
assert np.isclose(np.exp(-6),.0024787521766663585)
for n in range(20):assert np.isclose(pmf[n]*12,pmf[n+1]*(n+1)*4)
# Source queue example, plus the two self-check calculations.
assert np.isclose(stats.poisson.sf(4,2),.052653017343711125)
assert np.isclose(stats.poisson.sf(3,3),.35276811121776874)
pi=s.Matrix([[1,3,2]])/6
P=s.Matrix([[0,1,0],[s.Rational(1,3),0,s.Rational(2,3)],[0,1,0]])
assert pi*P==pi

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
