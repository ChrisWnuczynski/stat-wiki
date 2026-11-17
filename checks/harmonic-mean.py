"""Check the harmonic-mean article. The script reads the markdown only."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SLUG = "harmonic-mean"
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

from fractions import Fraction as F
assert F(3) / (F(1, 5) + F(1, 10) + F(1, 15)) == F(90, 11)
assert (5 + 10 + 15) / 3 == 10
assert F(3) / (F(1, 100) + F(1, 200) + F(1, 300)) == F(1800, 11)
assert round(1800 / 11) == 164
assert abs(36 / 11 - 3.272727) < 1e-6
assert abs(31 / 6 - 5.166666) < 1e-6
recs = [1, F(1, 2), F(1, 3), F(1, 4), F(1, 5), F(1, 100)]
H = 6 / sum(recs)
assert round(float(H), 2) == 2.62
assert round(115 / 6, 2) == 19.17
assert "90/11" in md or "90}{11" in md or r"\frac{90}{11}" in md
assert "8.1818" in md
assert "164" in md

print(SLUG, "ok")
