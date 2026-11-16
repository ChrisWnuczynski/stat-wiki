"""Check average-linkage heights and the scale reversal."""
from pathlib import Path
root = Path(__file__).resolve().parents[1]
body = (root / "articles/average-linkage.qmd").read_text().split("## See also", 1)[0]
assert (2+3)/2 == 2.5
assert (6+5)/2 == 5.5
assert abs((8+6+5)/3 - 19/3) < 1e-12
assert abs(19/3 - 6.333) < 0.001
assert (6+8+4+6)/4 == 6
assert min(6,8,4,6) == 4 and max(6,8,4,6) == 8
assert (1+5)/2 == 3
assert abs((16/5 + 16/5)/2 - 3.2) < 1e-12
assert (1+25)/2 == 13
assert abs(256/25 - 10.24) < 1e-12
assert (2*4 + 7)/3 == 5
for s in ("2.5", "5.5", "19/3", "6.333", "10.24"):
    assert s in body, s
assert body.count('title="Proof"') >= 1
assert "**Your turn.**" in body and "## Check yourself" in body
assert 'data-cite-key="hastie_esl2009"' in body
print("average linkage passed")
