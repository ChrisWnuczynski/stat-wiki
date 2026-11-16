"""Check minimal-sufficiency likelihood ratios."""
from pathlib import Path
import math

root = Path(__file__).resolve().parents[1]
page = (root / "articles/minimal-sufficiency.qmd").read_text()
body = page.split("## See also", 1)[0]

assert 2 + 0 + 5 == 7 and 1 + 3 + 3 == 7 and 4 + 0 + 0 == 4
assert math.factorial(1) * math.factorial(3) * math.factorial(3) == 36
assert math.factorial(2) * math.factorial(0) * math.factorial(5) == 240
assert 36 / 240 == 0.15
assert math.factorial(4) / 240 == 0.1
assert 0.1 * 1 ** 3 == 0.1 and 0.1 * 2 ** 3 == 0.8
assert round(math.exp(-1), 4) == 0.3679
assert abs((1.1 - 1) - 0.1) < 1e-12 and abs((1.1 - 0.2) - 0.9) < 1e-12

for printed in ("0.15", "0.1", "0.8", "0.3679", "0.9", "[0.1,0.2]"):
    assert printed in body, printed
assert body.count('title="Proof"') == 1
assert "**Your turn.**" in body and "## Check yourself" in body
assert body.count('title="Answer"') >= 4
print("minimal-sufficiency ratios and practice passed")
