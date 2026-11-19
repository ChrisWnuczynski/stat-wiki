"""Check Poisson and Brownian increment calculations."""

import math
from pathlib import Path

root = Path(__file__).resolve().parents[1]
page = (root / "articles/stationary-and-independent-increments.qmd").read_text()
body = page.split("## See also", 1)[0]

assert round(math.exp(-1), 4) == 0.3679
assert round(math.exp(-2), 4) == 0.1353
assert 2 * 0.5 == 1
assert 3 * (1 / 3) == 1
# inhomogeneous
assert 1 + 4 == 5

for printed in ("0.3679", "0.1353", "e^{-1}", "e^{-2}"):
    assert printed in body, printed
assert body.count('title="Proof"') == 1
assert "**Your turn.**" in body and "## Check yourself" in body
assert body.count('title="Answer"') >= 3
for qid in ("depth-stationary-and-independent-increments-q1", "depth-stationary-and-independent-increments-q2"):
    assert f"../questions/{qid}.qmd" in page
assert 'data-cite-key="durrett2019"' in body
print("stationary and independent increments checks passed")
