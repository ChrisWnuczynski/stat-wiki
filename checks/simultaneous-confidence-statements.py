"""Recompute numerical examples and exercise answers for simultaneous-confidence-statements."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SLUG = 'simultaneous-confidence-statements'
text = (ROOT / "articles" / (SLUG + ".qmd")).read_text(encoding="utf-8")
worked = text.split("{#worked-example}", 1)[1].split("\n## ", 1)[0]
answer = worked.split('title="Answer"}', 1)[1]

import math
import numpy as np
from scipy import stats, special, linalg, integrate

S=np.array([[4.,1],[1,9]]);C=.2*S;c=18*2/17*stats.f.ppf(.95,2,17)
assert round(c,6)==7.605594
assert np.allclose(np.round(np.sqrt(c*np.diag(C)),6),[2.466673,3.700009])
a=np.ones(2);assert a@C@a==3 and round(math.sqrt(c*a@C@a),6)==4.776692
assert math.sqrt(9*4)==6 and round(math.sqrt(45),6)==6.708204
for a in [np.array([1.,0]),np.array([1.,1]),np.array([2.,-1])]:
 h=math.sqrt(c)*C@a/math.sqrt(a@C@a)
 assert np.isclose(h@np.linalg.solve(C,h),c) and np.isclose(a@h,math.sqrt(c*a@C@a))
assert math.isclose(3*(.05/3),.05)

# Match computed worked-example and practice results to their generated text.
assert rf"c\approx{c:.6f}" in worked
coordinate_widths=np.sqrt(c*np.diag(C))
assert f"approximately ${coordinate_widths[0]:.6f}$ and ${coordinate_widths[1]:.6f}$" in worked
assert rf"\approx{math.sqrt(c*np.ones(2)@C@np.ones(2)):.6f}" in worked
assert rf"\approx{math.sqrt(45):.6f}" in answer and f"={math.sqrt(9*4):g}$" in answer
print("simultaneous-confidence-statements: numerical checks passed")
