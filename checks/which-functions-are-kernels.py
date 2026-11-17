"""Recompute numerical examples and exercise answers for which-functions-are-kernels."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SLUG = 'which-functions-are-kernels'
text = (ROOT / "articles" / (SLUG + ".qmd")).read_text(encoding="utf-8")
worked = text.split("{#worked-example}", 1)[1].split("\n## ", 1)[0]
answer = worked.split('title="Answer"}', 1)[1]

import math
import numpy as np
from scipy import stats, special, linalg, integrate

a=np.array([[1,2],[2,1]]);v=np.array([1,-1]);assert v@a@v==-2
x=np.array([-1.,0,1]);G=(1+np.outer(x,x))**2
P=np.column_stack([np.ones(3),np.sqrt(2)*x,x*x]);assert np.allclose(G,P@P.T)
assert np.allclose(G,[[4,1,0],[1,1,1],[0,1,4]])
assert np.allclose(np.linalg.eigvalsh(G),[(5-math.sqrt(17))/2,4,(5+math.sqrt(17))/2])
assert np.allclose(np.round(np.linalg.eigvalsh(G),4),[.4384,4,4.5616])
H=np.array([[1,-3],[-3,1]]);assert np.ones(2)@H@np.ones(2)==-4
for f in [[1,2],[0,0],[-3,7]]:assert np.linalg.matrix_rank(np.outer(f,f))<=1
assert -.2<0 and -1<0

# Match computed worked-example and practice results to their generated text.
eigenvalues=np.linalg.eigvalsh(G)
assert ','.join(f'{z:g}' if z==4 else f'{z:.4f}' for z in eigenvalues) in worked
assert f'quadratic form at $(1,1)^T$ is ${np.ones(2)@H@np.ones(2):g}$' in worked
maximum_rank=max(np.linalg.matrix_rank(np.outer(f,f)) for f in [[1,2],[0,0],[-3,7]])
assert 'rank is at most '+{0:'zero',1:'one'}[maximum_rank] in answer
print("which-functions-are-kernels: numerical checks passed")
