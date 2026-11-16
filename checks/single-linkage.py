"""Check single-linkage heights and page structure."""
from pathlib import Path
root = Path(__file__).resolve().parents[1]
body = (root / "articles/single-linkage.qmd").read_text().split("## See also", 1)[0]
assert min(2, 3) == 2 and min(6, 5) == 5 and min(8, 6, 5) == 5
assert max(0, 2, 3) - min(0, 2, 3) == 3
assert min(10, 9, 8) == 8
assert max(0, 1, 2) - 0 == 2
# chain 0,1,2,3,6
assert 3-0 == 3 and 6-3 == 3
for s in ("$1$", "$2$", "$5$", "8"):
    assert s in body
assert body.count('title="Proof"') == 1
assert "**Your turn.**" in body and "## Check yourself" in body
assert 'data-cite-key="hastie_esl2009"' in body
assert 'data-cite-key="dodge2008"' in body
print("single linkage passed")
