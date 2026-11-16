"""Check hidden-layer XOR, smooth example and generated practice."""

import math
from pathlib import Path


root = Path(__file__).resolve().parents[1]
page = (root / "articles/hidden-layer.qmd").read_text()
body = page.split("## See also", 1)[0]


def threshold(net):
    return int(net >= 0)


for x1, x2 in ((0, 0), (0, 1), (1, 0), (1, 1)):
    target = x1 ^ x2
    # The inherited three-unit copy-and-AND representation.
    h3, h4, h5 = x1, x1 & x2, x2
    assert threshold(h3 - 2 * h4 + h5 - .5) == target
    # The inherited two-unit OR-minus-AND representation.
    a = threshold(2 * x1 + 2 * x2 - 3)
    b = threshold(2 * x1 + 2 * x2 - 1)
    assert threshold(-2 * a + 2 * b - 1) == target
    # The answered bank question uses OR and NAND, then their AND.
    or_unit = threshold(x1 + x2 - .5)
    nand_unit = threshold(-x1 - x2 + 1.5)
    assert threshold(or_unit + nand_unit - 1.5) == target

assert (2 + 1) * 3 + (3 + 1) * 1 == 13


def sigmoid(z):
    return 1 / (1 + math.exp(-z))


def smooth_network(x):
    h1 = sigmoid(10 * (x - .25))
    h2 = sigmoid(10 * (x - .75))
    score = 10 * (h1 - h2 - .5)
    return h1, h2, score, sigmoid(score)


assert [round(v, 6) for v in smooth_network(0)] == [
    .075858, .000553, -4.246946, .014106]
assert [round(v, 6) for v in smooth_network(.5)] == [
    .924142, .075858, 3.482836, .970195]
assert [round(v, 6) for v in smooth_network(1)] == [
    .999447, .924142, -4.246946, .014106]
assert math.isclose(smooth_network(0)[3], smooth_network(1)[3])

# The second example has an exact triangular response.
def rectified_network(x):
    return max(0, x) - 2 * max(0, x - 1) + max(0, x - 2)


assert [rectified_network(x) for x in (0, 1, 2, 3)] == [0, 1, 0, 0]
assert rectified_network(.5) == .5 and rectified_network(1.5) == .5

# Corrected initial-weights question: 25 input coordinates plus bias, with
# augmented squared norm 26, matches the answer's variance and tail.
assert round(26**-.5, 3) == .196
assert 26 * .5**2 == 6.5
assert round(math.sqrt(6.5), 2) == 2.55
z = 2 / math.sqrt(6.5)
assert round(z, 3) == .784
assert round(math.erfc(z / math.sqrt(2)), 2) == .43
assert round(sigmoid(2) * (1 - sigmoid(2)), 3) == .105

for printed in (
    "(p+1)l+(l+1)m", "3\\times3+4=13", "$24$",
    "$0.075858$", "0.000553", "$-4.246946$", "0.014106",
    "$0.924142$", "$3.482836$", "0.970195",
    "0.999447", "$0.075305$", "$26$", "0.196",
    "6.5", "$2.55$", "0.784", "0.43",
):
    assert printed in body, f"Missing displayed number {printed}"

assert body.count('title="Proof"') == 1
assert "## Motivating example" in body and "## Worked example" in body
assert "## Interpretation" in body and "### Another feature map" in body
assert "**Your turn.**" in body and "## Check yourself" in body
assert body.count('title="Answer"') >= 3
assert "Two threshold solutions for XOR" in body
for qid in ("ex-sl-14-7", "ex-sl-16-1"):
    assert f"../questions/{qid}.qmd" in page
for key in ("bishop2006", "rumelhart_hinton_williams1986"):
    assert f'data-cite-key="{key}"' in body
print("hidden-layer XOR, smooth example and practice passed")
