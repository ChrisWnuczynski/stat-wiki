"""Verify sigmoid arithmetic and the generated concept page."""

import math
from pathlib import Path


root = Path(__file__).resolve().parents[1]
page = (root / "articles/sigmoid-function.qmd").read_text()
body = page.split("## See also", 1)[0]


def sigmoid(z):
    return 1 / (1 + math.exp(-z))


def derivative(z):
    p = sigmoid(z)
    return p * (1 - p)


assert sigmoid(0) == .5 and derivative(0) == .25
assert math.isclose(sigmoid(2), .8807970779778823)
assert round(sigmoid(2), 3) == .881
assert round(derivative(2), 3) == .105
assert math.isclose(sigmoid(-2), 1 - sigmoid(2))
assert round(sigmoid(-1), 6) == .268941
assert round(sigmoid(1), 6) == .731059
assert round(derivative(-1), 6) == .196612
assert round(derivative(1), 6) == .196612
assert round(math.exp(2), 3) == 7.389
assert round(math.exp(2), 6) == 7.389056
o = sigmoid(-1)
assert round(o - 1, 6) == -.731059
assert round((o - 1) * derivative(-1), 6) == -.143735
assert sigmoid(math.log(3)) == .75
assert derivative(math.log(3)) == .1875
assert (sigmoid(math.log(3)) - 1) * derivative(math.log(3)) == -.046875
for z, output, grad in ((-8, .000335, -.000670), (-1, .2689, -.2874)):
    p = sigmoid(z)
    assert abs(p - output) < .00005
    assert abs(-2 * (1 - p) * p * (1 - p) - grad) < .0001
assert round(sigmoid(-8) - 1, 6) == -.999665
assert abs(abs((-2 * (1 - sigmoid(-1)) * derivative(-1)) /
               (-2 * (1 - sigmoid(-8)) * derivative(-8))) - 430) < 2

for printed in (
    "$0.269$", "$0.731$", "$e^2\\approx7.389$", "$1/4$",
    "$z=2$", "0.881", "0.105", "0.268941", "0.731059",
    "$0.196612$", "7.389056", "-0.731059", "-0.143735",
    "3/4=0.75", "3/16=0.1875", "-1/4=-0.25",
    "-3/64=-0.046875", "$z=-8$", "0.000335",
    "$-0.000670$", "$-0.999665$", "$0.9$",
):
    assert printed in body, f"Missing displayed number {printed}"

assert body.count('title="Proof"') == 1
assert "## Motivating example" in body and "## Worked example" in body
assert "**Your turn.**" in body and "## Check yourself" in body
assert body.count('title="Answer"') >= 3
for qid in ("ex-sl-15-6", "ex-sl-15-7"):
    assert f"../questions/{qid}.qmd" in page
for key in ("bishop2006", "mcculloch_pitts1943",
            "rumelhart_hinton_williams1986"):
    assert f'data-cite-key="{key}"' in body
print("sigmoid arithmetic, proof, practice and cited history passed")
