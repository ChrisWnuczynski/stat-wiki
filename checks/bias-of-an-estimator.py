"""Check variance bias and mean squared error."""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tools.shown import shown
root = Path(__file__).resolve().parents[1]
content = (root / "research/content/bias-of-an-estimator.md").read_text()
content = shown(content, "bias-of-an-estimator")
article = root / "articles/bias-of-an-estimator.qmd"
page = article.read_text().split("## See also", 1)[0] if article.is_file() else content

def need(s):
    assert s in content, s
    if article.is_file():
        assert s in page, s

n, sigma2 = 5, 4
bias = -sigma2/n
assert bias == -0.8
var_s = 2*sigma2**2/(n-1)
assert var_s == 8
scale = (n-1)/n
var_mle = scale**2 * var_s
assert abs(var_mle - 5.12) < 1e-12
mse = var_mle + bias**2
assert abs(mse - 5.76) < 1e-12 and abs(bias**2 - 0.64) < 1e-12
assert -9/8 == -1.125
assert abs(2*81/7 - 162/7) < 1e-12 and round(162/7, 3) == 23.143
assert 0.3 + 0.1**2 == 0.31
for s in ("-0.8", "5.12", "0.64", "5.76", "-1.125", "23.143", "0.31"):
    need(s)
assert content.count('title="Proof"') == 1
assert "**Your turn.**" in content and content.count('title="Answer"') >= 3
print("bias checks passed")
