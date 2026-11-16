"""Check Kullback–Leibler values for two binary distributions."""
from pathlib import Path
import math

root = Path(__file__).resolve().parents[1]
page = (root / "articles/kullback-leibler-divergence.qmd").read_text()
body = page.split("## See also", 1)[0]

forward = 0.8 * math.log(1.6) + 0.2 * math.log(0.4)
reverse = 0.5 * math.log(0.5 / 0.8) + 0.5 * math.log(0.5 / 0.2)
near = 0.8 * math.log(0.8 / 0.9) + 0.2 * math.log(2)
assert round(forward, 4) == 0.1927
assert round(reverse, 4) == 0.2231
assert round(forward / math.log(2), 4) == 0.2781
assert round(near, 4) == 0.0444
assert forward > 0 and reverse > 0 and near < forward

for printed in ("0.1927", "0.2231", "0.2781", "0.0444"):
    assert printed in body, printed
assert body.count('title="Proof"') == 1
assert "**Your turn.**" in body and "## Check yourself" in body
assert body.count('title="Answer"') >= 4
for key in ("shannon1948", "hastie_esl2009"):
    assert f'data-cite-key="{key}"' in body
print("kullback-leibler values and practice passed")
