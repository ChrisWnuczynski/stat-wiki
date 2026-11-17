"""Check the census article's arithmetic and required sections."""
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
prose = (root / "research/content/census.md").read_text(encoding="utf-8")
page = (root / "articles/census.qmd").read_text(encoding="utf-8")
keys = re.findall(r"\{\{cite:([^}]+)\}\}", prose)
assert len(keys) >= 5, keys
assert len(set(keys)) >= 2, set(keys)
for heading in ("## Motivating example", "## Worked example", "**Your turn.**", 'title="Answer"'):
    assert heading in prose, heading
assert "## Check yourself {#check-yourself}" in page
hidden = re.findall(r'title="Answer"\}(.*?)\n:+', prose, flags=re.S)
for block in hidden:
    assert "{cite:" not in block

base = [5, 7, 6, 8, 5, 9, 6, 4]
assert sum(base) == 50
assert sum(base) / 8 == 6.25
assert sum(base + [7, 9]) / 10 == 6.6
assert (5 + 8 + 4) / 3 == 17 / 3
