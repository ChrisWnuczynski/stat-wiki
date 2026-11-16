"""Validate linear mixed-model covariance examples and preserved structure."""

from math import isclose
from pathlib import Path

page = (Path(__file__).resolve().parents[1] / "articles/linear-mixed-model.qmd").read_text()
body = page.split("## See also", 1)[0]

assert 10 + 2 * 1 == 12
assert 9 + 4 == 13
assert isclose(9 / 13, .6923, abs_tol=.00005)
assert 4 + 4 == 8
assert 13 + 13 == 26
assert 4 + 6 == 10
assert 4 / 10 == .4
assert 6 + 6 == 12

for printed in ("10+2t", "9+4=13", "9/13", "0.6923", "4+4=8", "13+13=26", "4+6=10", "4/10=0.4", "6+6=12"):
    assert printed in body, printed
for heading in ("## Motivating example", "## Intuition", "## Definition", "## Dependence made explicit", "## Properties", "## Statistical use", "## Worked example", "## Common misconceptions", "## Assumptions and limits", "## Connections", "## History"):
    assert heading in body, heading
assert body.count('title="Proof"') == 1
assert "**Your turn.**" in body and 'title="Answer"' in body
assert "Main article" in body
for key in ("bates_lme4_2015",):
    assert f'data-cite-key="{key}"' in body
assert "§1.1" in body
print("Linear mixed-model covariance and preserved content passed")
