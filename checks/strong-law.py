"""Check strong-law moment bounds for a fair coin."""
from pathlib import Path

root = Path(__file__).resolve().parents[1]
page = (root / "articles/strong-law.qmd").read_text()
body = page.split("## See also", 1)[0]

def fourth(n):
    return (n + 3 * n * (n - 1)) / 16

assert abs((1 / 4) / (100 * 0.01) - 0.25) < 1e-12
assert fourth(100) == 1862.5
assert abs(1862.5 / 100 ** 4 - 0.000018625) < 1e-15
assert abs(0.000018625 / 0.0001 - 0.18625) < 1e-12
assert abs((1 / 4) / 50 / 0.04 - 0.125) < 1e-12
assert fourth(50) == 462.5
assert abs(462.5 / 50 ** 4 - 0.000074) < 1e-15
assert abs(0.000074 / 0.0016 - 0.04625) < 1e-12
assert abs(1 / (2 * 400 ** 0.5) - 0.025) < 1e-12

for printed in ("0.25", "1862.5", "0.000018625", "0.18625", "0.125", "462.5", "0.000074", "0.04625"):
    assert printed in body, printed
assert body.count('title="Proof"') == 1
assert "**Your turn.**" in body
assert body.count('title="Answer"') >= 4
assert 'data-cite-key="durrett2019"' in body
assert 'data-cite-key="dodge2008"' in body
print("strong-law moment bounds and practice passed")
