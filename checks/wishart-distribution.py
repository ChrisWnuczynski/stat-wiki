"""Check Wishart means, entry variances, and the normal fourth moment."""
from pathlib import Path

root = Path(__file__).resolve().parents[1]
page = (root / "articles/wishart-distribution.qmd").read_text()
body = page.split("## See also", 1)[0]

assert 3 * 2 == 6 and 3 * 1 == 3
assert 3 * (2 * 2 + 2 * 2) == 24
assert 3 * (1 * 1 + 1 * 1) == 6
assert 3 * (2 * 2 + 1 * 1) == 15
assert round(24 ** 0.5, 3) == 4.899
assert 4 * 2 == 8 and 2 * 4 * (2 ** 2) == 32
assert 5 * 4 == 20 and 5 * (16 + 16) == 160
assert 3 * 1 == 3

for printed in ("24", "15", "4.899", "160", "8", "32", "6"):
    assert printed in body, printed
assert body.count('title="Proof"') == 1
assert "**Your turn.**" in body
assert body.count('title="Answer"') >= 3
assert 'data-cite-key="durrett2019"' in body
assert 'data-cite-key="dodge2008"' in body
print("wishart moments and practice passed")
