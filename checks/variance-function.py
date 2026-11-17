"""Check displayed variance functions and numeric examples."""

from math import isclose, sqrt
from pathlib import Path

body = (Path(__file__).resolve().parents[1] / "articles/variance-function.qmd").read_text().split("## See also")[0]

normal = lambda mu: 1
poisson = lambda mu: mu
bernoulli = lambda mu: mu * (1 - mu)
gamma = lambda mu: mu ** 2
inv_gaussian = lambda mu: mu ** 3
assert (normal(2), poisson(2), gamma(2), inv_gaussian(2)) == (1, 2, 4, 8)
assert isclose(bernoulli(.2), .16)
assert (poisson(2), poisson(6)) == (2, 6)
assert gamma(6) / gamma(2) == 9
phi = .25
assert (phi * gamma(2), phi * gamma(6)) == (1, 9)
assert (sqrt(phi * gamma(2)), sqrt(phi * gamma(6))) == (1, 3)
assert sqrt(phi) == .5
assert all(isclose(a, b) for a, b in zip((bernoulli(.2), bernoulli(.8), bernoulli(.5)), (.16, .16, .25)))
assert isclose(bernoulli(.8), .16)
assert (poisson(2), poisson(6)) == (2, 6)
assert (.5 * gamma(3), .5 * gamma(6)) == (4.5, 18)
assert round(sqrt(4.5), 3) == 2.121 and round(sqrt(18), 3) == 4.243

for printed in (
    "V(\\mu)=1", "V(\\mu)=\\mu", "\\mu(1-\\mu)", "\\mu^2", "\\mu^3",
    "\\phi=1/4", "=1", "=9", "0.16", "0.25", "\\phi=1/2", "=4.5",
    "=18", "2.121", "4.243", "0.2", "0.8", "0.5", "w_i>0",
):
    assert printed in body, f"Missing displayed value: {printed}"
assert body.count('title="Proof"') == 1
assert "## Motivating example" in body and "## Worked example" in body
assert "**Your turn.**" in body and 'title="Answer"' in body
for key in ("nelder_wedderburn1972", "rstats_family2026", "wuthrich_merz2022_glm"):
    assert f'data-cite-key="{key}"' in body
print("variance function examples, proof and citations passed")
