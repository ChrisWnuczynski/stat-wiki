"""Verify loaded-die probabilities and preserved probability properties."""

import json
from fractions import Fraction as F
from pathlib import Path

root = Path(__file__).resolve().parents[1]
page = (root / "articles/probability-measure.qmd").read_text()
body = page.split("## See also", 1)[0]
pending = json.loads((root / "research/pending/probability-measure.json").read_text())

p = {1: F(1, 12), 2: F(1, 12), 3: F(1, 6), 4: F(1, 6), 5: F(1, 4), 6: F(1, 4)}
P = lambda a: sum((p[i] for i in a), F(0))
assert P(p) == 1
even, high = {2, 4, 6}, {4, 5, 6}
assert (P(even), P(high), P(even & high), P(even | high)) == (F(1, 2), F(2, 3), F(5, 12), F(3, 4))
assert P(even) + P(high) - P(even & high) == P(even | high)
odd, low = {1, 3, 5}, {1, 2, 3}
assert (P(odd), P(low), P(odd & low), P(odd | low)) == (F(1, 2), F(1, 3), F(1, 4), F(7, 12))
assert F(1, 10) + F(2, 10) != F(6, 10)
for printed in ("1/12", "1/6", "1/4", "1/2", "2/3", "5/12", "3/4", "1/3", "7/12", "0.1", "0.2", "0.6"):
    assert printed in body, printed
assert page.count("![") >= 1
assert body.count('title="Proof"') == 1
assert "## Motivating example" in body and "## Worked example" in body
assert "**Your turn.**" in body and 'title="Answer"' in body
assert pending["self_checks"] == ["ex-prob-three-toss-weights", "ex-prob-intersection-bound"]
for q in pending["self_checks"]:
    assert "## Worked answer" in (root / "questions" / f"{q}.qmd").read_text()
for key in ("durrett2019", "dodge2008", "kolmogorov1933_slln"):
    assert f'data-cite-key="{key}"' in body
assert json.loads((root / "research/baseline.json").read_text())["probability-measure"]["figures"] == 1
print("probability-measure arithmetic and preservation passed")
