"""Arithmetic checks for the jump chain article."""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tools.shown import shown
import math

root = Path(__file__).resolve().parents[1]
text = (root / "research/content/jump-chain.md").read_text()
text = shown(text, "jump-chain")
body = (root / "articles/jump-chain.qmd").read_text().split("## See also", 1)[0]
assert 2 / 6 == 1 / 3 and 4 / 6 == 2 / 3
assert abs(math.exp(-3) - 0.049787068367863944) < 1e-15
assert round(math.exp(-3), 5) == 0.04979
assert 2 + 4 + 6 == 12 and 4 / 12 == 1 / 3
assert 5 / 10 == 1 / 2 and abs(1 / 10 - 0.1) < 1e-12
# two-clock race
a, b = 2.0, 4.0
# integral a e^{-(a+b)t} dt = a/(a+b)
assert abs(a / (a + b) - 1 / 3) < 1e-12
for printed in ("1/3", "2/3", "1/6", "0.04979", "4/12", "1/2", "1/10"):
    assert printed in text, printed
    assert printed in body, printed
assert "**Your turn.**" in body and 'title="Proof"' in body
print("jump chain checks passed")
