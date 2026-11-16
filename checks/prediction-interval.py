"""Arithmetic checks for the prediction interval article."""
import math
from pathlib import Path
from scipy.stats import t

root = Path(__file__).resolve().parents[1]
text = (root / "research/content/prediction-interval.md").read_text()
page = (root / "articles/prediction-interval.qmd").read_text()
body = page.split("## See also", 1)[0]

n, s, x0, xbar, sxx, yhat = 11, 1.5, 8, 5, 110, 12
inside = 1 + 1 / n + (x0 - xbar) ** 2 / sxx
se = s * math.sqrt(inside)
tq = t.ppf(0.975, n - 2)
margin = tq * se
assert round(inside, 5) == 1.17273
assert round(se, 5) == 1.62439
assert round(tq, 5) == 2.26216
assert round(margin, 5) == 3.67462
assert round(yhat - margin, 3) == 8.325
assert round(yhat + margin, 3) == 15.675
se_mean = s * math.sqrt(1 / n + (x0 - xbar) ** 2 / sxx)
assert round(se_mean, 5) == 0.62341
assert round(tq * se_mean, 3) == 1.410
se_c = s * math.sqrt(1 + 1 / n)
assert round(se_c, 5) == 1.56670
assert round(tq * se_c, 5) == 3.54412
assert round(1.96 * 2, 2) == 3.92
assert (round(10 - 3.92, 2), round(10 + 3.92, 2)) == (6.08, 13.92)
for printed in ("1.17273", "1.62439", "2.26216", "3.67462", "8.325", "15.675",
                "0.62341", "1.410", "1.09091", "1.56670", "3.54412", "3.92",
                "6.08", "13.92", "10.590", "13.410"):
    assert printed in text, printed
    assert printed in body, printed
assert "**Your turn.**" in body and body.count('title="Answer"') >= 3
print("prediction interval checks passed")
