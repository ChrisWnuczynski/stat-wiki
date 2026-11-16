"""Check count-mixture moments and page structure."""
import math
from pathlib import Path
root = Path(__file__).resolve().parents[1]
body = (root / "articles/count-models-beyond-the-poisson.qmd").read_text().split("## See also", 1)[0]
assert (2+6)/2 == 4
assert ((2-4)**2 + (6-4)**2)/2 == 4
assert 4+4 == 8
assert abs(math.exp(-4) - 0.0183) < 5e-5
mix = (math.exp(-2)+math.exp(-6))/2
assert abs(mix - 0.0689) < 5e-5
assert abs(mix/math.exp(-4) - 3.76) < 0.005
assert (3/4)*2 + (1/4)*6 == 3
assert (3/4)*(2-3)**2 + (1/4)*(6-3)**2 == 3
assert 3+3 == 6
assert (1+5)/2 == 3
assert ((1-3)**2+(5-3)**2)/2 == 4
assert 3+4 == 7
for s in ("0.0183", "0.0689", "3.76", "12"):
    assert s in body, s
assert body.count('title="Proof"') == 1
assert "**Your turn.**" in body and "## Check yourself" in body
assert 'data-cite-key="dodge2008"' in body
print("count models passed")
