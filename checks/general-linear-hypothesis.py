"""Recompute the displayed examples and practice answers."""
import math
from fractions import Fraction
import numpy as np
from scipy import stats, optimize
from pathlib import Path

x=np.arange(1,5);y=np.array([2,3,5,6]);X=np.c_[np.ones(4),x];b=np.linalg.lstsq(X,y,rcond=None)[0]
assert np.allclose(b,[.5,1.4])
rss1=sum((y-X@b)**2);rss0=sum((y-y.mean())**2)
assert math.isclose(rss1,.2) and rss0==10 and math.isclose((rss0-rss1)/(rss1/2),98)
assert round(stats.f.ppf(.95,1,2),1)==18.5
assert ((70-52)/2)/(52/26)==4.5
print('joint p',stats.f.sf(4.5,2,26),'exercise p',stats.f.sf(4,1,17))
assert (42-34)/(34/17)==4
P=X@np.linalg.inv(X.T@X)@X.T;P0=np.ones((4,4))/4
assert np.allclose((P-P0)@(np.eye(4)-P),0)
assert round(stats.f.sf(4.5,2,26),5)==.02098 and round(stats.f.sf(4,1,17),4)==.0617

# Compare recomputed results with the generated worked example and practice answer.
ROOT = Path(__file__).resolve().parents[1]
SLUG = 'general-linear-hypothesis'
article = (ROOT / "articles" / (SLUG + ".qmd")).read_text(encoding="utf-8")
worked_section = article.split("{#worked-example}", 1)[1].split("\n## ", 1)[0]
worked_example, your_turn = worked_section.split("**Your turn.**", 1)

worked_f=((70-52)/2)/(52/(30-4))
assert f"={worked_f:.1f}," in worked_example
assert f"p={stats.f.sf(worked_f,2,26):.5f}" in worked_example
practice_f=(42-34)/(34/17)
assert f"F=8/2={practice_f:g}" in your_turn
assert f"${stats.f.sf(practice_f,1,17):.4f}$" in your_turn
assert f"={((rss0-rss1)/(rss1/2)):.0f}" in article

print("general-linear-hypothesis: numerical checks passed")
