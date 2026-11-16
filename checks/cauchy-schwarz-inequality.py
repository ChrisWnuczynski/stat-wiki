"""Check Cauchy–Schwarz vector and coin calculations."""

import math
from pathlib import Path

root = Path(__file__).resolve().parents[1]
page = (root / "articles/cauchy-schwarz-inequality.qmd").read_text()
body = page.split("## See also", 1)[0]

assert 12 ** 2 + 15 ** 2 + 16 ** 2 == 625
assert math.sqrt(625) == 25
assert 12 * 0.48 + 15 * 0.60 + 16 * 0.64 == 25
assert abs(4) < 5
assert 1 * 2 + 2 * 4 == 10
assert 5 * 20 == 100
# fair coin
assert (1 / 2) ** 2 == 1 / 4
assert (1 / 4) ** 2 == 1 / 16
assert (1 / 2) * (1 / 2) == 1 / 4
# Y = 1 - X
assert -1 / 4 == 0 - (1 / 2) * (1 / 2)

for printed in (
    "625", "25", "0.48", "0.60", "0.64", "12", "15", "16",
    "1/16", "1/4", "-1/4",
):
    assert printed in body, printed
assert "5" in body and "10" in body
assert body.count('title="Proof"') == 1
assert "**Your turn.**" in body and "## Check yourself" in body
assert body.count('title="Answer"') >= 3
for qid in ("ex-prob-sign-covariance", "ex-inf-poisson-information"):
    assert f"../questions/{qid}.qmd" in page
for key in ("durrett2019", "dodge2008"):
    assert f'data-cite-key="{key}"' in body
print("cauchy-schwarz checks passed")
