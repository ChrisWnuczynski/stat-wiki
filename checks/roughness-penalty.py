"""Check roughness integrals, the three-point line, and the penalty comparison."""
from pathlib import Path
import math

root = Path(__file__).resolve().parents[1]
page = (root / "articles/roughness-penalty.qmd").read_text()
body = page.split("## See also", 1)[0]

assert abs(8 * math.pi ** 4 - 779.272728) < 1e-5
assert round(8 * math.pi ** 4, 2) == 779.27
sxy = (0 - 1) * (0 - 1 / 3) + (2 - 1) * (0 - 1 / 3)
assert sxy == 0
rss = 2 * (1 / 3) ** 2 + (2 / 3) ** 2
assert abs(rss - 2 / 3) < 1e-12
assert abs(8 * (1 / 12) - 2 / 3) < 1e-12
assert abs(8 * 0.1 - 0.8) < 1e-12
assert 36 * (1 / 3) == 12
assert 4 * 1 == 4

for printed in ("1/3", "2/3", "779.27", "8\\pi^4", "1/12", "0.1", "0.8", "12", "0.00022"):
    assert printed in body, printed
assert body.count('title="Proof"') == 1
assert "## Motivating example" in body and "## Worked example" in body
assert "**Your turn.**" in body and "## Check yourself" in body
assert body.count('title="Answer"') >= 4
assert body.count("![") >= 1
assert 'data-cite-key="hastie_esl2009"' in body
print("roughness-penalty integrals, line and practice passed")
