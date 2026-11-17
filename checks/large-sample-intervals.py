"""Recompute the numerical examples and exercises for this article."""
import math
from fractions import Fraction as F
import numpy as np
from scipy import stats

from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SLUG='large-sample-intervals'
ARTICLE=(ROOT / "articles" / (SLUG + ".qmd")).read_text(encoding="utf-8")
WORKED=ARTICLE.split("{#worked-example}",1)[1].split("\n## ",1)[0]
EXAMPLE,TURN=WORKED.split("**Your turn.**",1)
ANSWER=TURN.split('title="Answer"}',1)[1].split("\n:::",1)[0]

def close(a,b,tol=1e-6):
    assert np.allclose(a,b,rtol=0,atol=tol), (a,b)

n,mean,s=51,1136,178
se=s/math.sqrt(n);close(se,24.9249854957)
h=1.96*se;close(h,48.8529715716)
close([mean-h,mean+h],[1087.1470284284,1184.8529715716])
q=stats.t.ppf(.975,50);close(q,2.0085591121)
close([mean-q*se,mean+q*se],[1085.9366932636,1186.0633067364])
close((1.96*178/25)**2,194.74760704);assert math.ceil((1.96*178/25)**2)==195
close([20-1.96*5/10,20+1.96*5/10],[19.02,20.98])
close(1.96*5/math.sqrt(400),.49)
# Compare computed values with the worked example and hidden answer.
assert f"${se:.6f}$" in EXAMPLE
assert f"${h:.6f}$" in EXAMPLE
assert f"${mean-h:.6f}$ and ${mean+h:.6f}$" in EXAMPLE
turn_se=5/math.sqrt(100)
turn_margin=1.96*turn_se
assert f"standard error is ${turn_se:.1f}$" in ANSWER
assert rf"20\pm{turn_margin:.2f}=({20-turn_margin:.2f},{20+turn_margin:.2f})" in ANSWER
assert f"sample of ${int(100*2**2)}$" in ANSWER
print("large-sample-intervals: numerical checks passed")
