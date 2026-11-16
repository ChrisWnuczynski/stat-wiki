"""Check effective-sample-size inflation factors."""

import math
from pathlib import Path

root = Path(__file__).resolve().parents[1]
page = (root / "articles/effective-sample-size.qmd").read_text()
body = page.split("## See also", 1)[0]

terms = [(1 - k / 5) * (0.5 ** k) for k in range(1, 5)]
assert round(sum(terms), 4) == 0.6125
inflation = 1 + 2 * sum(terms)
assert abs(inflation - 2.225) < 1e-12
assert round(5 / inflation, 3) == 2.247
assert abs((1 + 0.8) / (1 - 0.8) - 9) < 1e-9
assert round(1000 / 9, 2) == 111.11
assert round(math.sqrt(0.001), 5) == 0.03162
assert round(math.sqrt(0.009), 5) == 0.09487
assert round(math.sqrt(2.225), 3) == 1.492
assert abs((1 - 1 / 3) / (1 + 1 / 3) - 0.5) < 1e-12
assert 900 / 2 == 450
assert round(400 / 3, 2) == 133.33

for printed in (
    "0.6125", "2.225", "2.247", "111.11", "0.03162", "0.09487",
    "1.492", "450", "133.33", "0.8",
):
    assert printed in body, printed
assert body.count('title="Proof"') == 1
assert "**Your turn.**" in body and "## Check yourself" in body
assert body.count('title="Answer"') >= 3
for qid in ("ex-ur-one-change", "ex-ur-posterior-mean"):
    assert f"../questions/{qid}.qmd" in page
assert 'data-cite-key="geyer2005_markov_chain"' in body
print("effective sample size checks passed")
