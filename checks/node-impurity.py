"""Check node-impurity algebra, split arithmetic and baseline preservation."""

import json
import math
from pathlib import Path

root = Path(__file__).resolve().parents[1]
page = (root / "articles/node-impurity.qmd").read_text()
body = page.split("## See also", 1)[0]
pending = json.loads((root / "research/pending/node-impurity.json").read_text())


def scores(probs):
    gini = 1 - sum(p * p for p in probs)
    entropy = -sum(p * math.log(p) for p in probs if p)
    error = 1 - max(probs)
    return gini, entropy, error


parent = scores([0.8, 0.2])
left, right = scores([0.7, 0.3]), scores([0.9, 0.1])
assert round(parent[0], 2) == 0.32 and round(parent[1], 3) == 0.500
assert round(parent[2], 2) == 0.20
assert round((left[0] + right[0]) / 2, 2) == 0.30
assert round((left[1] + right[1]) / 2, 3) == 0.468
assert round((left[2] + right[2]) / 2, 2) == 0.20
assert round(parent[0] - (left[0] + right[0]) / 2, 2) == 0.02
assert round(parent[1] - (left[1] + right[1]) / 2, 3) == 0.032
new_parent, new_left, new_right = scores([0.6, 0.4]), scores([0.8, 0.2]), scores([0.4, 0.6])
assert round(new_parent[0], 2) == 0.48
assert round((new_left[0] + new_right[0]) / 2, 2) == 0.40
assert round(new_parent[0] - (new_left[0] + new_right[0]) / 2, 2) == 0.08
alt_left, alt_right = scores([1, 0]), scores([0.2, 0.8])
assert (alt_left[0], round(alt_right[0], 2)) == (0, 0.32)
assert round((alt_left[0] + alt_right[0]) / 2, 2) == 0.16
assert round(new_parent[0] - (alt_left[0] + alt_right[0]) / 2, 2) == 0.32
assert round(math.log(2), 4) == 0.6931
assert all(scores([p, 1-p])[0] <= 0.5 for p in [0, 0.1, 0.5, 0.9, 1])
for printed in ("80", "20", "0.32", "0.500", "0.20", "0.30", "0.468", "0.02", "0.032", "0.6931", "12", "8", "0.6", "0.4", "0.48", "0.40", "0.08", "0.16"):
    assert printed in body, printed
assert body.count('title="Proof"') == 1
assert "## Motivating example" in body and "## Worked example" in body
assert "**Your turn.**" in body and 'title="Answer"' in body
assert page.count("![") >= json.loads((root / "research/baseline.json").read_text())["node-impurity"]["figures"]
assert "ex-sl-12-2.qmd" in page and "ex-sl-12-5.qmd" in page
for key in ("rpart_longintro2023", "sklearn_tree2026", "dodge2008"):
    assert f'data-cite-key="{key}"' in body, key
assert any(f'data-cite-key="{key}"' in body for key in ("breiman_cart1984", "stanford_cs229_trees2018"))
assert pending["self_checks"] == ["ex-sl-12-2", "ex-sl-12-5"]
for slug in pending["self_checks"]:
    assert "## Worked answer" in (root / "questions" / f"{slug}.qmd").read_text()
print("node impurity arithmetic and preservation passed")
