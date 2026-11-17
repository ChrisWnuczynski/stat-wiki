"""Validate activation values, derivatives, and preserved content."""

from math import exp, isclose
from pathlib import Path

page = (Path(__file__).resolve().parents[1] / "articles/activation-function.qmd").read_text()
body = page.split("## See also", 1)[0]
sigmoid = lambda z: 1 / (1 + exp(-z))
derivative = lambda z: sigmoid(z) * (1 - sigmoid(z))

for z, output, slope in ((2, .8808, .1050), (0, .5, .25), (1, .7311, .1966), (-1, .2689, .1966), (-2, .1192, .1050)):
    assert round(sigmoid(z), 4) == output
    assert round(derivative(z), 4) == slope
assert isclose(derivative(20), 2.0611536e-9, rel_tol=1e-7)
assert max(0, -2) == 0 and max(0, 1) == 1
assert 2 * 1 - 1 == 1 and 2 * 0 - 1 == -1
for printed in ("0.8808", "0.1050", "0.7311", "0.2689", "0.1966", "0.1192", "2.06\\times10^{-9}", "1/4", "2x-1"):
    assert printed in body, printed
for heading in ("## Motivating example", "## Intuition", "## Definition", "## Shape and gradients", "## Properties", "## Statistical use", "## Worked example", "## Common misconceptions", "## Assumptions and limits", "## Connections", "## History"):
    assert heading in body, heading
assert body.count('title="Proof"') == 1
assert "**Your turn.**" in body and 'title="Answer"' in body
for key in ("mcculloch_pitts1943", "rumelhart_hinton_williams1986", "bishop2006", "goodfellow_bengio_courville2016", "glorot_bordes_bengio2011"):
    assert f'data-cite-key="{key}"' in body
print("Activation examples, derivatives and inherited content passed")
