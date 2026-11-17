"""Check the dataset article's arithmetic and required sections."""
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
prose = (root / "research/content/dataset.md").read_text(encoding="utf-8")
page = (root / "articles/dataset.qmd").read_text(encoding="utf-8")
keys = re.findall(r"\{\{cite:([^}]+)\}\}", prose)
assert len(keys) >= 5, keys
assert len(set(keys)) >= 2, set(keys)
for heading in ("## Motivating example", "## Worked example", "**Your turn.**", 'title="Answer"'):
    assert heading in prose, heading
assert "## Check yourself {#check-yourself}" in page
hidden = re.findall(r'title="Answer"\}(.*?)\n:+', prose, flags=re.S)
for block in hidden:
    assert "{cite:" not in block

sizes = [2, 4, 3, 2, 5]
assert sum(sizes) / len(sizes) == 3.2
reduced = [2, 4, 3, 2]
assert reduced.count(2) / len(reduced) == 0.5
assert sum(reduced) / len(reduced) == 2.75
