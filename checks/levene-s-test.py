"""Recompute the absolute-deviation F ratios and inspect the generated article."""
import re
from pathlib import Path

import numpy as np
from scipy import stats

ROOT = Path(__file__).resolve().parents[1]
groups = [np.array([3.0, 5, 7]), np.array([2.0, 4, 6]), np.array([0.0, 2, 13])]


def levene_f(samples, centre):
    z_groups = []
    for sample in samples:
        c = float(centre(sample))
        z_groups.append(np.abs(sample - c))
    means = np.array([z.mean() for z in z_groups])
    grand = np.concatenate(z_groups).mean()
    ssb = sum(len(z) * (m - grand) ** 2 for z, m in zip(z_groups, means))
    ssw = sum(np.sum((z - m) ** 2) for z, m in zip(z_groups, means))
    return (ssb / 2) / (ssw / 6), ssb, ssw


mean_f, ssb, ssw = levene_f(groups, np.mean)
med_f, msb, msw = levene_f(groups, np.median)
assert abs(ssb - 32) < 1e-9 and abs(ssw - 18) < 1e-9
assert abs(mean_f - 16 / 3) < 1e-9
assert abs(msb - 18) < 1e-9 and abs(msw - 74) < 1e-9
assert abs(med_f - 27 / 37) < 1e-9
crit = stats.f.ppf(0.95, 2, 6)
assert abs(crit - 5.14325) < 1e-4
assert mean_f > crit > med_f
assert abs(1 - stats.f.cdf(mean_f, 2, 6) - 0.0467) < 5e-4
assert abs(1 - stats.f.cdf(med_f, 2, 6) - 0.520) < 5e-3
soft = stats.levene(*groups, center="mean")
hard = stats.levene(*groups, center="median")
assert abs(soft.statistic - 16 / 3) < 1e-9
assert abs(hard.statistic - 27 / 37) < 1e-9

replaced = [groups[0], groups[1], np.array([0.0, 2, 4])]
zero_f, _, _ = levene_f(replaced, np.mean)
assert zero_f == 0

md = (ROOT / "research" / "content" / "levene-s-test.md").read_text(encoding="utf-8")
for token in ("16/3", "27/37", "5.143", "Your turn", "## Check yourself"):
    assert token in md, token
answers = re.findall(r'collapse="true" title="Answer"\}(.*?)(?=\n:{3,})', md, re.S)
assert len(answers) >= 4
assert all("{{cite:" not in answer for answer in answers)

page = (ROOT / "articles" / "levene-s-test.qmd").read_text(encoding="utf-8")
assert "## Check yourself {#check-yourself}" in page
assert "Your turn" in page
assert page.count('class="cite-ref"') >= 5
print("levene-s-test: all recomputed claims and generated-text checks passed")
