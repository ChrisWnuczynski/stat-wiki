"""Recompute the displayed examples and practice answers."""
import math
from fractions import Fraction
import numpy as np
from scipy import stats, optimize
from pathlib import Path

x=np.array([[-1.8,-2.1],[6.2,3.8],[-1.5,-2.2],[-.9,-1.4],[.3,-1.3],[1.4,-1.9],[2.6,.8],[1.6,.8],[-2.3,-2.5],[.5,-.2],[3.4,.3],[.9,-1.]])
s=np.cov(x.T);v,a=np.linalg.eigh(s);v=v[::-1];a=a[:,::-1];a[:,0]*=np.sign(a[0,0]);a[:,1]=[-a[1,0],a[0,0]]
assert np.allclose(s,[[5.9097,3.9964],[3.9964,3.2402]],atol=.00005)
assert np.allclose(v,[8.788,.362],atol=.0005)
assert np.allclose(a[:,0],[.8114,.5845],atol=.00005)
assert round(100*v[0]/sum(v),2)==96.05
assert round(np.corrcoef(x.T)[0,1],4)==.9133
assert round(100*(1+np.corrcoef(x.T)[0,1])/2,1)==95.7
assert round(abs(x.mean(0)@a[:,1])/np.linalg.norm(x.mean(0)),2)==.94
assert np.allclose(np.cov(((x-x.mean(0))@a).T),np.diag(v),atol=1e-12)
r=.6**np.abs(np.arange(8)[:,None]-np.arange(8)[None,:]);lam=np.linalg.eigvalsh(r)[::-1];cum=np.cumsum(lam)/sum(lam)
assert np.allclose(np.round(lam,3),[3.151,1.832,1.035,.644,.448,.344,.287,.259])
assert np.allclose(np.round(100*cum,1),[39.4,62.3,75.2,83.3,88.9,93.2,96.8,100])
assert np.searchsorted(cum,.9)+1==6 and np.searchsorted(cum,.75)+1==3
assert np.searchsorted(np.cumsum([5,2,1,0])/8,.9)+1==3
assert 9/10==.9 and round(100/101*100,2)==99.01
assert round(np.linalg.det(s),4)==3.1778 and round(np.trace(s),4)==9.1499
assert round((8.788-5.9097)/3.9964,4)==.7202
assert round(100*(1-v[0]/sum(v)),2)==3.95
mean=x.mean(0);tsq=len(x)*mean@np.linalg.solve(s,mean)
assert (len(x)-2)*tsq/(2*(len(x)-1))>stats.f.ppf(.95,2,len(x)-2)
assert np.all(2*stats.t.sf(np.abs(mean/np.sqrt(np.diag(s)/len(x))),len(x)-1)>.05)

# Compare recomputed results with the generated worked example and practice answer.
ROOT = Path(__file__).resolve().parents[1]
SLUG = 'choosing-the-number-of-principal-components'
article = (ROOT / "articles" / (SLUG + ".qmd")).read_text(encoding="utf-8")
worked_section = article.split("{#worked-example}", 1)[1].split("\n## ", 1)[0]
worked_example, your_turn = worked_section.split("**Your turn.**", 1)

worked_eigenvalues=np.array([5,2,1,0])
worked_cumulative=np.cumsum(worked_eigenvalues)/worked_eigenvalues.sum()
for explained in worked_cumulative[:2]:
 assert f"{100*explained:.1f}\\%" in worked_example
practice_eigenvalues=np.array([6,3,1])
practice_explained=practice_eigenvalues[:2].sum()/practice_eigenvalues.sum()
assert f"={practice_explained:.1f}" in your_turn
assert f"={1-practice_explained:.1f}" in your_turn
# Also bind the refitted two-variable covariance PCA and AR(1) table.
for eigenvalue in v:
 assert f"{eigenvalue:.3f}" in article
assert f"{100*v[0]/sum(v):.2f}\\%" in article
for eigenvalue in lam:
 assert f"{eigenvalue:.3f}" in article

print("choosing-the-number-of-principal-components: numerical checks passed")
