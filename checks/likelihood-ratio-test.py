"""Check binomial likelihood-ratio numbers and practice."""

from math import exp, log
from pathlib import Path
from scipy.stats import binom, chi2

root = Path(__file__).resolve().parents[1]
body = (root / "articles/likelihood-ratio-test.qmd").read_text().split("## See also", 1)[0]

def g2(n, k, p0=.5):
    phat = k/n
    return 2*(k*log(phat/p0)+(n-k)*log((1-phat)/(1-p0)))

g = g2(10, 8)
assert round(g, 4) == 3.8549
assert round(exp(-g/2), 4) == .1455
assert round(chi2.sf(g, 1), 4) == .0496
assert 2*binom.sf(7, 10, .5) == .109375
assert 2*(1+10+45)/1024 == .109375
gturn = g2(20, 14)
assert round(gturn, 4) == 3.2913
assert round(chi2.sf(gturn, 1), 5) == .06965
assert round(2*binom.sf(13, 20, .5), 5) == .11532

for printed in ("0.5", "0.8", "3.8549", "0.1455", "0.0496",
                "0.109375", "1024", "0.7", "3.2913", "0.06965", "0.11532"):
    assert printed in body, printed
assert body.count('title="Proof"') == 1
assert "## Motivating example" in body and "## Worked example" in body
assert "**Your turn.**" in body and 'title="Answer"' in body
for key in ("siegrist2022_lrt", "taboga2021_lrt", "dodge2008", "anastasiou_reinert2020"):
    assert f'data-cite-key="{key}"' in body
print("likelihood-ratio calculations and practice passed")
