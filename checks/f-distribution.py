"""Check F means, mode and variance."""
from pathlib import Path
root = Path(__file__).resolve().parents[1]
content = (root / "research/content/f-distribution.md").read_text()
article = root / "articles/f-distribution.qmd"
page = article.read_text().split("## See also", 1)[0] if article.is_file() else content

def need(s):
    assert s in content, s
    if article.is_file():
        assert s in page, s

mean = 20/(20-2)
mode = 20*(8-2)/(8*(20+2))
recip = 8/(8-2)
assert abs(mean - 10/9) < 1e-12 and round(mean, 3) == 1.111
assert mode == 15/22 and round(mode, 3) == 0.682
assert recip == 4/3 and round(recip, 3) == 1.333
assert abs(1/1.111 - 0.900) < 0.001
var = 2*36*(4+6-2)/(4*(6-2)**2*(6-4))
assert var == 4.5 and 6/(6-2) == 1.5
assert 4/(4-2) == 2 and 5/(5-2) == 5/3 and round(5/3, 3) == 1.667
for s in ("1.111", "0.682", "1.333", "1.5", "4.5", "1.667", "15/22", "10/9"):
    need(s)
assert content.count('title="Proof"') == 1
assert "**Your turn.**" in content and content.count('title="Answer"') >= 3
print("F distribution checks passed")
