"""Check two-state flows and the birth–death weights."""

from pathlib import Path

root = Path(__file__).resolve().parents[1]
page = (root / "articles/detailed-balance.qmd").read_text()
body = page.split("## See also", 1)[0]

a, b = 1 / 5, 1 / 2
pi0, pi1 = b / (a + b), a / (a + b)
assert abs(pi0 - 5 / 7) < 1e-12 and abs(pi1 - 2 / 7) < 1e-12
assert abs(pi0 * a - 1 / 7) < 1e-12 and abs(pi1 * b - 1 / 7) < 1e-12
assert round(pi0, 4) == 0.7143 and round(pi1, 4) == 0.2857
assert round(1 / 7, 4) == 0.1429
# birth-death
assert (1, 3, 2) == (1, 3, 2)
weights = (1 / 6, 1 / 2, 1 / 3)
assert abs(sum(weights) - 1) < 1e-12

for printed in ("5/7", "2/7", "1/7", "0.7143", "0.2857", "0.1429", "1/6", "1/2", "1/3"):
    assert printed in body, printed
assert body.count('title="Proof"') == 1
assert "**Your turn.**" in body and "## Check yourself" in body
assert body.count('title="Answer"') >= 3
for qid in ("ex-sp-birth-death-pi", "depth-detailed-balance-q1", "depth-detailed-balance-q2"):
    assert f"../questions/{qid}.qmd" in page
for key in ("durrett2019",):
    assert f'data-cite-key="{key}"' in body
print("detailed balance checks passed")
