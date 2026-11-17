"""Checks for natural-experiment."""
import json
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
slug = "natural-experiment"
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
assert (30 + 40 + 50 + 40) / 4 == 40
assert (20 + 25 + 30 + 25) / 4 == 25
assert 40 - 25 == 15
assert (20 + 25 + 30 + 25 + 20) / 5 == 24
assert 40 - 24 == 16
assert abs(25.8 - 19.5 - 6.3) < 1e-12
print(slug, "ok")
