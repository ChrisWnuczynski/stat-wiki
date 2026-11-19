"""Recompute W from the 1965 coefficients and inspect the generated article."""
import re
from pathlib import Path

import numpy as np
from scipy import stats

ROOT = Path(__file__).resolve().parents[1]
x = np.array([2.0, 2.2, 2.5, 2.7, 3.1, 3.4, 4.0, 8.5])
a = np.array([0.6052, 0.3164, 0.1743, 0.0561])
ordered = np.sort(x)
gaps = ordered[::-1][:4] - ordered[:4]
assert np.allclose(gaps, [6.5, 1.8, 0.9, 0.4])
b = float(a @ gaps)
s2 = float(np.sum((x - x.mean()) ** 2))
w = b ** 2 / s2
assert abs(b - 4.68263) < 1e-9
assert abs(s2 - 30.98) < 1e-9
assert abs(w - 0.70778) < 5e-6
raw = stats.shapiro(x)
assert abs(raw.statistic - 0.70772) < 5e-5
assert abs(raw.pvalue - 0.002753) < 5e-6

logs = np.log(x)
lgaps = np.sort(logs)[::-1][:4] - np.sort(logs)[:4]
lb = float(a @ lgaps)
ls2 = float(np.sum((logs - logs.mean()) ** 2))
lw = lb ** 2 / ls2
assert abs(lb - 1.12618) < 5e-5
assert abs(ls2 - 1.45981) < 5e-5
assert abs(lw - 0.86879) < 5e-5
logged = stats.shapiro(logs)
assert abs(logged.statistic - 0.86886) < 5e-5
assert abs(logged.pvalue - 0.1469) < 5e-4

# Table 6, 5% points used for the "same W, different n" comparison.
assert 0.85 > 0.818 and 0.85 < 0.905
from scipy.stats import norm
qsteps = np.diff(norm.ppf((np.arange(1, 9) - 0.5) / 8))
assert abs(qsteps[-2] - 0.398) < 5e-4
assert abs(qsteps[-1] - 0.647) < 5e-4
assert abs((8.5 - 4.0) / (4.0 - 3.4) - 7.5) < 1e-9
assert abs(qsteps[-1] / qsteps[-2] - 1.62) < 5e-3
assert abs(x.mean() - 3.55) < 1e-12

md = (ROOT / "research" / "content" / "shapiro-wilk-test.md").read_text(encoding="utf-8")
for token in ("0.70778", "0.818", "0.86879", "0.905", "3.55", "0.647", "Your turn", "## Check yourself", "razali_wah2011"):
    assert token in md, token
assert "3.675" not in md
assert "Details" not in md
answers = re.findall(r'collapse="true" title="Answer"\}(.*?)(?=\n:{3,})', md, re.S)
assert len(answers) >= 4
assert all("{{cite:" not in answer for answer in answers)

page = (ROOT / "articles" / "shapiro-wilk-test.qmd").read_text(encoding="utf-8")
assert "## Check yourself {#check-yourself}" in page
assert "Your turn" in page
assert page.count('class="cite-ref"') >= 5
print("shapiro-wilk-test: all recomputed claims and generated-text checks passed")
