"""Checks for the count-responses article."""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tools.shown import shown

from math import exp

root = Path(__file__).resolve().parents[1]
prose = (root / "research/content/count-responses.md").read_text(encoding="utf-8")
prose = shown(prose, "count-responses")
article = root / "articles/count-responses.qmd"
target = article.read_text(encoding="utf-8").split("## See also", 1)[0] if article.is_file() else prose

assert round(exp(-1.5), 4) == 0.2231
assert round(exp(-0.2), 4) == 0.8187
assert round(exp(-1.7), 4) == 0.1827
assert abs(exp(-1.7) / exp(-1.5) - exp(-0.2)) < 1e-12
assert round(exp(0.5), 4) == 1.6487
assert round(exp(0.3), 4) == 1.3499
assert abs(exp(0.3) / exp(0.5) - exp(-0.2)) < 1e-12
assert round(exp(-0.4), 4) == 0.6703
assert abs(exp(-0.4) - exp(-0.2) ** 2) < 1e-12
assert 2 - 0.5 * 4 == 0

for printed in ("0.2231", "0.8187", "0.1827", "1.6487", "1.3499", "0.6703"):
    assert printed in target, printed
assert 'title="Proof"' in prose and "**Your turn.**" in prose
assert prose.count('title="Answer"') >= 3
print("count-responses checks passed")
