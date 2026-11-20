"""Check global and detailed balance residuals."""

from pathlib import Path

root = Path(__file__).resolve().parents[1]
page = (root / "articles/global-balance-and-detailed-balance.qmd").read_text()
body = page.split("## See also", 1)[0]

a, b = 1 / 5, 1 / 2
pi0, pi1 = 5 / 7, 2 / 7
global_resid = pi0 * (1 - a) + pi1 * b - pi0
detail_resid = pi0 * a - pi1 * b
assert abs(global_resid) < 1e-12 and abs(detail_resid) < 1e-12
assert round(pi0, 4) == 0.7143 and round(pi1, 4) == 0.2857
assert abs((1 / 3) - 0) == 1 / 3

for printed in ("1/3", "0.7143", "0.2857", "5/7", "2/7"):
    assert printed in body, printed
assert body.count('title="Proof"') == 1
assert "**Your turn.**" in body and "## Check yourself" in body
assert body.count('title="Answer"') >= 3
for qid in ("ex-sp-deterministic-cycle", "ex-sp-doubly-stochastic"):
    assert f"../questions/{qid}.qmd" in page
for key in ("durrett2019",):
    assert f'data-cite-key="{key}"' in body
print("global and detailed balance checks passed")
