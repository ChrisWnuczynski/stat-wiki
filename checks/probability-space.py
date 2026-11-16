"""Check the probability-space counts, series, and practice answers."""
from pathlib import Path

root = Path(__file__).resolve().parents[1]
page = (root / "articles/probability-space.qmd").read_text()
body = page.split("## See also", 1)[0]

assert 1/2 + 1/4 + 1/8 == 7/8
assert 1 - 7/8 == 1/8
assert 6 + 6 - 3 == 9
assert 9 / 36 == 1/4
assert 6 / 36 == 1/6
assert 3 / 36 == 1/12
assert 3 * 3 == 9
assert 2 ** 4 == 16
assert round(0.2 + 0.5 - 0.1, 10) == 0.6
assert round(1 - 0.2, 10) == 0.8
assert round((0.8 ** 2) * 0.2, 10) == 0.128
assert round(0.2 + 0.16 + 0.128, 10) == 0.488
assert round(0.8 ** 3, 10) == 0.512
assert round(0.4 * 3, 10) == 1.2

for printed in (
    "7/8", "1/8", "36", "1/6", "1/12", "1/4", "16",
    "0.2", "0.5", "0.1", "0.6", "0.8", "0.128", "0.488", "0.512", "1.2",
):
    assert printed in body, printed
assert body.count('title="Proof"') == 1
assert "## Motivating example" in body and "## Worked example" in body
assert "**Your turn.**" in body and "## Check yourself" in body
assert body.count('title="Answer"') >= 4
assert 'data-cite-key="durrett2019"' in body
print("probability-space counts, proof and practice passed")
