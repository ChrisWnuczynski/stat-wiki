"""Check printed pooled-variance arithmetic against the generated article."""

import math
from pathlib import Path

root = Path(__file__).resolve().parents[1]
page = (root / "articles/pooled-variance.qmd").read_text()
body = page.split("## See also", 1)[0]

s1 = 95000 / 7
assert round(s1, 3) == 13571.429
assert 165000 / 12 == 13750
se_var = 13750 * (1 / 8 + 1 / 6)
assert round(se_var, 3) == 4010.417
assert round(math.sqrt(se_var), 3) == 63.328
weighted_by_n = (8 * (95000 / 7) + 6 * 14000) / 14
assert round(weighted_by_n, 3) == 13755.102
assert round(269 / 14, 3) == 19.214
assert 200 / 7 == 200 / 7 and round(200 / 7, 3) == 28.571
assert 999 / 108 == 9.25
assert round(math.sqrt(9.250 / 100), 3) == 0.304
assert round(math.sqrt(1 / 100), 3) == 0.100
assert round(math.sqrt(9.250 / 10), 3) == 0.962
assert round(math.sqrt(100 / 10), 3) == 3.162

ss = 49 * 14.1 ** 2 + 49 * 14.3 ** 2
assert round(49 * 14.1 ** 2, 2) == 9741.69
assert round(49 * 14.3 ** 2, 2) == 10020.01
assert round(ss, 2) == 19761.70
sp2 = ss / 98
assert round(sp2, 2) == 201.65
assert round(math.sqrt(sp2), 3) == 14.200
ratio = 14.1 ** 2 / 14.3 ** 2
assert round(198.81 / 204.49, 5) == 0.97222
lo, hi = ratio / 1.762, ratio * 1.762
assert round(lo, 5) == 0.55177
assert round(hi, 5) == 1.71306
assert round(lo, 4) == 0.5518 and round(hi, 4) == 1.7131

for printed in (
    "2800", "95000", "2600", "70000", "13750", "13571.429", "14000",
    "63.328", "4010.417", "13755.102", "19.214", "28.571", "9.250",
    "0.304", "0.100", "0.962", "3.162", "14.1", "14.3", "9741.69",
    "10020.01", "19761.70", "201.65", "14.200", "0.97222", "1.762",
    "0.55177", "1.71306", "0.5518", "1.7131", "12",
):
    assert printed in body, printed

assert body.count('title="Proof"') == 1
assert "## Motivating example" in body and "## Worked example" in body
assert "**Your turn.**" in body and "## Check yourself" in body
assert body.count('title="Answer"') >= 3
for qid in ("ex-inf-safety-interval", "depth-pooled-variance-q1", "depth-pooled-variance-q2"):
    assert f"../questions/{qid}.qmd" in page
for key in ("dodge2008", "siegrist2022_normals", "nist_mean_limits2002"):
    assert f'data-cite-key="{key}"' in body
print("pooled variance checks passed")
