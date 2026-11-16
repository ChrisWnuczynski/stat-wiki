"""Check learning-rate contractions on the quadratic bowl."""
from pathlib import Path

root = Path(__file__).resolve().parents[1]
page = (root / "articles/learning-rate.qmd").read_text()
body = page.split("## See also", 1)[0]

err = 2.0
vals = []
for _ in range(4):
    err *= 0.8
    vals.append(round(3 + err, 10))
assert vals == [4.6, 4.28, 4.024, 3.8192]
err = 2.0
fast = []
for _ in range(2):
    err *= 0.2
    fast.append(round(3 + err, 10))
assert fast == [3.4, 3.08]
assert abs(abs((1 - 2 * 1.1) * 2) - 2.4) < 1e-12
assert abs(round(3 + (1 - 2 * 1.1) * 2, 10) - 0.6) < 1e-12

for printed in ("4.6", "4.28", "4.024", "3.8192", "3.4", "3.08", "0.6", "2.4", "1.2"):
    assert printed in body, printed
assert body.count('title="Proof"') == 1
assert "**Your turn.**" in body and "## Check yourself" in body
assert body.count('title="Answer"') >= 4
assert 'data-cite-key="hastie_esl2009"' in body
print("learning-rate steps and practice passed")
