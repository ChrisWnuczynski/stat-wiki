"""Independent numerical and algebraic checks for fisher-s-exact-test."""
import math
from pathlib import Path
import numpy as np


from scipy.stats import hypergeom, fisher_exact
ks=np.arange(1,11);pm=hypergeom.pmf(ks,20,11,10);obs=hypergeom.pmf(8,20,11,10)
assert abs(pm.sum()-1)<1e-13
assert abs(obs-.03215051202667302)<1e-14
assert abs(hypergeom.sf(7,20,11,10)-.03488925934746368)<1e-14
assert abs(pm[pm<=obs+1e-14].sum()-.06977851869492736)<1e-14
assert np.array_equal(ks[pm<=obs+1e-14],[1,2,3,8,9,10])
assert abs(fisher_exact([[8,2],[3,7]]).pvalue-.06977851869492736)<1e-14
assert 8*7/(2*3)==28/3
assert 10*11/20==5.5 and 10*9/20==4.5

assert abs(hypergeom.pmf(3,7,4,3)-4/35)<1e-14

root=Path(__file__).resolve().parents[1]
body=(root / "articles" / "fisher-s-exact-test.qmd").read_text()
source=(root / "research/content" / "fisher-s-exact-test.md").read_text()
assert "**Your turn.**" in body
assert len(__import__("re").findall(r"\{\{cite:",source)) >= 5
for token in ['0.0321505', '0.0348893', '0.0697785']:
    assert token in body, (token, "fisher-s-exact-test")
print("fisher-s-exact-test: numerical and algebraic checks passed")
