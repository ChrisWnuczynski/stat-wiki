"""Independent calculations and generated-output checks."""
from pathlib import Path
import re,sys
import numpy as np
import sympy as s
from scipy import stats
ROOT=Path(__file__).resolve().parents[1]
SLUG='a-single-threshold-unit-cannot-compute-xor'
NEEDLES=['XNOR', 'NAND', '3/2']

from scipy.optimize import linprog
X=np.array([[0,0],[0,1],[1,0],[1,1]]);y=np.array([0,1,1,0]);A=np.c_[np.ones(4),X];labels=2*y-1
# Strict separation of finitely many points can be rescaled to margin one.
assert not linprog(np.zeros(3),A_ub=-labels[:,None]*A,b_ub=-np.ones(4),bounds=[(None,None)]*3,method='highs').success
OR=(2*X.sum(axis=1)-1>=0).astype(int);NAND=(3-2*X.sum(axis=1)>=0).astype(int)
score=OR+NAND-1.5
assert np.array_equal(OR,[0,1,1,1]) and np.array_equal(NAND,[1,1,1,0])
assert np.array_equal((score>=0).astype(int),y)
assert np.array_equal((-score>=0).astype(int),1-y)
assert np.array_equal(X.sum(axis=1)-2*np.prod(X,axis=1),y)
assert np.allclose((X[1]+X[2])/2,(X[0]+X[3])/2)
# Affine hidden layers compose to one affine score, for arbitrary fixed matrices.
M=np.array([[2.,1.,-1.],[3.,0.,2.]]);c=np.array([1.,-2.,3.]);v=np.array([1.,2.,-1.]);b=.7
assert np.allclose((X@M+c)@v+b,X@(M@v)+(c@v+b))

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
