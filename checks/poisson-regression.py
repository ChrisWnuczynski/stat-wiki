"""Arithmetic for the Poisson-regression depth pass."""
from math import log
from pathlib import Path

root = Path(__file__).resolve().parents[1]
prose = (root / "research/content/poisson-regression.md").read_text(encoding="utf-8")
page = root / "articles/poisson-regression.qmd"
assert page.is_file(), "generate articles before this check"
body = page.read_text(encoding="utf-8").split("## See also", 1)[0]

assert 4 / 2 == 2 and 9 / 3 == 3
assert (4 + 9) / (2 + 3) == 2.6
assert abs(2.6 * 2 - 5.2) < 1e-12 and abs(2.6 * 3 - 7.8) < 1e-12
assert abs(6 / 13 - 0.4615384615) < 1e-9
assert round(6 / 13, 4) == 0.4615
assert round(25 / 13, 4) == 1.9231
assert round(log(2), 4) == 0.6931
assert round(log(1.5), 4) == 0.4055
assert round(6.5 / 3, 4) == 2.1667
assert 8 / 4 == 2
assert 9 / 4 == 2.25

for printed in ("0.6931", "0.4055", "2.6", "5.2", "7.8", "0.4615", "1.9231", "2.1667", "2.25"):
    assert printed in prose and printed in body, printed
assert prose.count('title="Proof"') == 1
assert "**Your turn.**" in prose and "## Check yourself" in prose
assert prose.count('title="Answer"') == 4
print("poisson-regression arithmetic passed")
