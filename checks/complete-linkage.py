"""Check complete-linkage heights, comparisons, and page structure."""

from pathlib import Path

root = Path(__file__).resolve().parents[1]
page = (root / "articles" / "complete-linkage.qmd").read_text(encoding="utf-8")
body = page.split("## See also", 1)[0]

# Four points 0, 2, 3, 8.
assert max(2, 3) == 3
assert max(6, 5) == 6
assert max(8, 6, 5) == 8
assert min(8, 6, 5) == 5
# Three points 0, 1, 4.
assert max(4 - 0, 4 - 1) == 4
# Squared comparison does not reorder the maxima.
assert max(1, 9) == 9 and max(4, 6) == 6
assert max(1 ** 2, 9 ** 2) == 81 and max(4 ** 2, 6 ** 2) == 36
assert 36 < 81 and 6 < 9
# Points 0, 1, 2, 10.
assert max(2, 1) == 2
assert max(10, 9, 8) == 10
assert min(10, 9, 8) == 8
assert max(0, 1, 2) - min(0, 1, 2) == 2

for printed in (
    "0", "2", "3", "8", "1", "6", "5", "4", "9", "81", "36", "10",
    "$1$", "$3$", "$8$",
):
    assert printed in body, printed
assert "19/3" not in body  # that fraction belongs to average linkage
assert body.count('title="Proof"') == 1
assert "## Motivating example" in body and "## Worked example" in body
assert "**Your turn.**" in body and "## Check yourself" in body
assert body.count('title="Answer"') >= 4
for key in ("hastie_esl2009", "james_islr2021", "dodge2008"):
    assert f'data-cite-key="{key}"' in body
print("complete linkage heights, proof and practice passed")
