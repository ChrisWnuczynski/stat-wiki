"""Independent calculations and generated-output checks."""
from pathlib import Path
import re,sys
import numpy as np
import sympy as s
from scipy import stats
ROOT=Path(__file__).resolve().parents[1]
SLUG='perceptron-learning-rule'
NEEDLES=['0.447214', 'five corrections', '1/2']

X=np.array([[0,0],[1,0],[0,1]]);y=np.array([0,1,1]);w=np.zeros(2,dtype=int);b=0;trace=[];scores=[]
for epoch in range(10):
 changes=0
 for x,t in zip(X,y):
  score=b+w@x;pred=int(score>=0)
  if pred!=t:
   scores.append(score);w+=(t-pred)*x;b+=t-pred;trace.append((*w,b));changes+=1
 if changes==0:break
assert trace==[(0,0,-1),(1,0,0),(1,0,-1),(1,1,0),(1,1,-1)]
assert scores==[0,-1,0,-1,0] and epoch==3
assert np.all((X@w+b>=0)==y)
assert np.allclose(X@np.ones(2)-.5,[-.5,.5,.5])
# Check the stated fixed-boundary exercise, and the one-point source update.
assert list((np.array([[1,0],[0,0],[1,2]])@np.array([2,-1])-1>=0).astype(int))==[1,0,0]
assert np.isclose(1/np.sqrt(5),.4472135954999579)
z=np.array([1,1,0]);wv=np.zeros(3,dtype=int);wv-=z
assert np.array_equal(wv,[-1,-1,0]) and wv@z==-2
# Exhaustively check the margin inequalities throughout a separable run.
Z=np.c_[X,np.ones(3)];labels=2*y-1;v=np.zeros(3);u=np.array([1,1,-.5]);u/=np.linalg.norm(u);gamma=np.min(labels*(Z@u));R=np.max(np.linalg.norm(Z,axis=1));m=0
for epoch in range(100):
 changed=False
 for z,t in zip(Z,labels):
  if t*(v@z)<=0:v+=t*z;m+=1;changed=True;assert v@u>=m*gamma-1e-10;assert v@v<=m*R**2+1e-10
 if not changed:break
assert m<=(R/gamma)**2+1e-10 and np.all(labels*(Z@v)>0)

# The same two inequalities with a nonzero initial vector.
v=np.array([3.,-5.,1.]);v0=v.copy();m=0
for epoch in range(100):
 changed=False
 for z,t in zip(Z,labels):
  if t*(v@z)<=0:
   v+=t*z;m+=1;changed=True
   assert v@u>=v0@u+m*gamma-1e-10
   assert v@v<=v0@v0+m*R**2+1e-10
 if not changed:break
assert epoch<99 and np.all(labels*(Z@v)>0)

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
