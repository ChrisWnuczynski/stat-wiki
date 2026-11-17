"""Recompute the displayed examples and practice answers."""
import math
from fractions import Fraction
import numpy as np
from scipy import stats, optimize
from pathlib import Path

o=np.array([[67,41,6],[129,183,32]]);e=o.sum(1)[:,None]*o.sum(0)[None,:]/o.sum();t=sum(((o-e)**2/e).flat)
assert o.sum()==458 and np.all(o.sum(1)==[114,344])
assert np.allclose(e,[[48.79,55.76,9.46],[147.21,168.24,28.54]],atol=.01)
assert round(t,2)==15.94 and round(stats.chi2.sf(t,2),6)==.000346
assert round(67/114,4)==.5877 and 129/344==.375
z=np.array([[20,30],[30,70]]);ee=z.sum(1)[:,None]*z.sum(0)[None,:]/z.sum();tt=np.sum((z-ee)**2/ee)
assert math.isclose(tt,1.5) and round(stats.chi2.sf(tt,1),4)==.2207
assert round(t,4)==15.9364
assert np.allclose(np.round((o-e)**2/e,2),[[6.80,3.90,1.26],[2.25,1.29,.42]])

# Compare recomputed results with the generated worked example and practice answer.
ROOT = Path(__file__).resolve().parents[1]
SLUG = 'contingency-tables'
article = (ROOT / "articles" / (SLUG + ".qmd")).read_text(encoding="utf-8")
worked_section = article.split("{#worked-example}", 1)[1].split("\n## ", 1)[0]
worked_example, your_turn = worked_section.split("**Your turn.**", 1)

assert f"T={tt:.1f}" in worked_example
assert f"p={stats.chi2.sf(tt,1):.4f}" in worked_example
for expectation in ee.flat:
 assert f"{expectation:.3f}" in worked_example
assert f"67/114={67/114:.4f}" in your_turn
assert f"129/344={129/344:.4f}" in your_turn
assert f"T={t:.2f}" in article

print("contingency-tables: numerical checks passed")
