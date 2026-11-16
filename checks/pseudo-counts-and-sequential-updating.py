"""Check all numeric examples and retained material on the pseudo-count page."""

import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
page = (root / "articles/pseudo-counts-and-sequential-updating.qmd").read_text()
body = page.split("## See also", 1)[0]
pending = json.loads((root / "research/pending/pseudo-counts-and-sequential-updating.json").read_text())

def update(a, b, x, n):
    return a + x, b + n - x

assert update(2, 3, 3, 5) == (5, 5)
assert update(5, 5, 4, 5) == update(2, 3, 7, 10) == (9, 6)
assert (2 / 5, 5 / 10, 9 / 15, 7 / 10) == (.4, .5, .6, .7)
assert round(8 / 13, 4) == .6154
assert update(1, 1, 2, 4) == (3, 3)
assert update(3, 3, 3, 5) == update(1, 1, 5, 9) == (6, 5)
assert round(6 / 11, 4) == .5455 and round(5 / 9, 4) == .5556
for printed in ("0.4", "0.5", "0.6", "0.7", "0.6154", "0.5455", "0.5556", "8/13", "6/11", "5/9"):
    assert printed in body, printed
assert "Beta}(5,5)" in body and "Beta}(1,1)" in body
assert body.count('title="Proof"') == 1
assert "## Motivating example" in body and "## Worked example" in body
assert "**Your turn.**" in body and 'title="Answer"' in body
assert pending["self_checks"] == ["ex-ur-posterior-mean", "ex-geom-beta"]
for q in pending["self_checks"]:
    assert (root / "questions" / f"{q}.qmd").exists()
for q in ("ex-ur-posterior-mean", "ex-applied-geometric", "ex-geom-beta", "ex-mammal-ig"):
    assert f"../questions/{q}.qmd" in page
for source in ("diaconis_ylvisaker1979", "dodge2008"):
    assert f'data-cite-key="{source}"' in body
assert json.loads((root / "research/baseline.json").read_text())["pseudo-counts-and-sequential-updating"]["figures"] == 0
print("pseudo-count update, retained content and practice passed")
