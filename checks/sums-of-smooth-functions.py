"""Arithmetic for the sums-of-smooth-functions depth pass."""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tools.shown import shown
from math import exp

root = Path(__file__).resolve().parents[1]
prose = (root / "research/content/sums-of-smooth-functions.md").read_text(encoding="utf-8")
prose = shown(prose, "sums-of-smooth-functions")
page = root / "articles/sums-of-smooth-functions.qmd"
assert page.is_file(), "generate articles before this check"
body = page.read_text(encoding="utf-8").split("## See also", 1)[0]

etas = {
    (0, 0): 1 - 0.3 - 0.5,
    (0, 1): 1 - 0.3 + 0.5,
    (1, 0): 1 + 0.3 - 0.5,
    (1, 1): 1 + 0.3 + 0.5,
}
expected = {(0, 0): 0.2, (0, 1): 1.2, (1, 0): 0.8, (1, 1): 1.8}
for key, value in expected.items():
    assert abs(etas[key] - value) < 1e-12, (key, etas[key])
assert abs((etas[1, 1] - etas[1, 0]) - (etas[0, 1] - etas[0, 0])) < 1e-12
assert abs((2.4 - 0.8) - (1.2 - 0.2) - 0.6) < 1e-12
assert round(exp(0.6), 4) == 1.8221
assert round(exp(1.8), 4) == 6.0496
assert round(exp(2.4), 4) == 11.0232
assert 4 - 1 == 3
for printed in ("0.2", "1.2", "0.8", "1.8", "0.6", "1.8221", "6.0496", "11.0232"):
    assert printed in prose and printed in body, printed
assert prose.count('title="Proof"') == 1
assert "**Your turn.**" in prose and "## Check yourself" in prose
assert prose.count('title="Answer"') == 4
print("sums-of-smooth-functions arithmetic passed")
