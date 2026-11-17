"""Recompute the examples and inspect the generated perceptron article."""
from pathlib import Path
import re
import numpy as np
import sympy as sp
from scipy import stats

ROOT=Path(__file__).resolve().parents[1]
SLUG='perceptron'
source=(ROOT / "research" / "content" / (SLUG+".md")).read_text()
body=(ROOT / "articles" / (SLUG+".qmd")).read_text().split("## See also",1)[0]
assert "Your turn" in body and 'collapse="true"' in body
assert "## Check yourself {#check-yourself}" in body
assert len(re.findall('class="cite-ref"',body))>=5

X=np.array([[0,0],[1,0],[0,1]],float); y=np.array([0,1,1]);v=np.zeros(3);updates=[]
for epoch in range(20):
 mistakes=0
 for x,label in zip(X,y):
  a=np.r_[1,x];o=int(v@a>=0)
  if o!=label:
   before=v@a;v+=(label-o)*a
   assert np.isclose(v@a-before,(label-o)*(a@a))
   updates.append(v.tolist());mistakes+=1
 if mistakes==0:break
assert updates==[[-1,0,0],[0,1,0],[-1,1,0],[0,1,1],[-1,1,1]]
assert np.array_equal((np.c_[np.ones(3),X]@v>=0).astype(int),y)

# Track both inequalities used in the finite-mistake proof independently.
u=np.array([-1.,2.,2.])/3
augmented=np.c_[np.ones(3),X];signed=2*y-1
assert np.isclose(u@u,1)
gamma=min(signed*(augmented@u));R=max(np.linalg.norm(augmented,axis=1))
assert np.isclose(gamma,1/3) and np.isclose(R**2/gamma**2,18)
for T,weights in enumerate(updates,1):
 w=np.array(weights,float)
 assert u@w >= T*gamma-1e-12
 assert w@w <= T*R**2+1e-12
assert len(updates)<=R**2/gamma**2
assert 'Cauchy–Schwarz' in body and 'R^2/\\gamma^2' in body

assert np.array_equal((np.c_[np.ones(3),[[1,0],[0,0],[1,2]]]@[-1,2,-1]>=0).astype(int),[1,0,0])
# Recompute the longer five-pattern learning trajectory also printed on the page.
points=np.array([[1,1],[0,.5],[-.5,-.5],[1,0],[.5,-1]],float)
labels=np.array([1,1,1,0,0]);oldv=np.array([-1.,2.,1.])
chosen=[1,3,1,3,2,2]
expected=[[0,2,1.5],[-1,1,1.5],[0,1,2],[-1,0,2],[0,-.5,1.5],[1,-1,1]]
for i,want in zip(chosen,expected):
 a=np.r_[1,points[i]];o=int(oldv@a>=0)
 assert o!=labels[i]
 oldv+=(labels[i]-o)*a;assert np.allclose(oldv,want)
extra=0
for epoch in range(10):
 mistakes=0
 for x,label in zip(points,labels):
  a=np.r_[1,x];o=int(oldv@a>=0)
  if o!=label:oldv+=(label-o)*a;mistakes+=1;extra+=1
 if not mistakes:break
assert extra==3 and np.allclose(oldv,[0,-2,2])
assert '(-1,1,1)' in body

print(SLUG+": numeric and generated-article checks passed")
