"""Check geometric trial probabilities, means, and the failure-count shift."""
from pathlib import Path

root = Path(__file__).resolve().parents[1]
page = (root / "articles/geometric-distribution.qmd").read_text()
body = page.split("## See also", 1)[0]

assert abs(0.8 ** 3 - 0.512) < 1e-12
assert abs(0.8 * 0.2 - 0.16) < 1e-12
assert abs((0.8 ** 2) * 0.2 - 0.128) < 1e-12
assert abs(0.2 + 0.16 + 0.128 - 0.488) < 1e-12
assert abs(0.8 / 0.04 - 20) < 1e-12
assert round(20 ** 0.5, 3) == 4.472
assert round(0.8 ** 10, 4) == 0.1074
assert 27 / 64 == 0.421875
assert round(27 / 64, 4) == 0.4219
assert (3 / 4) / (1 / 4) == 3

for printed in ("0.512", "0.128", "0.488", "4.472", "0.1074", "27/64", "0.4219"):
    assert printed in body, printed
assert body.count('title="Proof"') == 1
assert "**Your turn.**" in body
assert body.count('title="Answer"') >= 3
assert 'data-cite-key="dodge2008"' in body
print("geometric probabilities and practice passed")
