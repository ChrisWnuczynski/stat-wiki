"""Check the test-statistic article. The script reads the markdown only."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SLUG = "test-statistic"
md = (ROOT / "research" / "content" / f"{SLUG}.md").read_text(encoding="utf-8")
cites = re.findall(r"\{\{cite:([a-z0-9_]+)\}\}", md)
assert len(cites) >= 5, len(cites)
assert len(set(cites)) >= 2, set(cites)
heads = [h.split(" — ")[0] for h in re.findall(r"(?m)^## (.+)$", md)]
assert heads == ['Lead context', 'Motivating example', 'Intuition', 'Definition', 'Statistical use', 'Worked example', 'Common misconceptions', 'Connections'], heads
for line in md.splitlines():
    assert line == line.rstrip(" \t"), repr(line)
assert md.endswith("\n") and not md.endswith("\n\n")
low = md.lower()
for phrase in (
    "not a claim",
    "not claimed",
    "this page",
    "dodge states",
    "the manual",
    "question bank",
    "letter opener",
    "wikipedia",
    "grokipedia",
    "hansen2010",
):
    assert phrase not in low, phrase
assert "**Your turn.**" in md
assert "## Check yourself" not in md
match = re.search(
    r'::: \{\.callout-tip collapse="true" title="Answer"\}\n(.*?)\n:::',
    md,
    re.S,
)
assert match, "missing answer callout"
assert "{cite:" not in match.group(1)

import math
se = math.sqrt(0.25 / 1028)
assert abs(se - 0.0156) < 5e-5
assert abs((0.56 - 0.50) / 0.0156 - 3.85) < 0.01
assert abs(math.sqrt(0.25 / 100) - 0.05) < 1e-12
assert abs((0.60 - 0.50) / 0.05 - 2) < 1e-12
assert 1028 * 0.5 == 514

print(SLUG, "ok")
