"""Check nested squared-error comparison."""
from pathlib import Path
root = Path(__file__).resolve().parents[1]
body = (root / "articles/nested-cross-validation.qmd").read_text().split("## See also", 1)[0]
y = [0, 1, 0, 8]
cands = [0, 1, 4]
full = [sum((yi-c)**2 for yi in y)/4 for c in cands]
assert full == [16.25, 12.75, 14.25]
# hold out index 3 (value 8)
rest = [0, 1, 0]
inner = [sum((yi-c)**2 for yi in rest)/3 for c in cands]
assert abs(inner[0] - 1/3) < 1e-12
assert abs(inner[1] - 2/3) < 1e-12
assert abs(inner[2] - 41/3) < 1e-12
assert (8-0)**2 == 64
# hold out a zero, leave 1,0,8
rest2 = [1, 0, 8]
inner2 = [sum((yi-c)**2 for yi in rest2)/3 for c in cands]
assert abs(inner2[0] - 65/3) < 1e-12
assert abs(inner2[1] - 50/3) < 1e-12
assert abs(inner2[2] - 41/3) < 1e-12
assert (0-4)**2 == 16
# hold out 1, leave 0,0,8
rest3 = [0, 0, 8]
inner3 = [sum((yi-c)**2 for yi in rest3)/3 for c in cands]
assert abs(inner3[0] - 64/3) < 1e-12
assert inner3[1] == 17
assert inner3[2] == 16
assert (1-4)**2 == 9
assert (16+9+16+64)/4 == 26.25
for s in ("16.25", "12.75", "14.25", "26.25", "64"):
    assert s in body, s
assert body.count('title="Proof"') == 1
assert "**Your turn.**" in body and "## Check yourself" in body
assert 'data-cite-key="cawley_talbot2010"' in body
print("nested cv passed")
