"""Check unit activations, derivatives and retained logic-gate examples."""

from math import exp, isclose
from pathlib import Path

root = Path(__file__).resolve().parents[1]
page = (root / "articles/artificial-neuron.qmd").read_text()
body = page.split("## See also", 1)[0]

sigmoid = lambda z: 1 / (1 + exp(-z))
relu = lambda z: max(0, z)
threshold = lambda z: int(z >= 0)

and_nets = [-1.5, -.5, -.5, .5]
assert [threshold(z) for z in and_nets] == [0, 0, 0, 1]
assert [round(sigmoid(z), 3) for z in and_nets] == [.182, .378, .378, .622]
assert isclose(sigmoid(0) * (1 - sigmoid(0)), .25)

z = .25 + .5 * 2 - 1 * 1
assert z == .25 and threshold(z) == 1 and relu(z) == .25
assert round(sigmoid(z), 6) == .562177
assert round(sigmoid(z) * (1 - sigmoid(z)), 6) == .246134
z_negative = .25 + .5 * 0 - 1 * 1
assert z_negative == -.75 and threshold(z_negative) == relu(z_negative) == 0
assert round(sigmoid(z_negative), 6) == .320821

turn_z = .5 + 1 * 3 - 2 * 1
assert turn_z == 1.5 and threshold(turn_z) == 1 and relu(turn_z) == 1.5
assert round(sigmoid(turn_z), 6) == .817574
assert round(sigmoid(turn_z) * (1 - sigmoid(turn_z)), 6) == .149146
assert relu(.5 + 1 * 0 - 2 * 1) == 0

for fragment in (
    "## Motivating example", "## Worked example", "**Your turn.**",
    'title="Proof"', 'title="Answer"', "0.562177", "0.246134",
    "0.320821", "0.817574", "0.149146", "## Common misconceptions",
    "#assumptions-and-limits",
):
    assert fragment in body, f"Missing section or calculation: {fragment}"
assert body.count('title="Proof"') == 1
for qid in ("ex-sl-14-2", "ex-sl-14-3", "ex-sl-14-5", "ex-sl-14-7"):
    assert f"../questions/{qid}.qmd" in page
print("artificial-neuron activation and gate calculations passed")
