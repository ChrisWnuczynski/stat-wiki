"""Check beta posterior hypothesis probabilities and the loss comparison."""

from math import comb
from pathlib import Path
from scipy.stats import beta

root = Path(__file__).resolve().parents[1]
page = (root / "articles/posterior-hypothesis-probability.qmd").read_text()
body = page.split("## See also", 1)[0]

p0 = beta.cdf(0.5, 8, 4)
assert p0 == sum(comb(11, j) for j in range(8, 12)) / 2 ** 11
assert p0 == 29 / 256
assert round(p0, 4) == 0.1133
assert round(1 - p0, 4) == 0.8867
assert round(0.1133 / 0.8867, 4) == 0.1278
assert round(8 / 12, 4) == 0.6667
lo, hi = beta.ppf(0.025, 8, 4), beta.ppf(0.975, 8, 4)
assert round(lo, 4) == 0.3903 and round(hi, 4) == 0.8907
assert round(10 * 0.1133, 3) == 1.133
assert round(2 * 0.1278, 4) == 0.2556
assert round(4 / 12, 4) == 0.3333
# three heads swaps the probability
assert round(1 - beta.cdf(0.5, 4, 8), 4) == round(p0, 4)

for printed in (
    "0.1133", "0.8867", "0.1278", "0.6667", "0.3903", "0.8907",
    "1.133", "0.2556", "0.3333", "29/256", "0.11328125",
):
    assert printed in body, printed
assert body.count('title="Proof"') == 1
assert "**Your turn.**" in body and "## Check yourself" in body
assert body.count('title="Answer"') >= 3
for qid in ("c-08", "q-44"):
    assert f"../questions/{qid}.qmd" in page
assert 'data-cite-key="dodge2008"' in body
print("posterior hypothesis probability checks passed")
