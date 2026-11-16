"""Check negative-binomial numerical examples and rendered depth."""

from math import exp, isclose
from pathlib import Path
from scipy.stats import nbinom, poisson

page = (Path(__file__).resolve().parents[1] / "articles/negative-binomial-distribution.qmd").read_text()
body = page.split("## See also", 1)[0]

assert 3 + 3**2 / 1 == 12
assert isclose(nbinom.pmf(0, 1, 1 / 4), 1 / 4)
assert round(poisson.pmf(0, 3), 4) == .0498
assert isclose(nbinom.sf(6, 1, 1 / 4), (3 / 4)**7)
assert round(nbinom.sf(6, 1, 1 / 4), 4) == .1335
assert round(poisson.sf(6, 3), 4) == .0335
assert 3.9 < nbinom.sf(6, 1, 1 / 4) / poisson.sf(6, 3) < 4
assert 2 + 2**2 / 2 == 4
assert isclose(nbinom.pmf(0, 2, .5), .25)
assert isclose(nbinom.pmf(1, 2, .5), .25)
assert 4 + 4**2 / 2 == 12
assert isclose(nbinom.pmf(0, 2, 2 / 6), 1 / 9)
assert isclose(nbinom.pmf(0, 2, 2 / 5), .16)
for printed in ("0.0498", "0.1335", "0.0335", "1/4", "3+3^2/1=12", "2+2^2/2=4", "4+4^2/2=12", "1/9"):
    assert printed in body, printed
for heading in ("## Motivating example", "{#intuition}", "## Definition", "## Properties", "## Related distributions", "## Statistical inference", "## Worked example", "## Common misconceptions", "## Assumptions and limits", "## Connections", "## History"):
    assert heading in body, heading
assert "**Your turn.**" in body and 'title="Answer"' in body
assert body.count('title="Proof"') == 1
assert page.count("![") >= 2
assert 'data-cite-key="zeileis_kleiber_jackman2008"' in body
print("Negative binomial examples and inherited plots passed")
