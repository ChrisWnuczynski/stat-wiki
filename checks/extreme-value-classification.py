"""Arithmetic checks for extreme-value classification."""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tools.shown import shown
import math

root = Path(__file__).resolve().parents[1]
text = (root / "research/content/extreme-value-classification.md").read_text()
text = shown(text, "extreme-value-classification")
body = (root / "articles/extreme-value-classification.qmd").read_text().split("## See also", 1)[0]
g20 = (1 - 1 / 20) ** 20
g50 = (1 - 1 / 50) ** 50
limit = math.exp(-1)
assert round(g20, 5) == 0.35849
assert round(limit, 5) == 0.36788
assert round((1 - 1 / 10) ** 10, 5) == 0.34868
assert round(g50, 5) == 0.36417
assert round(limit - g20, 5) == 0.00939
assert round(limit - g50, 5) == 0.00371
for printed in ("0.35849", "0.36788", "0.34868", "0.36417", "0.00371", "0.00939"):
    assert printed in text, printed
    assert printed in body, printed
assert "**Your turn.**" in body and 'title="Proof"' in body
print("extreme-value classification checks passed")
