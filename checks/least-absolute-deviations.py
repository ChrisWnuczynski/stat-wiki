"""Check the least-absolute-deviations article. The script reads the markdown only."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SLUG = "least-absolute-deviations"
md = (ROOT / "research" / "content" / f"{SLUG}.md").read_text(encoding="utf-8")
cites = re.findall(r"\{\{cite:([a-z0-9_]+)\}\}", md)
assert len(cites) >= 5, len(cites)
assert len(set(cites)) >= 2, set(cites)
heads = [h.split(" — ")[0] for h in re.findall(r"(?m)^## (.+)$", md)]
assert heads == ['Lead context', 'Motivating example', 'Definition', 'Properties', 'Worked example', 'Assumptions and limits', 'History'], heads
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

assert abs(0) + abs(1.5) + abs(0) == 1.5
assert abs(0) + abs(0) + abs(3) == 3
assert abs(1 - 1) + abs(1 - 1) + abs(5 - 1) == 4
assert abs(1 - 1) + abs(1 - 3) + abs(5 - 5) == 2
assert 2 < 4
assert "hansen2010" not in md

print(SLUG, "ok")
