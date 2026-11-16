"""Check hierarchical merge heights and cophenetic averages."""
from pathlib import Path

root = Path(__file__).resolve().parents[1]
page = (root / "articles/hierarchical-clustering.qmd").read_text()
body = page.split("## See also", 1)[0]

cross = [10, 12, 9, 11]
assert sum(cross) / 4 == 10.5
assert (1 + 2 + 4 * 10.5) / 6 == 7.5
assert (1 + 10 + 12 + 9 + 11 + 2) / 6 == 7.5
assert (1 + 2 + 4 * 9) / 6 == 6.5
assert (1 + 2 + 4 * 12) / 6 == 8.5
assert 4 * 3 / 2 == 6 and 4 - 1 == 3

for printed in ("10.5", "7.5", "6.5", "8.5"):
    assert printed in body, printed
assert body.count('title="Proof"') == 1
assert "**Your turn.**" in body and "## Check yourself" in body
assert body.count('title="Answer"') >= 4
assert 'data-cite-key="hastie_esl2009"' in body
assert 'data-cite-key="dodge2008"' in body
print("hierarchical heights and practice passed")
