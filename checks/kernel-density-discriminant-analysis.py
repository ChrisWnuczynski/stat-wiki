"""Recompute the numerical examples and exercises for this article."""
import math
from fractions import Fraction as F
import numpy as np
from scipy import stats

from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SLUG='kernel-density-discriminant-analysis'
ARTICLE=(ROOT / "articles" / (SLUG + ".qmd")).read_text(encoding="utf-8")
WORKED=ARTICLE.split("{#worked-example}",1)[1].split("\n## ",1)[0]
EXAMPLE,TURN=WORKED.split("**Your turn.**",1)
ANSWER=TURN.split('title="Answer"}',1)[1].split("\n:::",1)[0]

def close(a,b,tol=1e-6):
    assert np.allclose(a,b,rtol=0,atol=tol), (a,b)

phi=lambda z:math.exp(-z*z/2)/math.sqrt(2*math.pi)
f=lambda x,a:sum(phi(x-v) for v in a)/len(a)
a,b=[0,1],[4,5]
f1,f2=f(3,a),f(3,b)
close([f1,f2],[.02921140746,.14798084552])
close([f1/2,f2/2],[.01460570373,.07399042276])
close(f2/f1,5.065858114); close(f2/(f1+f2),.835142863)
assert .9*f1>.1*f2
close(f(2.5,a),f(2.5,b))
close([.3*f(2.5,a)/f(2.5,a),.7*f(2.5,b)/f(2.5,a)],[.3,.7])
close(.8/(.8+.2*4),.5)
# Each shifted Gaussian bump has unit integral at multiple bandwidths.
for h in [.2,1,10]:
 from scipy.integrate import quad
 close(quad(lambda x:phi((x-2)/h)/h,-np.inf,np.inf)[0],1)
# Compare computed values with the worked example and hidden answer.
for value in (f1,f2):
    assert f"${value:.7f}$" in EXAMPLE
assert f"${f2/f1:.4f}$" in EXAMPLE
assert f"${f2/(f1+f2):.5f}$" in EXAMPLE
posterior=np.array([.3*f(2.5,a),.7*f(2.5,b)])
posterior/=posterior.sum()
assert f"${posterior[0]:.1f}$ and ${posterior[1]:.1f}$" in ANSWER
print("kernel-density-discriminant-analysis: numerical checks passed")
