"""Check the raw-data article against its pending file."""
import json
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
self_checks = json.loads((root / "research/self-checks.json").read_text(encoding="utf-8")).get("raw-data", [])
prose = (root / "research/content/raw-data.md").read_text(encoding="utf-8")
keys = re.findall(r"{{cite:([^}]+)}}", prose)
assert len(keys) >= 5, keys
assert len(set(keys)) >= 2, set(keys)
assert "**Your turn.**" in prose
assert 'collapse="true" title="Answer"' in prose
hidden = re.findall(r'title="Answer"\}(.*?)\n:+', prose, flags=re.S)
assert hidden, "missing answer callout"
for block in hidden:
    assert "{cite:" not in block
checks = self_checks
assert 2 <= len(checks) <= 3
for item in checks:
    assert "{cite:" not in item["answer"]
assert (8+11+9+10+12)/5 == 10
assert (8+11+9+10+12+16)/6 == 11
