"""Check the parameter article's arithmetic and required sections."""
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
prose = (root / "research/content/parameter.md").read_text(encoding="utf-8")
page = (root / "articles/parameter.qmd").read_text(encoding="utf-8")
keys = re.findall(r"\{\{cite:([^}]+)\}\}", prose)
assert len(keys) >= 5, keys
assert len(set(keys)) >= 2, set(keys)
for heading in ("## Motivating example", "## Worked example", "**Your turn.**", 'title="Answer"'):
    assert heading in prose, heading
assert "## Check yourself {#check-yourself}" in page
hidden = re.findall(r'title="Answer"\}(.*?)\n:+', prose, flags=re.S)
for block in hidden:
    assert "{cite:" not in block

pop = [2, 4, 6, 8, 10]
assert sum(pop) / 5 == 6
assert sum([2, 4, 6]) / 3 == 4
assert sum(pop + [16]) / 6 == 23 / 3
