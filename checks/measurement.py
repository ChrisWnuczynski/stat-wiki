"""Checks for measurement."""
import json
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
slug = "measurement"
prose = (root / "research/content" / f"{slug}.md").read_text(encoding="utf-8")
works = json.loads((root / "bibliography.json").read_text(encoding="utf-8"))["works"]
keys = re.findall(r"\{\{cite:([^}]+)\}\}", prose)
assert len(keys) >= 5, keys
assert len(set(keys)) >= 2, set(keys)
for key in set(keys):
    assert key in works, key
assert "## Motivating example" in prose
assert "## Worked example" in prose
assert "**Your turn.**" in prose
assert 'collapse="true" title="Answer"' in prose
assert "## Check yourself" not in prose
hidden = re.findall(r'title="Answer"\}(.*?)\n:+', prose, flags=re.S)
assert hidden, "missing answer callout"
for block in hidden:
    assert "{cite:" not in block
assert (10 + 12 + 11 + 11) / 4 == 11
assert 11 - 12 == -1
assert (10 + 12 + 11 + 11 + 16) / 5 == 12
assert 12 - 12 == 0
print(slug, "ok")
