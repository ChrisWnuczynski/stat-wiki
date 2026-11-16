"""Check normal approximations and the Chebyshev bound for coin tosses."""
from pathlib import Path
from scipy.stats import binom, norm
from math import sqrt

root = Path(__file__).resolve().parents[1]
page = (root / "articles/limit-theorems.qmd").read_text()
body = page.split("## See also", 1)[0]

exact100 = 1 - binom.cdf(59, 100, 0.5)
plain = 1 - norm.cdf(2)
corr = 1 - norm.cdf(1.9)
assert round(exact100, 4) == 0.0284
assert round(plain, 4) == 0.0228
assert round(corr, 4) == 0.0287
assert abs(round(exact100, 4) - round(plain, 4) - 0.0056) < 1e-9
assert abs(round(corr, 4) - round(exact100, 4) - 0.0003) < 1e-9
assert round(binom.cdf(8, 20, 0.5), 4) == 0.2517
assert round(norm.cdf((8 - 10) / sqrt(5)), 3) == 0.186
assert round(norm.cdf((8.5 - 10) / sqrt(5)), 3) == 0.251
assert abs((0.25) / 100 / 0.01 - 0.25) < 1e-12

for printed in ("0.0284", "0.0228", "0.0287", "0.0003", "0.0056", "0.2517", "0.186", "0.251", "0.25"):
    assert printed in body, printed
assert body.count('title="Proof"') == 1
assert "**Your turn.**" in body and "## Check yourself" in body
assert body.count('title="Answer"') >= 4
assert body.count("![") >= 2
for key in ("durrett2019", "dodge2008"):
    assert f'data-cite-key="{key}"' in body
print("limit-theorem approximations and practice passed")
