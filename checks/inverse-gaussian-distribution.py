"""Check inverse-Gaussian moments, density height and tail probabilities."""

import math
from pathlib import Path
from scipy.stats import invgauss

root = Path(__file__).resolve().parents[1]
page = (root / "articles/inverse-gaussian-distribution.qmd").read_text()
body = page.split("## See also", 1)[0]

def height(mu, lam):
    return math.sqrt(lam / (2 * math.pi * mu ** 3))

assert 2 ** 3 / 4 == 2
assert 4 ** 3 / 4 == 16
assert 4 ** 3 / 16 == 4
assert round(math.sqrt(2), 4) == 1.4142
assert round(height(2, 4), 4) == 0.2821
assert round(height(4, 16), 4) == 0.1995
# scipy: mu_shape = mu/lam, scale = lam
assert round(invgauss.sf(3, 2 / 4, scale=4), 4) == 0.1756
assert round(invgauss.cdf(1, 0.5, scale=4), 4) == 0.2324
assert round(invgauss.cdf(2, 0.5, scale=4), 4) == 0.6277
assert abs(invgauss.pdf(2, 0.5, scale=4) - height(2, 4)) < 1e-12
mean, var = invgauss.stats(0.25, scale=16, moments="mv")
assert float(mean) == 4 and float(var) == 4
mean_b, var_b = invgauss.stats(4, scale=1, moments="mv")
assert float(mean_b) == 4 and float(var_b) == 64
assert abs(16 ** 2 * (0.25) ** 3 - 4) < 1e-12

for printed in (
    "0.2821", "0.1756", "0.2324", "0.6277", "0.1995", "1.4142",
    "64", "16", "0.25",
):
    assert printed in body, printed
assert 'title="Proof"' in body  # the distribution card supplies one
assert "**Your turn.**" in body
assert body.count('title="Answer"') >= 2
print("inverse gaussian checks passed")
