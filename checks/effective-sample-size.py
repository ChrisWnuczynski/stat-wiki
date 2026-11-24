"""Check effective-sample-size inflation factors."""

import math
from fractions import Fraction
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

# Finite-n convention on the page: Var(mean) = (sigma^2 / n) * multiplier,
# with multiplier = 1 + 2 * sum_{k=1}^{n-1} (1 - k/n) rho_k,
# and n_eff defined by sigma^2 / n_eff = Var(mean). For rho_k = (-1/2)^k
# this is not the infinite-sum factor (1+rho)/(1-rho) = 1/3.
neg_terms = [(1 - k / 5) * ((-0.5) ** k) for k in range(1, 5)]
neg_sum = sum(neg_terms)
assert abs(neg_sum - (-23 / 80)) < 1e-12
assert abs(neg_sum - (-0.2875)) < 1e-12
neg_mult = 1 + 2 * neg_sum
assert abs(neg_mult - (17 / 40)) < 1e-12
assert abs(neg_mult - 0.425) < 1e-12
neg_ess = 5 / neg_mult
assert abs(neg_ess - (200 / 17)) < 1e-12
assert round(neg_ess, 3) == 11.765
var_mean = neg_mult / 5
assert abs(var_mean - (17 / 200)) < 1e-12
assert abs(var_mean - 0.085) < 1e-12
var_s = 5 + 2 * sum((5 - k) * ((-0.5) ** k) for k in range(1, 5))
assert abs(var_s - (17 / 8)) < 1e-12
assert abs(var_s / 25 - var_mean) < 1e-12
lag1_pairs = 2 * (5 - 1) * (-0.5)
assert lag1_pairs == -4
inf_factor = (1 + (-0.5)) / (1 - (-0.5))
assert abs(inf_factor - (1 / 3)) < 1e-12
assert abs(5 / inf_factor - 15) < 1e-12

# Alternating the signs of centered variables multiplies lag-k correlation by (-1)^k.
# A global sign flip would not. Perfect alternation rho_k = (-1)^k makes the
# finite-n multiplier exactly zero for every even n, so no finite ESS exists.
flipped = [((-1) ** k) * (Fraction(1, 2) ** k) for k in range(1, 5)]
assert flipped == [Fraction(-1, 2) ** k for k in range(1, 5)]
for n in range(2, 22, 2):
    exact = 1 + 2 * sum((1 - Fraction(k, n)) * ((-1) ** k) for k in range(1, n))
    assert exact == 0, (n, exact)
    assert sum((-1) ** t for t in range(1, n + 1)) == 0

for printed in (
    "0.6125", "2.225", "2.247", "111.11", "0.03162", "0.09487",
    "1.492", "450", "133.33", "0.8",
    "0.425", "11.765", "17/40", "200/17", "0.085", "17/200", r"\frac{17}{8}",
):
    assert printed in body, printed
assert "survived the dependence" not in body
assert "survived" not in body
assert "signs reversed" not in body
assert "(-1)^t" in body
assert "multiplier is therefore zero" in body
assert "variance of the mean is also positive" in body
assert r"0<\sigma^2<\infty" in body
assert body.count('data-cite-key="stan_reference_analysis2026"') >= 2
assert 'data-locator="§16.4, p. 196"' in body
assert 'data-locator="§16.4, p. 197"' in body
assert body.count('title="Proof"') == 1
assert "**Your turn.**" in body and "## Check yourself" in body
assert body.count('title="Answer"') >= 3
for qid in ("ex-ur-one-change", "ex-ur-posterior-mean"):
    assert f"../questions/{qid}.qmd" in page
assert 'data-cite-key="geyer1992"' in body
print("effective sample size checks passed")
