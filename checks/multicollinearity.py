"""Arithmetic for the multicollinearity depth pass."""
from math import sqrt
from pathlib import Path

root = Path(__file__).resolve().parents[1]
prose = (root / "research/content/multicollinearity.md").read_text(encoding="utf-8")
page = root / "articles/multicollinearity.qmd"
assert page.is_file(), "generate articles before this check"
body = page.read_text(encoding="utf-8").split("## See also", 1)[0]

s11, s22, s12 = 10, 50, 22
assert s12 ** 2 / (s11 * s22) == 0.968
r = s12 / (s11 * s22) ** 0.5
assert round(r, 4) == 0.9839
assert abs(1 / (1 - 0.968) - 31.25) < 1e-12
assert round(sqrt(31.25), 3) == 5.590
det = s11 * s22 - s12 ** 2
assert det == 16
# responses
s1y, s2y = 7, 17
b1 = (s1y * s22 - s2y * s12) / det
b2 = (s2y * s11 - s1y * s12) / det
assert b1 == -1.5 and b2 == 1
assert s1y / s11 == 0.7
assert 10 * 40 - 20 ** 2 == 0
assert 1 / (1 - 0.36) == 1.5625

for printed in ("0.968", "0.9839", "31.25", "5.590", "-1.5", "0.7", "1.5625", "0.032"):
    assert printed in prose, printed
    assert printed in body, printed
assert prose.count('title="Proof"') == 1
assert "**Your turn.**" in prose and "## Check yourself" in prose
assert prose.count('title="Answer"') == 4
assert "{{cite:dodge2008}}" in prose
print("multicollinearity arithmetic passed")
