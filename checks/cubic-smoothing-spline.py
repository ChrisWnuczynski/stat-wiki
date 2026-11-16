"""Check the three-point smoothing comparison."""
from pathlib import Path
root = Path(__file__).resolve().parents[1]
body = (root / "articles/cubic-smoothing-spline.qmd").read_text().split("## See also", 1)[0]
# least squares slope is zero; RSS = 2/3; penalty of quadratic is 8; lambda = 1/12
xs = [0, 1, 2]
ys = [0, 1, 0]
mx, my = 1, 1/3
num = sum((x-mx)*(y-my) for x, y in zip(xs, ys))
den = sum((x-mx)**2 for x in xs)
assert abs(num) < 1e-12
rss = sum((y-1/3)**2 for y in ys)
assert abs(rss - 2/3) < 1e-12
assert abs((2/3)/8 - 1/12) < 1e-12
# second derivative of 2x-x^2 is -2; integral of 4 from 0 to 2 is 8
assert (-2)**2 * (2-0) == 8
for s in ("1/12", "2/3"):
    assert s in body, s
assert body.count('title="Proof"') >= 1
assert "**Your turn.**" in body and "## Check yourself" in body
assert 'data-cite-key="hastie_esl2009"' in body
print("cubic spline passed")
