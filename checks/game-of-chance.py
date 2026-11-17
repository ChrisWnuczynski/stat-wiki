"""Check the game-of-chance article. The script reads the markdown only."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SLUG = "game-of-chance"
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

from fractions import Fraction
euro = Fraction(-3, 6) + Fraction(1, 1) * Fraction(3, 6) + Fraction(2, 1) * Fraction(2, 6)
assert euro == Fraction(2, 3)
assert sum(range(1, 7)) == 21
assert Fraction(21, 6) == Fraction(7, 2)
assert Fraction(4, 6) == Fraction(2, 3)
coin = Fraction(1, 2) * 3 + Fraction(1, 2) * (-1)
assert coin == 1
assert coin + euro == Fraction(5, 3)
wheel = Fraction(4, 4) + Fraction(-2, 4)
assert wheel == Fraction(1, 2)

print(SLUG, "ok")
