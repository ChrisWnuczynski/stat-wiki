"""Checks for the link-function article."""

from math import exp
from pathlib import Path

root = Path(__file__).resolve().parents[1]
prose = (root / "research/content/link-function.md").read_text(encoding="utf-8")
article = root / "articles/link-function.qmd"
target = article.read_text(encoding="utf-8").split("## See also", 1)[0] if article.is_file() else prose

assert round(exp(1.5), 4) == 4.4817
assert round(exp(1.5) / (1 + exp(1.5)), 4) == 0.8176
assert round(exp(-1), 4) == 0.3679
assert round(1 / (1 + exp(1)), 4) == 0.2689
assert round(exp(0.2), 4) == 1.2214
assert exp(0) == 1

for printed in ("4.4817", "0.8176", "0.3679", "0.2689", "1.2214", "1.5"):
    assert printed in target, printed
assert 'title="Proof"' in prose and "**Your turn.**" in prose
assert prose.count('title="Answer"') >= 3
print("link-function checks passed")
