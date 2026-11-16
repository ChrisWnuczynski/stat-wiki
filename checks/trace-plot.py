"""Check Gelman–Rubin variance split on two short sequences."""
import math
from pathlib import Path
root = Path(__file__).resolve().parents[1]
body = (root / "articles/trace-plot.qmd").read_text().split("## See also", 1)[0]

def within(xs):
    m = sum(xs)/len(xs)
    return sum((x-m)**2 for x in xs)/(len(xs)-1), m

w1, m1 = within([0,1,0,1])
w2, m2 = within([5,6,5,6])
assert abs(w1 - 1/3) < 1e-12 and abs(w2 - 1/3) < 1e-12
assert m1 == 0.5 and m2 == 5.5
W = (w1+w2)/2
B_over_n = ((m1-3)**2 + (m2-3)**2)/1
assert B_over_n == 12.5
n = 4
B = B_over_n * n
sigma2 = ((n-1)/n)*W + B/n
assert abs(sigma2 - 12.75) < 1e-12
ratio = sigma2 / W
assert abs(ratio - 38.25) < 1e-12
assert abs(math.sqrt(ratio) - 6.185) < 5e-4
# agreeing chains
w, m = within([1,2,1,2])
assert m == 1.5 and abs(w - 1/3) < 1e-12
sigma_agree = ((n-1)/n)*w
assert abs(sigma_agree - 0.25) < 1e-12
assert abs(sigma_agree/w - 0.75) < 1e-12
# your turn
w_a, m_a = within([2,2,2,2])
w_b, m_b = within([2,4,2,4])
assert m_a == 2 and m_b == 3 and w_a == 0
assert abs(w_b - 4/3) < 1e-12
W2 = (w_a+w_b)/2
assert abs(W2 - 2/3) < 1e-12
B2 = ((m_a-2.5)**2 + (m_b-2.5)**2)
assert abs(B2 - 0.5) < 1e-12
# identity
assert abs((sigma2 - W) - (B - W)/n) < 1e-12
for s in ("12.75", "6.185", "12.5", "0.25"):
    assert s in body, s
assert body.count('title="Proof"') == 1
assert "**Your turn.**" in body and "## Check yourself" in body
assert 'data-cite-key="gelman_rubin1992"' in body
print("trace plot passed")
