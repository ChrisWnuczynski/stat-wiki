"""Check quartile interpolation, fences and scale comparisons."""

import math
import re
from pathlib import Path
from scipy.stats import norm

root = Path(__file__).resolve().parents[1]
page = (root / "articles/interquartile-range.qmd").read_text()
body = page.split("## See also", 1)[0]

def quantile(values, p):
    n = len(values)
    h = 1 + (n - 1) * p
    j = math.floor(h)
    g = h - j
    if g == 0:
        return values[j - 1]
    return (1 - g) * values[j - 1] + g * values[j]

sample = [1, 2, 3, 4, 5, 6, 7, 8, 9, 100]
q1, q3 = quantile(sample, 0.25), quantile(sample, 0.75)
assert (q1, q3, q3 - q1) == (3.25, 7.75, 4.5)
assert q3 + 1.5 * (q3 - q1) == 14.5
clean = list(range(1, 10))
assert (quantile(clean, 0.25), quantile(clean, 0.75)) == (3, 7)
assert sum(sample) / 10 == 14.5
sd = math.sqrt(sum((v - 14.5) ** 2 for v in sample) / 9)
assert round(sd, 3) == 30.152
sd9 = math.sqrt(7.5)
assert round(sd9, 3) == 2.739
assert round(sd - sd9, 3) == 27.414
assert round(sd / 4.5, 3) == 6.701
z = norm.ppf(0.75)
assert round(z, 5) == 0.67449
assert round(2 * z, 3) == 1.349
normal_sd_iqr = 1 / (2 * z)
assert round(normal_sd_iqr, 4) == 0.7413

# Bind both comparison values to SD/IQR in the benchmark section itself.
# Numbers elsewhere on the page cannot rescue a reciprocal or partial fix.
benchmark = re.search(
    r"(?ms)^## A fence and a normal benchmark[^\n]*\n(.*?)(?=^## |\Z)", body
)
assert benchmark, "missing normal-benchmark section"
equations = {
    re.sub(r"\s+", "", equation)
    for equation in re.findall(r"\$([^$\n]+)\$", benchmark.group(1))
}
for equation in (
    rf"\mathrm{{SD}}/\mathrm{{IQR}}\approx{sd:.5f}/4.5\approx{sd / 4.5:.3f}",
    r"\mathrm{SD}/\mathrm{IQR}=\frac{1}{2\Phi^{-1}(0.75)}\approx"
    f"{normal_sd_iqr:.4f}",
    r"\mathrm{IQR}/\mathrm{SD}=2\Phi^{-1}(0.75)\approx2\times"
    f"{z:.5f}" + r"\approx" + f"{2 * z:.3f}",
):
    assert equation in equations, f"missing or inconsistent scale ratio: {equation}"
assert "interquartile range is many times its standard deviation" not in body
assert "Heavy tails show up when" not in body

five = [1, 2, 3, 10, 11]
assert quantile(five, 0.25) == 2 and quantile(five, 0.5) == 3 and quantile(five, 0.75) == 10
assert (10 - 2) == 8 and 2 * (10 - 3) == 14
tiny = [0, 0, 100]
assert quantile(tiny, 0.25) == 0 and quantile(tiny, 0.75) == 50
assert quantile([2, 2, 5, 8, 8], 0.25) == 2
assert quantile([2, 2, 5, 8, 8], 0.75) == 8

for printed in (
    "3.25", "7.75", "4.5", "14.5", "30.152", "2.739", "27.414",
    "0.67449", "1.349", "98.5", "2.15", "6.701", "0.5",
):
    assert printed in body, printed
assert body.count('title="Proof"') == 1
assert "**Your turn.**" in body and "## Check yourself" in body
assert body.count('title="Answer"') >= 3
for qid in ("ex-da-nutrition-types", "ex-inf-milk-summaries"):
    assert f"../questions/{qid}.qmd" in page
for key in ("nist_handbook2002", "dodge2008"):
    assert f'data-cite-key="{key}"' in body
print("interquartile range checks passed")
