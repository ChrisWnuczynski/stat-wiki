"""Checks for Fisher–Neyman factorisation."""

from math import comb
from pathlib import Path

root = Path(__file__).resolve().parents[1]
prose = (root / "research/content/fisher-neyman-factorisation.md").read_text(encoding="utf-8")
article = root / "articles/fisher-neyman-factorisation.qmd"
target = article.read_text(encoding="utf-8").split("## See also", 1)[0] if article.is_file() else prose

assert comb(4, 2) == 6
assert abs(1 / comb(4, 2) - 1 / 6) < 1e-12
assert abs(1 / comb(3, 2) - 1 / 3) < 1e-12
assert abs(1 / comb(5, 1) - 1 / 5) < 1e-12
for printed in ("1/6", "1/3", "1/5"):
    assert printed in target, printed
assert "**Your turn.**" in prose and 'collapse="true"' in prose
assert prose.count('title="Answer"') >= 3
print("fisher-neyman checks passed")
