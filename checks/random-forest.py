"""Printed values for the random-forest article."""

from pathlib import Path

root = Path(__file__).resolve().parents[1]
page = (root / "articles" / "random-forest.qmd").read_text(encoding="utf-8")
body = page.split("## See also", 1)[0]

def var_avg(rho, sigma2, B):
    return rho * sigma2 + (1 - rho) * sigma2 / B

assert abs(var_avg(0.2, 4, 100) - 0.832) < 1e-12
assert 4 / 100 == 0.04
assert abs(0.8 / 0.04 - 20) < 1e-12
assert abs(var_avg(0.2, 4, 200) - 0.816) < 1e-12
assert abs(var_avg(0.5, 1, 50) - 0.51) < 1e-12
assert 1 / 50 == 0.02

for printed in ("0.832", "0.04", "0.8", "0.032", "0.816", "0.51", "0.02", "0.2", "100"):
    assert printed in body, printed
assert body.count('title="Proof"') == 1
assert "**Your turn.**" in body
assert body.count('collapse="true" title="Answer"') == 3
assert "## Check yourself" in body
print("random forest checks passed")
