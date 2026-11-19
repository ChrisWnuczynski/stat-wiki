"""Arithmetic checks for Tukey intervals."""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tools.shown import shown


from scipy.stats import studentized_range

root = Path(__file__).resolve().parents[1]
prose = (root / "research/content/tukey-intervals.md").read_text(encoding="utf-8")
prose = shown(prose, "tukey-intervals")
article = root / "articles/tukey-intervals.qmd"
target = article.read_text(encoding="utf-8").split("## See also", 1)[0] if article.is_file() else prose

corn = studentized_range.ppf(0.95, 5, 10)
assert round(corn, 3) == 4.654
q = studentized_range.ppf(0.95, 3, 8)
assert round(q, 3) == 4.041
half = q * (6.25 ** 0.5) / (4 ** 0.5)
assert round(half, 3) == 5.051
assert (round(8 - half, 3), round(8 + half, 3)) == (2.949, 13.051)
assert (round(4 - half, 3), round(4 + half, 3)) == (-1.051, 9.051)
assert (round(6 - half, 3), round(6 + half, 3)) == (0.949, 11.051)
wide = q * 5 / 2
assert round(wide, 3) == 10.103

for printed in ("4.041", "5.051", "2.949", "13.051", "-1.051", "9.051",
                "0.949", "11.051", "10.103", "6.25"):
    assert printed in target, printed
assert 'title="Proof"' in prose and "**Your turn.**" in prose
assert prose.count('title="Answer"') >= 3
print("tukey-intervals checks passed")
