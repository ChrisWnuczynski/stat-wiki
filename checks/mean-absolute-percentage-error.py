"""Checks for mean-absolute-percentage-error."""
import json
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
slug = "mean-absolute-percentage-error"
text = (root / "research/content" / f"{slug}.md").read_text(encoding="utf-8")
works = json.loads((root / "bibliography.json").read_text(encoding="utf-8"))["works"]
cites = re.findall(r"\{\{cite:([a-z0-9_]+)\}\}", text)
assert len(cites) >= 5, len(cites)
assert len(set(cites)) >= 2
assert "makridakis_spiliotis_assimakopoulos2018" in set(cites)
for key in set(cites):
    if key != "makridakis_spiliotis_assimakopoulos2018":
        assert key in works, key
heads = re.findall(r"^## (.+)$", text, re.M)
assert heads == [
    "Lead context",
    "Motivating example",
    "Intuition",
    "Definition",
    "Properties",
    "Worked example",
    "Assumptions and limits",
    "Connections",
]
assert "**Your turn.**" in text
assert '::: {.callout-tip collapse="true" title="Answer"}' in text
answer = text.split('title="Answer"}', 1)[1].split(":::", 1)[0]
assert "{cite:" not in answer
assert "## Check yourself" not in text
errs = [abs(100 - 110) / 100, abs(200 - 160) / 200, abs(50 - 80) / 50]
assert errs == [0.1, 0.2, 0.6]
assert sum(100 * e for e in errs) / 3 == 30
assert (10 + 40 + 30) / 3 == 80 / 3
assert abs(100 * 20 / 80 - 25) < 1e-12
assert abs(100 * 30 / 120 - 25) < 1e-12
for printed in ("3.17", "8.28", "14.18", "14.58", "5.67", "6.99", "16.24", "30"):
    assert printed in text, printed
print(slug, "ok")
