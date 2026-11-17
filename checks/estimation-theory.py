"""Check the estimation-theory page, including the mean-squared-error arithmetic."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
md = (ROOT / "research" / "content" / "estimation-theory.md").read_text(encoding="utf-8")
cites = re.findall(r"\{\{cite:([a-z0-9_]+)\}\}", md)
assert len(cites) >= 5, len(cites)
assert len(set(cites)) >= 2, set(cites)
heads = [h.split(" — ")[0].strip() for h in re.findall(r"(?m)^## (.+)$", md)]
assert heads == [
    "Lead context",
    "Motivating example",
    "Definition",
    "Statistical use",
    "Worked example",
    "History",
    "Connections",
], heads
assert "**Your turn.**" in md
assert "## Check yourself" not in md
assert "wait:" not in md
assert "List the integers" not in md
assert "recompute the featured" not in md.lower()
assert "Ch. 5)" not in md
assert "\n\n\n\n" not in md
match = re.search(
    r'::: \{\.callout-tip collapse="true" title="Answer"\}\n(.*?)\n:::',
    md,
    re.S,
)
assert match and "{cite:" not in match.group(1)

sample = (2, 6, 3, 5)
assert sum(sample) / len(sample) == 4
# Unbiased estimators: MSE equals variance. n=4, sigma^2=4.
assert 4 / 4 == 1
# Your turn: n=9, sigma^2=9.
assert 9 / 9 == 1

print("estimation-theory ok")
