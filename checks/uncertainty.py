"""Check the uncertainty article against its pending file."""
import json
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
self_checks = json.loads((root / "research/self-checks.json").read_text(encoding="utf-8")).get("uncertainty", [])
prose = (root / "research/content/uncertainty.md").read_text(encoding="utf-8")
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
vals=[5,7,6,6]
assert sum(vals)/4 == 6
assert sum(abs(v-6) for v in vals)/4 == 0.5
vals2=[5,7,6,6,8]
mean=sum(vals2)/5
assert mean == 6.4
assert abs(sum(abs(v-mean) for v in vals2)/5 - 0.88) < 1e-9
