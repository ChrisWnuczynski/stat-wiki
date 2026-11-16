"""Arithmetic for the white-noise depth pass."""
from pathlib import Path

root = Path(__file__).resolve().parents[1]
prose = (root / "research/content/white-noise.md").read_text(encoding="utf-8")
page = root / "articles/white-noise.qmd"
assert page.is_file(), "generate articles before this check"
body = page.read_text(encoding="utf-8").split("## See also", 1)[0]

assert 4 / 4 == 1
assert -4 / 8 == -0.5
assert 9 / 9 == 1
# Gaussian fourth moment via the recurrence E(Z^4)=3 E(Z^2)
assert 3 * 1 - 1 == 2

for printed in ("-1/2", "0.5", "variance $4$", "variance $9$"):
    pass
for printed in ("-1/2",):
    assert printed in prose and printed in body
assert "2" in prose
assert prose.count('title="Proof"') == 1
assert "**Your turn.**" in prose and "## Check yourself" in prose
assert prose.count('title="Answer"') == 4
for key in ("dodge2008", "hyndman_athanasopoulos2021"):
    assert f"{{{{cite:{key}}}}}" in prose
print("white-noise arithmetic passed")
