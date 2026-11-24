"""Check significance-level critical values, intervals and discrete size."""

import math
from math import comb
from pathlib import Path
from scipy.stats import binom, t

root = Path(__file__).resolve().parents[1]
page = (root / "articles/significance-level.qmd").read_text()
body = page.split("## See also", 1)[0]

n = 195
mean, sd = 9.261460, 0.022789
crit = t.ppf(0.975, n - 1)
assert round(crit, 4) == 1.9723
se = sd / math.sqrt(n)
margin = 1.9723 * se
assert (round(mean - margin, 6), round(mean + margin, 6)) == (9.258241, 9.264679)
assert round(t.ppf(0.95, n - 1), 4) == 1.6527
T = (mean - 5) / se
assert 2611 < T < 2612

se_bp = 7 / math.sqrt(101)
assert round(se_bp, 4) == 0.6965
assert round(1.960 * round(se_bp, 4), 3) == 1.365
assert round(127 - 1.365, 3) == 125.635
assert round(127 + 1.365, 3) == 128.365

def binomial_tail(ks, success, total):
    """Exact tail probability for Bin(15, success/total)."""
    numerator = sum(comb(15, k) * success**k * (total - success) ** (15 - k) for k in ks)
    return numerator / total**15

size = binomial_tail(range(13, 16), 3, 5)
tail_from_12 = binomial_tail(range(12, 16), 3, 5)
atom_12 = binomial_tail((12,), 3, 5)
power = binomial_tail(range(13, 16), 9, 10)
assert round(size, 6) == 0.027114
assert round(size * 100, 4) == 2.7114
assert round(tail_from_12, 6) == 0.090502
assert round(atom_12, 6) == 0.063388
assert round(power, 4) == 0.8159
assert abs(sum(binom.pmf(k, 15, 0.6) for k in (13, 14, 15)) - size) < 1e-12
assert round(1.635 * 1.1 / 6, 4) == 0.2998

for printed in (
    "9.261460", "0.022789", "1.9723", "9.258241", "9.264679", "1.6527",
    "0.6965", "1.365", "125.635", "128.365", "0.027114", "2.7114",
    "0.090502", "0.063388", "0.8159", "0.2998", "1.960", "1.635", "2611",
):
    assert printed in body, printed
assert "about 5%" not in body
assert body.count('title="Proof"') == 1
assert "**Your turn.**" in body and "## Check yourself" in body
assert body.count('title="Answer"') >= 3
for qid in ("ex-inf-blood-pressure-region", "ex-inf-serve-power"):
    assert f"../questions/{qid}.qmd" in page
for key in ("nist_mean_limits2002", "dodge2008", "rudloff_karatzas2010", "siegrist2022_testing"):
    assert f'data-cite-key="{key}"' in body
print("significance level checks passed")
