"""Recompute the displayed examples and practice answers."""
import math
from fractions import Fraction
import numpy as np
from scipy import stats, optimize
from pathlib import Path

o=np.array([23,50,20]); e=93*np.array([.25,.5,.25]); t=np.sum((o-e)**2/e)
assert round(t,5)==.72043 and round(stats.chi2.sf(t,2),5)==.69753
assert np.allclose(e,[23.25,46.5,23.25]) and round(stats.chi2.ppf(.95,2),3)==5.991
for o,t,p in [([18,12,30],8.4,.0150),([20,15,25],2.5,.2865)]:
 assert math.isclose(sum((np.array(o)-20)**2/20),t)
 assert round(stats.chi2.sf(t,2),4)==p
p=np.array([.25,.5,.25]);u=np.sqrt(p);P=np.eye(3)-np.outer(u,u)
assert np.allclose(P@P,P) and np.linalg.matrix_rank(P)==2

# Compare recomputed results with the generated worked example and practice answer.
ROOT = Path(__file__).resolve().parents[1]
SLUG = 'chi-squared-test-with-known-cell-probabilities'
article = (ROOT / "articles" / (SLUG + ".qmd")).read_text(encoding="utf-8")
worked_section = article.split("{#worked-example}", 1)[1].split("\n## ", 1)[0]
worked_example, your_turn = worked_section.split("**Your turn.**", 1)

worked_t=np.sum((np.array([18,12,30])-20)**2/20)
practice_t=np.sum((np.array([20,15,25])-20)**2/20)
assert f"={worked_t:.1f}." in worked_example
assert f"${stats.chi2.sf(worked_t,2):.4f}$" in worked_example
assert f"={practice_t:.1f}$" in your_turn
assert f"={stats.chi2.sf(practice_t,2):.4f}$" in your_turn

print("chi-squared-test-with-known-cell-probabilities: numerical checks passed")
