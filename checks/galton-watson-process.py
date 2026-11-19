"""Check Galton–Watson means, extinction roots and variances."""

from pathlib import Path

root = Path(__file__).resolve().parents[1]
page = (root / "articles/galton-watson-process.qmd").read_text()
body = page.split("## See also", 1)[0]

m = 3 / 2
sigma2 = 3 / 4
assert m == 0 * (1 / 4) + 2 * (3 / 4)
assert sigma2 == 3 - m ** 2
# (3s-1)(s-1) = 3s^2 - 4s + 1
assert 3 * (1 / 3) ** 2 - 4 * (1 / 3) + 1 == 0
var2 = sigma2 * m * ((m ** 2) - 1) / (m - 1)
assert var2 == 45 / 16 == 2.8125
# recurrence at n=1
assert m ** 2 * sigma2 + sigma2 * m == 45 / 16
# critical law
assert 0 * (2 / 5) + 1 * (1 / 5) + 2 * (2 / 5) == 1

for printed in ("1/3", "2/3", "3/2", "3/4", "45/16", "2.8125", "2/5", "1/5"):
    assert printed in body, printed
assert body.count('title="Proof"') == 1
assert "**Your turn.**" in body and "## Check yourself" in body
assert body.count('title="Answer"') >= 3
for qid in ("depth-galton-watson-process-q1", "depth-galton-watson-process-q2"):
    assert f"../questions/{qid}.qmd" in page
assert 'data-cite-key="durrett2019"' in body
print("galton-watson checks passed")
