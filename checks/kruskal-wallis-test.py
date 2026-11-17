"""Check the kruskal-wallis-test article. The script reads the markdown only."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SLUG = "kruskal-wallis-test"
md = (ROOT / "research" / "content" / f"{SLUG}.md").read_text(encoding="utf-8")
cites = re.findall(r"\{\{cite:([a-z0-9_]+)\}\}", md)
assert len(cites) >= 5, len(cites)
assert len(set(cites)) >= 2, set(cites)
heads = [h.split(" — ")[0] for h in re.findall(r"(?m)^## (.+)$", md)]
assert heads == ['Lead context', 'Motivating example', 'Definition', 'Interpretation', 'Worked example', 'Connections', 'History'], heads
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

from fractions import Fraction
ranks = (10, 26, 42)
assert sum(ranks) == 78
assert max(ranks) <= 42
assert 9 + 10 + 11 + 12 == 42
N, n = 12, 4
H = Fraction(12, N * (N + 1)) * sum(Fraction(r * r, n) for r in ranks) - 3 * (N + 1)
assert H == Fraction(128, 13)
assert 13.64 > 7.81

print(SLUG, "ok")
