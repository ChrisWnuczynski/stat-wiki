"""Recompute numerical examples and exercise answers for variable-importance."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SLUG = 'variable-importance'
text = (ROOT / "articles" / (SLUG + ".qmd")).read_text(encoding="utf-8")
worked = text.split("{#worked-example}", 1)[1].split("\n## ", 1)[0]
answer = worked.split('title="Answer"}', 1)[1]

import math
import numpy as np
from scipy import stats, special, linalg, integrate

y=np.array([0,0,1,1]);x=y.copy();permuted=np.array([1,0,1,0]);assert np.mean(x!=y)==0 and np.mean(permuted!=y)==.5
import itertools
errors=[np.mean(np.array(p)!=y) for p in itertools.permutations(x)]
assert np.isclose(np.mean(errors),.5)
assert np.isclose(.16-.10,.06) and np.isclose((.16-.10)/.10,.60)
assert np.isclose(.31-.12,.19) and np.isclose(.13-.12,.01)
assert round(100*(.31-.12)/.12,1)==158.3 and round(100*(.13-.12)/.12,1)==8.3
assert 5-4==1 and (5-4)/4==.25

# Match computed worked-example and practice results to their generated text.
assert f"importance for this shuffle is ${np.mean(permuted!=y)-np.mean(x!=y):g}$" in worked
assert f"expected importance is ${np.mean(errors)-np.mean(x!=y):g}$" in worked
assert f"0.16-0.10={.16-.10:.2f}" in answer
assert f"0.06/0.10={(.16-.10)/.10:.2f}" in answer
assert rf"{100*(.16-.10)/.10:g}\%" in answer
print("variable-importance: numerical checks passed")
