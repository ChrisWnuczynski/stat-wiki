"""Arithmetic checks for the positive predictive value article."""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tools.shown import shown

root = Path(__file__).resolve().parents[1]
text = (root / "research/content/positive-predictive-value.md").read_text()
text = shown(text, "positive-predictive-value")
page = (root / "articles/positive-predictive-value.qmd").read_text()
body = page.split("## See also", 1)[0]

def ppv(p, sens, spec):
    num = p * sens
    den = num + (1 - p) * (1 - spec)
    return num, den, num / den, (1 - p) * (1 - spec) / den

n, d, v, f = ppv(0.02, 0.90, 0.95)
assert abs(n - 0.018) < 1e-12 and abs(d - 0.067) < 1e-12
assert round(v, 3) == 0.269 and round(f, 3) == 0.731
n, d, v, f = ppv(0.10, 0.90, 0.95)
assert abs(n - 0.090) < 1e-12 and abs(d - 0.135) < 1e-12
assert round(v, 3) == 0.667 and round(f, 3) == 0.333
n, d, v, f = ppv(0.01, 0.99, 0.99)
assert abs(v - 0.5) < 1e-12
n, d, v, f = ppv(0.5, 0.9, 0.9)
assert abs(v - 0.9) < 1e-12
for printed in ("0.018", "0.049", "0.067", "0.269", "0.731", "0.090", "0.045",
                "0.135", "0.667", "0.333", "0.0099", "0.0198", "0.5", "0.45"):
    assert printed in text, printed
    assert printed in body, printed
assert text.count('title="Answer"') >= 3
assert 'title="Proof"' in text and "**Your turn.**" in text
print("positive predictive value checks passed")
