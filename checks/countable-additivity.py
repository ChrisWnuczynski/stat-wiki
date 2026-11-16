"""Printed values for the countable-additivity article."""

from pathlib import Path

root = Path(__file__).resolve().parents[1]
page = (root / "articles" / "countable-additivity.qmd").read_text(encoding="utf-8")
body = page.split("## See also", 1)[0]

assert abs(sum(0.5 ** k for k in range(1, 40)) - 1) < 1e-9
assert abs((1 - 2 ** -3) - 0.875) < 1e-12
assert abs((1 - 2 ** -4) - 0.9375) < 1e-12
assert abs((1 - 2 ** -5) - 0.96875) < 1e-12
assert abs((0.5 ** 4 + 0.5 ** 5) - 0.09375) < 1e-12
assert abs(0.96875 - 0.875 - 0.09375) < 1e-12
assert 0.25 + 0.25 == 0.5

for printed in ("0.875", "0.9375", "0.96875", "0.09375", "7/8", "15/16", "31/32", "3/32"):
    assert printed in body, printed
assert body.count('title="Proof"') == 1
assert "**Your turn.**" in body
assert body.count('collapse="true" title="Answer"') == 3
assert "## Check yourself" in body
print("countable additivity checks passed")
