"""Check the likelihood-ratios-in-diagnostic-testing article. The script reads the markdown only."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SLUG = "likelihood-ratios-in-diagnostic-testing"
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

lr = 0.89 / 0.07
prior = 0.0035 / 0.9965
post_odds = lr * prior
post = post_odds / (1 + post_odds)
assert abs(lr - 12.7142857) < 1e-6
assert abs(post - 0.042747) < 1e-5
assert abs((0.80 / 0.10) * (0.20 / 0.80) - 2) < 1e-12
assert abs(2 / 3 - 0.6666666667) < 1e-9
assert abs(0.70 / 0.02 - 35) < 1e-12

print(SLUG, "ok")
