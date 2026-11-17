"""Recompute the displayed examples and practice answers."""
import math
from fractions import Fraction
import numpy as np
from scipy import stats, optimize
from pathlib import Path

def collision(n,m):return 1-math.prod((m-j)/m for j in range(n)) if n<=m else 1
assert math.comb(23,2)==253
for n,value in [(23,.507),(40,.891),(50,.970)]:assert round(collision(n,365),3)==value
assert collision(22,365)<.5<collision(23,365)
assert math.isclose(collision(5,10),.6976)
assert math.isclose(collision(4,10),.496)
assert math.comb(4,2)/10==.6
assert math.perm(10,5)==30240
assert round(math.comb(23,2)/365,4)==.6932
assert round(collision(23,365),4)==.5073
# Exact enumeration confirms pairwise independence but not mutual independence.
from itertools import product
triples=list(product(range(3),repeat=3))
a=np.array([int(x[0]==x[1]) for x in triples]);b=np.array([int(x[0]==x[2]) for x in triples]);c=np.array([int(x[1]==x[2]) for x in triples])
assert math.isclose(np.mean(a*b),1/9) and math.isclose(np.mean(a*b*c),1/9)
assert not math.isclose(np.mean(a*b*c),1/27)

# Compare recomputed results with the generated worked example and practice answer.
ROOT = Path(__file__).resolve().parents[1]
SLUG = 'birthday-problem'
article = (ROOT / "articles" / (SLUG + ".qmd")).read_text(encoding="utf-8")
worked_section = article.split("{#worked-example}", 1)[1].split("\n## ", 1)[0]
worked_example, your_turn = worked_section.split("**Your turn.**", 1)

assert str(math.perm(10,5)) in worked_example
assert f"${collision(5,10):.4f}$" in worked_example
assert f"${collision(4,10):.3f}$" in your_turn
assert f"${math.comb(4,2)/10:.1f}$" in your_turn

print("birthday-problem: numerical checks passed")
