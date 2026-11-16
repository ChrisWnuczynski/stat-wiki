"""Check the numbers and preserved examples in exchangeability."""

from fractions import Fraction as F
from pathlib import Path

root = Path(__file__).resolve().parents[1]
page = (root / "articles/exchangeability.qmd").read_text()
body = page.split("## See also", 1)[0]

alpha, beta = 2, 3
mean = F(alpha, alpha + beta)
second = F(alpha * (alpha + 1), (alpha + beta) * (alpha + beta + 1))
p11 = second
p10 = mean - second
p01 = p10
p00 = 1 - p11 - p10 - p01
assert (mean, p11, p10, p01, p00) == (F(2, 5), F(1, 5), F(1, 5), F(1, 5), F(2, 5))
assert second - mean**2 == F(1, 25)
assert F(alpha + 1, alpha + beta + 1) == F(1, 2)
assert F(alpha, alpha + beta + 1) == F(1, 3)

p10_urn = p01_urn = F(1, 2)
assert p10_urn + p01_urn == 1
assert 0 - F(1, 2)**2 == -F(1, 4)

for fragment in (
    "## Motivating example", "## Worked example", "**Your turn.**",
    'title="Proof"', 'title="Answer"', "0.04", "0.333333",
    "-1/4", "4$ tumours among $14$", "$70$ historical",
    "## Common misconceptions", "#assumptions-and-limits",
):
    assert fragment in body, f"Missing section or calculation: {fragment}"
assert body.count('title="Proof"') == 1
for link in ("../questions/c-09.qmd", "../notes/bayes-08-hierarchy.qmd#exm-rat-tumour-hierarchy"):
    assert link in page, f"Lost inherited link: {link}"
print("exchangeability beta-mixture and finite-draw calculations passed")

assert abs(0.5 * (0.2 * 0.8 + 0.8 * 0.2) - 0.16) < 1e-12
assert abs(0.5 * (0.2 ** 2 + 0.8 ** 2) - 0.34) < 1e-12
assert 0.5 * 0.5 == 0.25
assert "../questions/depth-exchangeability-mixture.qmd" in page
