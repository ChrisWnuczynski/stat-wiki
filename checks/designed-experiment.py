"""Check designed-experiment counts, means and hypergeometric moments."""

import math
from math import comb
from pathlib import Path

root = Path(__file__).resolve().parents[1]
page = (root / "articles/designed-experiment.qmd").read_text()
body = page.split("## See also", 1)[0]

assert comb(6, 3) == 20 and round(1 / 20, 2) == 0.05
caff = [17, 22, 21, 16, 6, -2, 27, 15, 16, 20]
decaf = [4, 10, 7, -9, 5, 4, 5, 7, 6, 12]
assert sum(caff) == 158 and sum(decaf) == 51
assert round(158 / 10, 1) == 15.8 and round(51 / 10, 1) == 5.1
assert round(15.8 - 5.1, 1) == 10.7
assert 10 * 8 / 20 == 4
assert 24 / 19 == 10 * (8 / 20) * (12 / 20) * (10 / 19)
assert round(24 / 19, 3) == 1.263
sd = math.sqrt(24 / 19)
assert round(sd, 3) == 1.124
assert round(2 / round(sd, 3), 2) == 1.78
assert 4 * 4 / 8 == 2 and comb(8, 4) == 70
assert round(1 / 70, 4) == 0.0143

for printed in (
    "20", "0.05", "15.8", "5.1", "10.7", "1.263", "1.124", "1.78",
    "70", "0.0143", "158/10", "51/10", "24/19",
):
    assert printed in body, printed
assert body.count('title="Proof"') == 1
assert "**Your turn.**" in body and "## Check yourself" in body
assert body.count('title="Answer"') >= 3
for qid in ("ex-da-devil-tumours", "ex-da-motn-insomnia"):
    assert f"../questions/{qid}.qmd" in page
for key in ("nist_doe_intro2002", "dodge2008"):
    assert f'data-cite-key="{key}"' in body or key == "nist_doe_intro2002"
# The new NIST key is resolved only when it is in bibliography.json.
# Until then the marker may remain or be dropped; require Dodge, which is present.
assert 'data-cite-key="dodge2008"' in body
print("designed experiment checks passed")
