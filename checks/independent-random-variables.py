"""Arithmetic checks for independent random variables."""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tools.shown import shown

root = Path(__file__).resolve().parents[1]
text = (root / "research/content/independent-random-variables.md").read_text()
text = shown(text, "independent-random-variables")
body = (root / "articles/independent-random-variables.qmd").read_text().split("## See also", 1)[0]
assert abs(0.4 * 0.5 - 0.2) < 1e-12
joints = {(0, 0): 0.2, (0, 1): 0.3, (1, 0): 0.1, (1, 1): 0.4}
assert abs(sum(joints.values()) - 1) < 1e-12
ex = joints[(1, 0)] + joints[(1, 1)]
ey = joints[(0, 1)] + joints[(1, 1)]
exy = joints[(1, 1)]
assert ex == 0.5 and ey == 0.7 and exy == 0.4
assert abs(ex * ey - 0.35) < 1e-12
assert abs(0.6 * 0.5 - 0.3) < 1e-12
assert abs((1 / 2) * (1 / 3) - 1 / 6) < 1e-12
assert abs(0.25 - 0.25) < 1e-12
for printed in ("0.4", "0.5", "0.2", "0.3", "0.1", "0.7", "0.35", "1/6", "1/4"):
    assert printed in text, printed
    assert printed in body, printed
assert "**Your turn.**" in body and 'title="Proof"' in body
print("independent random variables checks passed")
