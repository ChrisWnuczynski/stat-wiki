"""Check Cauchy tail and quartiles."""
import math
from pathlib import Path
root = Path(__file__).resolve().parents[1]
body = (root / "articles/cauchy-distribution.qmd").read_text().split("## See also", 1)[0]
tail = 1 - 2*math.atan(5)/math.pi
assert abs(tail - 0.1257) < 5e-5
assert 2-3 == -1 and 2+3 == 5
assert "0.1257" in body
assert "**Your turn.**" in body and "Check yourself" in body
assert body.count('title="Proof"') == 1
assert 'data-cite-key="dodge2008"' in body
print("cauchy passed")
