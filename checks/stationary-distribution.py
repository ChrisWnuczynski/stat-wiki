"""Verify all numerical examples and generated structure for stationary distribution."""

from fractions import Fraction as F
from pathlib import Path

from sympy import Matrix

root = Path(__file__).resolve().parents[1]
page = (root / "articles/stationary-distribution.qmd").read_text()
body = page.split("## See also", 1)[0]

weather = Matrix([[F(4, 5), F(1, 5)], [F(3, 10), F(7, 10)]])
weather_pi = Matrix([[F(3, 5), F(2, 5)]])
assert weather_pi * weather == weather_pi
assert F(1, 5) * F(3, 5) == F(3, 10) * F(2, 5)
assert F(3, 5) / F(2, 5) == F(3, 2)

inherited = Matrix([[F(7, 10), F(3, 10)], [F(3, 5), F(2, 5)]])
inherited_pi = Matrix([[F(2, 3), F(1, 3)]])
assert inherited_pi * inherited == inherited_pi
assert inherited[0, 0] * inherited_pi[0] + inherited[1, 0] * inherited_pi[1] == inherited_pi[0]

machine = Matrix([[F(1, 2), F(1, 2), 0], [F(1, 4), F(1, 4), F(1, 2)], [0, F(1, 2), F(1, 2)]])
machine_pi = Matrix([[F(1, 5), F(2, 5), F(2, 5)]])
assert all(sum(machine.row(i)) == 1 for i in range(3))
assert machine_pi * machine == machine_pi
assert Matrix([[1, 0, 0]]) * machine**2 == Matrix([[F(3, 8), F(3, 8), F(1, 4)]])
assert F(1, 2) * F(1, 5) == F(1, 4) * F(2, 5)
assert F(1, 2) * F(2, 5) == F(1, 2) * F(2, 5)

practice = Matrix([[F(3, 5), F(2, 5)], [F(1, 5), F(4, 5)]])
practice_pi = Matrix([[F(1, 3), F(2, 3)]])
assert practice_pi * practice == practice_pi

for printed in (
    "(0.6,0.4)", "0.2", "0.3", "1.5", "(2/3,1/3)",
    "0.375", "0.25", "(0.2,0.4,0.4)", "(1/5,2/5,2/5)",
    "(1/3,2/3)", "0.6/3", "1.6/3", "1/(2|E|)",
    "(1/2,1/2)",
):
    assert printed in body, f"missing printed number: {printed}"
assert body.count('title="Proof"') == 1
assert "## Motivating example" in body and "## Worked example" in body
assert "**Your turn.**" in body and 'title="Answer"' in body
assert "## Common misconceptions" in body and "{#assumptions-and-limits}" in body
for key in ("levin_peres2017", "dodge2008"):
    assert f'data-cite-key="{key}"' in body
for qid in ("ex-sp-deterministic-cycle", "ex-sp-path-graph", "ex-sp-closed-classes"):
    question = (root / f"questions/{qid}.qmd").read_text()
    assert "Worked answer" in question
print("stationary distribution numbers and structure passed")
