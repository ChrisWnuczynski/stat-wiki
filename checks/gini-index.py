"""Printed values for the Gini index article."""

from math import log
from pathlib import Path

root = Path(__file__).resolve().parents[1]
page = (root / "articles" / "gini-index.qmd").read_text(encoding="utf-8")
body = page.split("## See also", 1)[0]

ps = [0.6, 0.2, 0.2]
gini = sum(p * (1 - p) for p in ps)
assert abs(gini - (1 - sum(p * p for p in ps))) < 1e-12
assert abs(gini - 0.56) < 1e-12
assert abs((1 - 0.6) - 0.4) < 1e-12
entropy = -(0.6 * log(0.6) + 2 * 0.2 * log(0.2))
assert round(entropy, 4) == 0.9503
assert abs(2 * 0.8 * 0.2 - 0.32) < 1e-12
assert abs(2 * 0.5 * 0.5 - 0.5) < 1e-12

for printed in ("0.56", "0.4", "0.9503", "0.32", "0.2", "0.44"):
    assert printed in body, printed
assert body.count('title="Proof"') == 1
assert "**Your turn.**" in body
assert body.count('collapse="true" title="Answer"') == 3
assert "## Check yourself" in body
print("gini index checks passed")
