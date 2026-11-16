"""Check the two-state chain arithmetic."""
from pathlib import Path
root = Path(__file__).resolve().parents[1]
content = (root / "research/content/discrete-time-markov-chain.md").read_text()
article = root / "articles/discrete-time-markov-chain.qmd"
page = article.read_text().split("## See also", 1)[0] if article.is_file() else content

def need(s):
    assert s in content, s
    if article.is_file():
        assert s in page, s

assert abs(0.8*0.2 + 0.2*0.5 - 0.26) < 1e-12
assert abs(0.5/0.7 - 5/7) < 1e-12
assert abs(0.2/0.7 - 2/7) < 1e-12
assert abs((5/7)*0.8 + (2/7)*0.5 - 5/7) < 1e-12
assert abs(0.1/0.5 - 0.2) < 1e-12
assert abs(0.6*0.6 + 0.4*0.1 - 0.40) < 1e-12
assert abs(0.5*0.5 + 0.5*0.5 - 0.5) < 1e-12
for s in ("0.26", "5/7", "2/7", "0.2", "0.40", "1/2", "0.5", "0.8"):
    need(s)
assert content.count('title="Proof"') == 1
assert "**Your turn.**" in content and 'collapse="true"' in content
assert content.count('title="Answer"') >= 3
print("discrete-time Markov chain checks passed")
