"""Check the measurement article against its pending file."""
import json
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
prose = (root / "research/content/measurement.md").read_text(encoding="utf-8")
pending = json.loads((root / "research/pending/measurement.json").read_text(encoding="utf-8"))
keys = re.findall(r"{{cite:([^}]+)}}", prose)
assert len(keys) >= 5, keys
assert len(set(keys)) >= 2, set(keys)
assert "## Motivating example" in prose
assert "## Worked example" in prose
assert "**Your turn.**" in prose
assert 'collapse="true" title="Answer"' in prose
assert "## Check yourself" not in prose
hidden = re.findall(r'title="Answer"\}(.*?)\n:+', prose, flags=re.S)
assert hidden, "missing answer callout"
for block in hidden:
    assert "{cite:" not in block
checks = pending["self_checks"]
assert 2 <= len(checks) <= 3
for item in checks:
    assert "{cite:" not in item["answer"]
assert (10+12+11+11)/4 == 11
assert 11-12 == -1
assert (10+12+11+11+16)/5 == 12
assert 12-12 == 0

