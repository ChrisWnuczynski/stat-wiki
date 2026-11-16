"""Check the two-state generator balance and the busy probability."""
from pathlib import Path
import math

root = Path(__file__).resolve().parents[1]
page = (root / "articles/generator.qmd").read_text()
body = page.split("## See also", 1)[0]

assert abs((1/2) / (1/2 + 1/4) - 2/3) < 1e-12
assert abs((1 - math.exp(-6)) / 3 - 0.332507) < 1e-4
assert round((1 - math.exp(-6)) / 3, 4) == 0.3325
assert round(1/3, 4) == 0.3333
# balance
pi0, pi1 = 2/3, 1/3
assert abs(pi0 * -2 + pi1 * 4) < 1e-12
assert abs(pi0 * 2 + pi1 * -4) < 1e-12

for printed in ("2/3", "1/3", "0.3325", "0.3333", "0.5", "0.25"):
    assert printed in body, printed
assert body.count('title="Proof"') == 1
assert "**Your turn.**" in body and "## Check yourself" in body
assert body.count('title="Answer"') >= 4
print("generator balance and practice passed")
