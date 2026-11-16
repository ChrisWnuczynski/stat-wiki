"""Check marginal and conditional probability contrasts."""

import math
from pathlib import Path

root = Path(__file__).resolve().parents[1]
page = (root / "articles/marginal-and-conditional-effects.qmd").read_text()
body = page.split("## See also", 1)[0]

def expit(z):
    return 1 / (1 + math.exp(-z))

assert round(expit(1), 4) == 0.7311
assert round(expit(-1), 4) == 0.2689
assert round(expit(2), 4) == 0.8808
assert round(expit(0), 4) == 0.5000
m0 = (expit(1) + expit(-1)) / 2
m1 = (expit(2) + expit(0)) / 2
assert round(m0, 4) == 0.5000
assert round(m1, 4) == 0.6904
assert round(m1 - m0, 4) == 0.1904
assert round(expit(1) - expit(0), 4) == 0.2311
assert round(expit(2) - expit(1), 4) == 0.1497
assert round((0.2311 + 0.1497) / 2, 4) == 0.1904
assert abs((min(0.2, 0.8) - 0.2 * 0.8) / (math.sqrt(0.2 * 0.8) ** 2) - 0.25) < 1e-12

for printed in (
    "0.7311", "0.2689", "0.8808", "0.6904", "0.1904", "0.2311",
    "0.1497", "0.25", "0.04", "0.16", "0.5000",
):
    assert printed in body, printed
assert body.count('title="Proof"') == 1
assert "**Your turn.**" in body and "## Check yourself" in body
assert body.count('title="Answer"') >= 3
for qid in ("c-37", "c-38"):
    assert f"../questions/{qid}.qmd" in page
print("marginal and conditional effects checks passed")
