"""Check lasso examples, threshold proof and preserved numerical content."""

from math import isclose
from pathlib import Path

page = (Path(__file__).resolve().parents[1] / "articles/lasso.qmd").read_text()
body = page.split("## See also", 1)[0]

soft = lambda b, lam: (1 if b > 0 else -1 if b < 0 else 0) * max(abs(b) - lam / 2, 0)
b = [1.8, -.4, .9]
assert 1.2 / 2 == .6
assert all(isclose(x, y) for x, y in zip([soft(x, 1.2) for x in b], [1.2, 0, .3]))
assert 1 + 1.2 == 2.2
assert [round(x / 2.2, 4) for x in b] == [.8182, -.1818, .4091]
assert [round(soft(x, 1), 4) for x in [2, -.7, .2]] == [1.5, -.2, 0]
assert 2**30 > 10**9 and 10**30 < 2**100 < 2 * 10**30
old = [3, -1.5, .8, -.3, .1]
assert [round(x / 2, 2) for x in old] == [1.5, -.75, .4, -.15, .05]
assert [round(soft(x, 1), 2) for x in old] == [2.5, -1, .3, 0, 0]
assert [x if abs(x) > 1 else 0 for x in old] == [3, -1.5, 0, 0, 0]
objective = lambda b1, b2: (3 - b1 - b2)**2 + 2 * (abs(b1) + abs(b2))
assert objective(2, 0) == objective(1, 1) == objective(0, 2) == 5
for s in [x / 100 for x in range(-100, 501)]:
    assert (3 - s)**2 + 2 * abs(s) >= 5 - 1e-10
for printed in ("1.8", "0.4", "0.9", "1.2", "0.6", "0.8182", "0.1818", "0.4091", "1.5", "0.2", "2^p", "10^9", "10^{30}", "2.5", "0.75"):
    assert printed in body, printed
for heading in ("## Motivating example", "## Intuition", "## Definition", "## Selection is conditional", "## Properties", "## Statistical use", "## Worked example", "## Common misconceptions", "## When a coefficient list misleads", "## Connections", "## History"):
    assert heading in body, heading
assert body.count('title="Proof"') == 1
assert "**Your turn.**" in body and 'title="Answer"' in body
assert "Main article" in body
for key in ("tibshirani1996", "friedman_glmnet2010", "hastie_esl2009", "james_islr2021"):
    assert f'data-cite-key="{key}"' in body
print("Lasso thresholds, nonuniqueness and preserved examples passed")
