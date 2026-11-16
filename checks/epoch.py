"""Printed values for the epoch article."""

from pathlib import Path

root = Path(__file__).resolve().parents[1]
page = (root / "articles" / "epoch.qmd").read_text(encoding="utf-8")
body = page.split("## See also", 1)[0]

assert 20 / 4 == 5
assert 12 / 5 == 2.4
assert 3 * 20 == 60
assert 20 / 5 == 4
assert 8 / 4 == 2
assert 7 / 5 == 1.4
assert 5000 == 5000

for printed in ("20", "4", "5", "12", "2.4", "60", "3", "5000", "1.4", "2/5"):
    assert printed in body, printed
assert "**Your turn.**" in body
assert body.count('collapse="true" title="Answer"') == 3
assert "## Check yourself" in body
print("epoch checks passed")
