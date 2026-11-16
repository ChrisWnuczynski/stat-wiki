"""Check random-slope marginal moments."""
import math
from pathlib import Path
root = Path(__file__).resolve().parents[1]
body = (root / "articles/random-slopes.qmd").read_text().split("## See also", 1)[0]
sa2, sb2, sab, s2 = 4, 1, -0.5, 1

def var(t):
    return sa2 + 2*t*sab + t**2*sb2 + s2

def cov(t, s):
    return sa2 + (t+s)*sab + t*s*sb2

assert var(2) == 7
assert cov(0, 2) == 3
assert var(1) == 5
# zero covariance
assert 4 + 4 + 1 == 9
assert (-0.5)/math.sqrt(4*1) == -0.25
assert 1*1 - 1.5**2 == -1.25
for s in ("$7$", "$3$", "$9$", "=5"):
    assert s in body, s
assert body.count('title="Proof"') == 1
assert "**Your turn.**" in body and "## Check yourself" in body
assert 'data-cite-key="bates_lme4_2015"' in body
print("random slopes passed")
