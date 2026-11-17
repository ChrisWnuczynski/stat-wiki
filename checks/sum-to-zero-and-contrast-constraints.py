"""Recompute numerical examples and exercise answers for sum-to-zero-and-contrast-constraints."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SLUG = 'sum-to-zero-and-contrast-constraints'
text = (ROOT / "articles" / (SLUG + ".qmd")).read_text(encoding="utf-8")
worked = text.split("{#worked-example}", 1)[1].split("\n## ", 1)[0]
answer = worked.split('title="Answer"}', 1)[1]

import math
import numpy as np
from scipy import stats, special, linalg, integrate

means=np.array([[5.,8],[7,15]]);g=means.mean();a=means.mean(axis=1)-g;b=means.mean(axis=0)-g;interaction=means-g-a[:,None]-b[None,:]
assert g==8.75 and np.allclose(a,[-2.25,2.25]) and np.allclose(b,[-2.75,2.75])
assert np.allclose(interaction,[[1.25,-1.25],[-1.25,1.25]])
y=np.array([[[4,6],[7,9]],[[6,8],[14,16]]]);assert np.allclose(y.mean(axis=2),means)
ssA=4*np.sum(a*a);ssB=4*np.sum(b*b);ssI=2*np.sum(interaction*interaction);sse=np.sum((y-means[:,:,None])**2)
assert (ssA,ssB,ssI,sse)==(40.5,60.5,12.5,8)
assert np.allclose(np.round(stats.f.sf([20.25,30.25,6.25],1,4),3),[.011,.005,.067])
assert round(stats.f.ppf(.95,1,4),2)==7.71
assert sse+ssI==20.5 and 8-3==5 and 15-8==7 and ((7-5)+(15-8))/2==4.5
for u in [-1,1]:
 for v in [-1,1]:assert 8.75+2.25*u+2.75*v+1.25*u*v==means[(u+1)//2,(v+1)//2]
X=np.array([[1,u,v,u*v] for u in [-1,1] for v in [-1,1] for _ in range(2)])
fit=np.linalg.lstsq(X,y.ravel(),rcond=None)[0];assert np.allclose(fit,[8.75,2.25,2.75,1.25])
Xadd=X[:,:3];assert np.isclose(np.sum((y.ravel()-Xadd@np.linalg.lstsq(Xadd,y.ravel(),rcond=None)[0])**2),20.5)
assert np.dot([-1,0,1],[4,7,10])==6
assert sum([1,-2,1])==0 and sum([1,1,1])==3

# Match computed worked-example and practice results to their generated text.
assert f"intercept ${g:g}$, fertiliser effects ${a[0]:g},{a[1]:g}$, and water effects ${b[0]:g},{b[1]:g}$" in worked
assert f"m(u,v)={g:g}+{a[1]:g}u+{b[1]:g}v+{interaction[1,1]:g}uv" in worked
exercise_means=np.array([4,7,10]);exercise_effects=exercise_means-exercise_means.mean()
assert 'intercept $'+f'{exercise_means.mean():g}'+'$ and effects $'+','.join(f'{z:g}' for z in exercise_effects)+'$' in answer
assert f"10-4={np.dot([-1,0,1],exercise_means):g}" in answer
print("sum-to-zero-and-contrast-constraints: numerical checks passed")
