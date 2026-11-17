"""Check the kurtosis article. The script reads the markdown only."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SLUG = "kurtosis"
md = (ROOT / "research" / "content" / f"{SLUG}.md").read_text(encoding="utf-8")
cites = re.findall(r"\{\{cite:([a-z0-9_]+)\}\}", md)
assert len(cites) >= 5, len(cites)
assert len(set(cites)) >= 2, set(cites)
heads = [h.split(" — ")[0] for h in re.findall(r"(?m)^## (.+)$", md)]
assert heads == ['Lead context', 'Motivating example', 'Intuition', 'Definition', 'Properties', 'Worked example', 'Assumptions and limits', 'Connections'], heads
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

def moments(v):
    n = len(v)
    m = sum(v) / n
    m2 = sum((x - m) ** 2 for x in v) / n
    m4 = sum((x - m) ** 4 for x in v) / n
    return m2, m4, m4 / m2 ** 2
assert moments([1, 2, 3, 4, 5]) == (2, 6.8, 1.7)
assert moments([1, 1, 1, 1, 6])[2] == 3.25
m2, m4, k = moments([0, 0, 0, 0, 0, 6])
assert m2 == 5 and m4 == 105 and k == 4.2
assert "1.7" in md and "3.25" in md and "4.2" in md
assert "2.96" in md and "5.9" in md and "6,693" in md
assert 4 ** 4 == 256

print(SLUG, "ok")
