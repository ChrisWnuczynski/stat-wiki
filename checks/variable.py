"""Check the variable article's arithmetic and required sections."""
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
prose = (root / "research/content/variable.md").read_text(encoding="utf-8")
page = (root / "articles/variable.qmd").read_text(encoding="utf-8")
keys = re.findall(r"\{\{cite:([^}]+)\}\}", prose)
assert len(keys) >= 5, keys
assert len(set(keys)) >= 2, set(keys)
for heading in ("## Motivating example", "## Worked example", "**Your turn.**", 'title="Answer"'):
    assert heading in prose, heading
assert "## Check yourself {#check-yourself}" in page
hidden = re.findall(r'title="Answer"\}(.*?)\n:+', prose, flags=re.S)
for block in hidden:
    assert "{cite:" not in block

masses = [4, 12, 5, 4, 9, 2]
assert sum(masses) / len(masses) == 6
assert masses.count(4) + [4, 12, 5, 4, 9, 2, 3].count(4) >= 2
