"""Recompute the block-rank statistic, its exact null count, and the generated article."""
import re
from itertools import permutations, product
from pathlib import Path

import numpy as np
from scipy import stats

ROOT = Path(__file__).resolve().parents[1]
scores = np.array(
    [[5, 8, 6], [4, 7, 5], [6, 9, 7], [3, 6, 4], [7, 5, 8], [4, 8, 6]],
    dtype=float,
)


def row_ranks(row):
    order = np.argsort(row, kind="mergesort")
    out = np.empty(3)
    out[order] = np.arange(1, 4)
    return out


ranks = np.vstack([row_ranks(row) for row in scores])
sums = ranks.sum(axis=0)
assert np.array_equal(sums, [7, 16, 13])
t1 = 12 / (6 * 3 * 4) * np.sum(sums ** 2) - 3 * 6 * 4
assert t1 == 7
assert abs(1 - stats.chi2.cdf(7, 2) - 0.0302) < 5e-5
assert abs(stats.chi2.ppf(0.95, 2) - 5.991) < 5e-4

perms = list(permutations((1, 2, 3)))
extreme = 0
for choice in product(range(6), repeat=6):
    total = np.zeros(3)
    for pi in choice:
        total += perms[pi]
    if np.sum((total - 12) ** 2) >= 42 - 1e-9:
        extreme += 1
assert extreme == 1350
assert extreme / 46656 == 25 / 864

t2 = (6 - 1) * 7 / (6 * 2 - 7)
assert t2 == 7
assert abs(1 - stats.f.cdf(7, 2, 10) - 0.0126) < 5e-4

changed = scores.copy()
changed[5] = [5, 4, 6]
changed_sums = np.vstack([row_ranks(row) for row in changed]).sum(axis=0)
assert np.array_equal(changed_sums, [8, 14, 14])
changed_t = 12 / (6 * 3 * 4) * np.sum(changed_sums ** 2) - 3 * 6 * 4
assert changed_t == 4

# Two treatments, every block favours the first: T1 = 4(S - b/2)^2 / b.
b, s = 6, 6
assert 4 * (s - b / 2) ** 2 / b == 6

md = (ROOT / "research" / "content" / "friedman-test.md").read_text(encoding="utf-8")
for token in ("25/864", "1350", "0.0302", "0.0126", "Your turn", "## Check yourself", "The fifth does not", "4.5"):
    assert token in md, token
assert "The sixth does not" not in md
assert "no residual" not in md
assert "Details" not in md
assert "(A_1 - C_1)/(k-1)" in md
turn = 12 / (4 * 3 * 4) * ((5 - 8) ** 2 + (8 - 8) ** 2 + (11 - 8) ** 2)
assert turn == 4.5
answers = re.findall(r'collapse="true" title="Answer"\}(.*?)(?=\n:{3,})', md, re.S)
assert len(answers) >= 4
assert all("{{cite:" not in answer for answer in answers)

page = (ROOT / "articles" / "friedman-test.qmd").read_text(encoding="utf-8")
assert "## Check yourself {#check-yourself}" in page
assert "Your turn" in page
assert page.count('class="cite-ref"') >= 5
print("friedman-test: all recomputed claims and generated-text checks passed")
