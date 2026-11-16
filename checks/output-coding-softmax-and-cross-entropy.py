"""Check softmax probabilities, cross-entropy, and the two-class reduction."""
from pathlib import Path
import math

root = Path(__file__).resolve().parents[1]
page = (root / "articles/output-coding-softmax-and-cross-entropy.qmd").read_text()
body = page.split("## See also", 1)[0]

def softmax(z):
    m = max(z)
    e = [math.exp(v - m) for v in z]
    s = sum(e)
    return [v / s for v in e]

p = softmax([0, 1, -1])
assert [f"{v:.4f}" for v in p] == ["0.2447", "0.6652", "0.0900"]
assert f"{-math.log(p[1]):.4f}" == "0.4076"
q = softmax([2, 1, 0.1])
assert [f"{v:.3f}" for v in q] == ["0.659", "0.242", "0.099"]
assert f"{-math.log(q[0]):.3f}" == "0.417"
sig = 1 / (1 + math.exp(-1))
assert f"{sig:.4f}" == "0.7311"
assert f"{-math.log(sig):.4f}" == "0.3133"
assert f"{sig - 1:.4f}" == "-0.2689"
assert abs(math.exp(2) + math.exp(1) + math.exp(0.1) - (math.exp(2+5)+math.exp(1+5)+math.exp(0.1+5))/math.exp(5)) < 1e-9

for printed in ("0.2447", "0.6652", "0.0900", "0.4076", "0.659", "0.242", "0.099",
                "0.417", "0.7311", "0.3133", "-0.2689"):
    assert printed in body, printed
assert body.count('title="Proof"') == 1
assert "**Your turn.**" in body and "## Check yourself" in body
assert body.count('title="Answer"') >= 4
for key in ("hastie_esl2009", "shannon1948"):
    assert f'data-cite-key="{key}"' in body
print("softmax values and practice passed")
