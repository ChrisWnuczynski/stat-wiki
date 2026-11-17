"""Recompute numerical examples and exercise answers for uniformisation."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SLUG = 'uniformisation'
text = (ROOT / "articles" / (SLUG + ".qmd")).read_text(encoding="utf-8")
worked = text.split("{#worked-example}", 1)[1].split("\n## ", 1)[0]
answer = worked.split('title="Answer"}', 1)[1]

import math
import numpy as np
from scipy import stats, special, linalg, integrate

Q=np.array([[-2.,2],[3,-3]])
for gamma in [3.,5.,10.]:
 R=np.eye(2)+Q/gamma;assert np.min(R)>=0 and np.allclose(R.sum(axis=1),1)
 result=sum(stats.poisson.pmf(n,gamma)*np.linalg.matrix_power(R,n) for n in range(100))
 assert np.allclose(result,linalg.expm(Q))
R=np.array([[.6,.4],[.6,.4]]);assert np.allclose(R@R,R)
assert round(.4*(1-math.exp(-5)),6)==.397305 and np.isclose(.6*2+.4*3,2.4) and np.isclose(5-2.4,2.6)
assert 1-4/3<0 and np.isclose(1-4/5,.2)
assert np.isclose(stats.poisson.sf(20,5),8.1093e-8,rtol=1e-5,atol=0)
M=20;P=sum(stats.poisson.pmf(n,5)*np.linalg.matrix_power(R,n) for n in range(M+1))
assert np.allclose(P.sum(axis=1),stats.poisson.cdf(M,5))
assert np.max(linalg.expm(Q)-P)<=stats.poisson.sf(M,5)+1e-14
assert np.allclose(linalg.expm(np.zeros((2,2))),np.eye(2))

# Match computed worked-example and practice results to their generated text.
assert rf"\approx{.4*(1-math.exp(-5)):.6f}" in worked
real_rate=.6*2+.4*3
assert f"0.4(3)={real_rate:g}$" in worked and f"5-2.4={5-real_rate:g}$" in worked
assert f"1-4/5={1-4/5:g}$" in answer
assert f"{stats.poisson.sf(20,5)/1e-8:.4f}" in text
print("uniformisation: numerical checks passed")
