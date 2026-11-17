"""Independent numerical and algebraic checks for interarrival-time."""
import math
from pathlib import Path
import numpy as np


from scipy.stats import gamma,poisson
assert 1/4*60==15
assert abs(math.exp(-2)-.1353352832366127)<1e-14
assert abs(13*math.exp(-4)-.2381033055535443)<1e-14
assert abs(gamma.sf(1,a=3,scale=.25)-poisson.cdf(2,4))<1e-14
assert abs(math.log(2)/4-.17328679513998632)<1e-14
assert abs(math.exp(-4*(.5+.25))/math.exp(-4*.5)-math.exp(-1))<1e-14

assert abs(math.exp(-1.5)*1.5**2/2-.25102143016698353)<1e-14
assert 1/8==.125

root=Path(__file__).resolve().parents[1]
body=(root / "articles" / "interarrival-time.qmd").read_text()
source=(root / "research/content" / "interarrival-time.md").read_text()
assert "**Your turn.**" in body
assert len(__import__("re").findall(r"\{\{cite:",source)) >= 5
for token in ['0.135335', '0.238103', '0.173287']:
    assert token in body, (token, "interarrival-time")
print("interarrival-time: numerical and algebraic checks passed")
