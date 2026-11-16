"""Check main-effect table arithmetic and preserved source content."""

import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
page = (root / "articles/main-effect.qmd").read_text()
body = page.split("## See also", 1)[0]
pending = json.loads((root / "research/pending/main-effect.json").read_text())

def effects(a0low, a1low, a0high, a1high):
    low = a1low - a0low
    high = a1high - a0high
    marginal = (a1low + a1high - a0low - a0high) / 2
    return low, high, marginal, high - low

assert effects(8, 14, 18, 12) == (6, -6, 0, -12)  # page uses B vs A sign
assert effects(10, 16, 14, 24) == (6, 10, 8, 4)
assert effects(20, 22, 25, 35) == (2, 10, 6, 8)
assert (10 + 14) / 2 == 12 and (16 + 24) / 2 == 20
assert (20 + 25) / 2 == 22.5 and (22 + 35) / 2 == 28.5
for printed in ("$8$ and $14$", "$18$ and $12$", "$10$ and $16$", "$14$ and $24$", "$22.5$", "$28.5$"):
    assert printed in body, printed
assert body.count('title="Proof"') == 1
assert "## Motivating example" in body and "## Worked example" in body
assert "**Your turn.**" in body and 'title="Answer"' in body
assert pending["self_checks"] == ["ex-inf-contrast-cell", "ex-inf-interaction-ss"]
for q in pending["self_checks"]:
    assert "## Worked answer" in (root / "questions" / f"{q}.qmd").read_text()
for key in ("nist_two_way_anova2002", "nist_interactions2002", "dodge2008"):
    assert f'data-cite-key="{key}"' in body
assert json.loads((root / "research/baseline.json").read_text())["main-effect"]["figures"] == 0
print("main-effect arithmetic, proof and sources passed")
