"""Check the data article's arithmetic and required sections."""
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
prose = (root / "research/content/data.md").read_text(encoding="utf-8")
page = (root / "articles/data.qmd").read_text(encoding="utf-8")
keys = re.findall(r"\{\{cite:([^}]+)\}\}", prose)
assert len(keys) >= 5, keys
assert len(set(keys)) >= 2, set(keys)
for heading in ("## Motivating example", "## Worked example", "**Your turn.**", 'title="Answer"'):
    assert heading in prose, heading
assert "## Check yourself {#check-yourself}" in page
hidden = re.findall(r'title="Answer"\}(.*?)\n:+', prose, flags=re.S)
for block in hidden:
    assert "{cite:" not in block

assert "5 units and 3 variables" in prose or "5 units and 3 variables" in page or "15 recorded values" in prose
