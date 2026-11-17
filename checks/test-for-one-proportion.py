"""Recompute numerical examples and exercise answers for test-for-one-proportion."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SLUG = 'test-for-one-proportion'
text = (ROOT / "articles" / (SLUG + ".qmd")).read_text(encoding="utf-8")
worked = text.split("{#worked-example}", 1)[1].split("\n## ", 1)[0]
answer = worked.split('title="Answer"}', 1)[1]

import math
import numpy as np
from scipy import stats, special, linalg, integrate

assert stats.binom.sf(7,10,.5)==56/1024 and stats.binom.sf(8,10,.5)==11/1024
assert 2*stats.binom.sf(7,10,.5)==.109375
assert round(stats.binom.sf(8,10,.8),5)==.37581
z=(120-100)/math.sqrt(50);assert round(z,4)==2.8284
assert round(stats.norm.sf(z),5)==.00234
assert round(stats.binom.sf(119,200,.5),5)==.00284
assert round(stats.norm.sf((119.5-100)/math.sqrt(50)),5)==.00291
assert stats.binom.sf(4,5,.5)==.03125
assert stats.binom.sf(3,5,.5)>.05
assert math.sqrt(.5*.5/100)==.05 and math.isclose((.6-.5)/.05,2)

# Match computed worked-example and practice results to their generated text.
assert rf"\approx{stats.binom.sf(8,10,.8):.5f}" in worked
assert f"1/32={stats.binom.sf(4,5,.5):.5f}" in answer
assert f"size ${stats.binom.sf(4,5,.5):.5f}$" in answer
print("test-for-one-proportion: numerical checks passed")
