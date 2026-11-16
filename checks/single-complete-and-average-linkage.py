"""Check linkage distances for the clinic and chain examples."""
from pathlib import Path

root = Path(__file__).resolve().parents[1]
page = (root / "articles/single-complete-and-average-linkage.qmd").read_text()
body = page.split("## See also", 1)[0]

cross = [10, 12, 9, 11]
assert min(cross) == 9 and max(cross) == 12 and sum(cross) / 4 == 10.5
chain = [2, 1]
assert min(chain) == 1 and max(chain) == 2 and sum(chain) / 2 == 1.5
far = [10, 9, 8]
assert min(far) == 8 and max(far) == 10 and sum(far) / 3 == 9
squares = [100, 144, 81, 121]
assert sum(squares) / 4 == 111.5 and 10.5 ** 2 == 110.25
assert 9 ** 2 == 81

for printed in ("10.5", "111.5", "110.25", "1.5", "3.5"):
    assert printed in body, printed
assert body.count('title="Proof"') == 1
assert "**Your turn.**" in body and "## Check yourself" in body
assert body.count('title="Answer"') >= 4
assert 'data-cite-key="hastie_esl2009"' in body
assert 'data-cite-key="dodge2008"' in body
print("linkage distances and practice passed")
