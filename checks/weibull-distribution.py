"""Check Weibull median, mean, hazard and survival."""
from math import exp, gamma, log, sqrt
from pathlib import Path
root = Path(__file__).resolve().parents[1]
content = (root / "research/content/weibull-distribution.md").read_text()
article = root / "articles/weibull-distribution.qmd"
page = article.read_text().split("## See also", 1)[0] if article.is_file() else content

def need(s):
    assert s in content, s
    if article.is_file():
        assert s in page, s

k, lam = 1.5, 20
med = lam * (log(2)) ** (1/k)
mean = lam * gamma(1 + 1/k)
assert round(med, 2) == 15.66
assert round(mean, 2) == 18.05
assert round(exp(-1), 4) == 0.3679
assert abs((k/lam) - 0.075) < 1e-12
assert round(20*log(2), 2) == 13.86
assert abs(1/20 - 0.05) < 1e-12
assert round(10*sqrt(log(2)), 2) == 8.33
assert gamma(2) == 1
for s in ("15.66", "18.05", "0.3679", "0.075", "13.86", "0.05", "8.33"):
    need(s)
assert content.count('title="Proof"') == 1
assert "**Your turn.**" in content and content.count('title="Answer"') >= 3
print("Weibull checks passed")
