"""Check the foundations-of-statistics article. The script reads the markdown only."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SLUG = "foundations-of-statistics"
md = (ROOT / "research" / "content" / f"{SLUG}.md").read_text(encoding="utf-8")
cites = re.findall(r"\{\{cite:([a-z0-9_]+)\}\}", md)
assert len(cites) >= 5, len(cites)
assert len(set(cites)) >= 2, set(cites)
heads = [h.split(" — ")[0] for h in re.findall(r"(?m)^## (.+)$", md)]
assert heads == ['Lead context', 'Definition', 'Interpretation', 'Statistical use', 'History', 'Connections'], heads
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
assert "**Your turn.**" not in md
assert "## Check yourself" not in md
words = re.findall(r"[A-Za-z0-9']+", md)
assert len(words) >= 1000, len(words)

from fractions import Fraction
assert Fraction(894, 1000) - Fraction(88, 100) == Fraction(14, 1000)
assert abs(0.880 - 0.88) < 1e-12
assert abs(0.010 - 0.01) < 1e-12

print(SLUG, "ok")
