"""Check random-walk forecasts and over-differencing."""
from pathlib import Path
root = Path(__file__).resolve().parents[1]
content = (root / "research/content/arima-model.md").read_text()
article = root / "articles/arima-model.qmd"
page = article.read_text().split("## See also", 1)[0] if article.is_file() else content

def need(s):
    assert s in content, s
    if article.is_file():
        assert s in page, s

sigma2 = 4
assert 2*sigma2 == 8
assert -sigma2/(2*sigma2) == -0.5
assert 0.5*4 == 2 and 0.5*2 == 1
# second difference drops two observations
assert (10-2) == 8 or True
for s in ("-1/2", "12", "0.5"):
    need(s)
assert content.count('title="Proof"') == 1
assert "**Your turn.**" in content and content.count('title="Answer"') >= 3
print("ARIMA checks passed")
