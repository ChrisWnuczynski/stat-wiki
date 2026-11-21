"""Arithmetic for the posterior-membership depth pass."""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tools.shown import shown

root = Path(__file__).resolve().parents[1]
prose = (root / "research/content/posterior-membership.md").read_text(encoding="utf-8")
prose = shown(prose, "posterior-membership")
page = root / "articles/posterior-membership.qmd"
assert page.is_file(), "generate articles before this check"
body = page.read_text(encoding="utf-8").split("## See also", 1)[0]

assert abs(0.6 * 0.2 - 0.12) < 1e-12
assert abs(0.4 * 0.8 - 0.32) < 1e-12
assert abs(0.12 / 0.44 - 3 / 11) < 1e-12
assert abs(0.32 / 0.44 - 8 / 11) < 1e-12
assert round(3 / 11, 4) == 0.2727
assert round(8 / 11, 4) == 0.7273
assert abs(0.12 / 0.32 - 0.375) < 1e-12
assert abs((3 / 11 * 4) / (3 / 11 + 1) - 6 / 7) < 1e-12
assert round(6 / 7, 4) == 0.8571
assert round(7 / 11, 4) == 0.6364
assert abs(0.3 / 0.5 - 0.6) < 1e-12
for printed in ("0.2727", "0.7273", "0.375", "0.8571", "0.6364", "3/11", "8/11"):
    assert printed in prose and printed in body, printed
assert prose.count('title="Proof"') == 1
assert "**Your turn.**" in prose and "## Check yourself" in prose
assert prose.count('title="Answer"') == 4
print("posterior-membership arithmetic passed")
