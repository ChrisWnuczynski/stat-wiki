"""Check the instrumental-variable article. The script reads the markdown only."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SLUG = "instrumental-variable"
md = (ROOT / "research" / "content" / f"{SLUG}.md").read_text(encoding="utf-8")
cites = re.findall(r"\{\{cite:([a-z0-9_]+)\}\}", md)
assert len(cites) >= 5, len(cites)
assert len(set(cites)) >= 2, set(cites)
heads = [h.split(" — ")[0] for h in re.findall(r"(?m)^## (.+)$", md)]
assert heads == ['Lead context', 'Motivating example', 'Definition', 'Properties', 'Statistical use', 'Worked example', 'Common misconceptions', 'History', 'Connections'], heads
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

assert (11 - 7) / (0.75 - 0.25) == 8
assert (11 - 7) / (0.65 - 0.25) == 10
assert abs(0.2578 - 0.1951 - 0.0627) < 1e-12
assert abs(0.1503 / 0.0627 - 2.4) < 0.01

print(SLUG, "ok")
