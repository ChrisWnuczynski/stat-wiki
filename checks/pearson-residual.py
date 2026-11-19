"""Check Pearson residual arithmetic."""

import math
from pathlib import Path

root = Path(__file__).resolve().parents[1]
page = (root / "articles/pearson-residual.qmd").read_text()
body = page.split("## See also", 1)[0]

assert round(5 / math.sqrt(2), 4) == 3.5355
assert round(5 / math.sqrt(50), 4) == 0.7071
assert round(math.sqrt(0.21), 4) == 0.4583
assert round(0.3 / math.sqrt(0.21), 4) == 0.6547
assert round(-0.7 / math.sqrt(0.21), 4) == -1.5275
assert round(math.sqrt(8), 4) == 2.8284
assert round(6 / math.sqrt(8), 4) == 2.1213
assert round(9 / math.sqrt(18), 4) == 2.1213
assert abs(0.8 / 0.4 - 2) < 1e-12
assert abs(-0.2 / 0.4 + 0.5) < 1e-12

for printed in (
    "3.5355", "0.7071", "0.4583", "0.6547", "-1.5275", "2.8284", "2.1213",
    "0.21",
):
    assert printed in body, printed
assert body.count('title="Proof"') == 1
assert "**Your turn.**" in body and "## Check yourself" in body
assert body.count('title="Answer"') >= 3
for qid in ("depth-pearson-residual-q1", "depth-pearson-residual-q2"):
    assert f"../questions/{qid}.qmd" in page
assert 'data-cite-key="dodge2008"' in body
print("pearson residual checks passed")
