"""Check Bonferroni levels and independent family-wise error."""
from pathlib import Path
import math

root = Path(__file__).resolve().parents[1]
page = (root / "articles/bonferroni-correction.qmd").read_text()
body = page.split("## See also", 1)[0]

assert 0.05 / 4 == 0.0125
assert abs(1 - 0.95 ** 4 - 0.18549375) < 1e-8
assert round(1 - 0.95 ** 4, 4) == 0.1855
assert round(1 - 0.9875 ** 4, 4) == 0.0491
assert round(1 - math.exp(-0.05), 4) == 0.0488
assert min(1, 4 * 0.02) == 0.08 and min(1, 4 * 0.01) == 0.04
assert min(1, 6 * 0.01) == 0.06
assert abs(4 * 0.0125 - 0.05) < 1e-12

for printed in ("0.1855", "0.0125", "0.0491", "0.0488", "0.08", "0.04", "0.06"):
    assert printed in body, printed
assert body.count('title="Proof"') == 1
assert "**Your turn.**" in body and "## Check yourself" in body
assert body.count('title="Answer"') >= 4
assert body.count("![") >= 1
for key in ("hastie_esl2009", "dodge2008", "durrett2019"):
    assert f'data-cite-key="{key}"' in body
print("bonferroni levels and practice passed")
