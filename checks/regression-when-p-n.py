"""Recompute numerical examples and exercise answers for regression-when-p-n."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SLUG = 'regression-when-p-n'
text = (ROOT / "articles" / (SLUG + ".qmd")).read_text(encoding="utf-8")
worked = text.split("{#worked-example}", 1)[1].split("\n## ", 1)[0]
answer = worked.split('title="Answer"}', 1)[1]

import math
import numpy as np
from scipy import stats, special, linalg, integrate

X=np.array([[1.,0,1],[0,1,1]]);y=np.array([1.,2.]);assert np.linalg.matrix_rank(X)==2 and np.linalg.matrix_rank(X.T@X)==2
assert np.allclose(np.linalg.pinv(X)@y,[0,1,1])
for t in [-3,0,1,4]:
 b=np.array([1-t,2-t,t]);assert np.allclose(X@b,y)
 assert np.dot([1,1,0],b)==3-2*t and np.dot([1,1,2],b)==3
b=np.linalg.solve(X.T@X+np.eye(3),X.T@y)
assert np.allclose(b,[.125,.625,.75]) and np.allclose(X@b,[.875,1.375])
assert np.isclose(np.sum((y-X@b)**2),.40625)
assert 3**2+3**2==18
assert 12-8==4

# Match computed worked-example and practice results to their generated text.
assert '('+','.join(f'{z:g}' for z in b)+')^T' in worked
assert '('+','.join(f'{z:g}' for z in X@b)+')^T' in worked
assert f"residual sum of squares ${np.sum((y-X@b)**2):.5f}$" in worked
exercise_pair=np.full(2,6/2)
assert 'minimised at $('+','.join(f'{z:g}' for z in exercise_pair)+')$' in answer
print("regression-when-p-n: numerical checks passed")
