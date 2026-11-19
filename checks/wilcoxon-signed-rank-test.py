"""Recompute the signed-rank counts and inspect the generated article."""
import re
from math import comb, sqrt
from pathlib import Path

from scipy import stats

ROOT = Path(__file__).resolve().parents[1]
before = [18, 22, 19, 25, 21, 24, 20, 30]
after = [19, 24, 22, 29, 26, 30, 27, 18]
d = [a - b for a, b in zip(after, before)]
assert d == [1, 2, 3, 4, 5, 6, 7, -12]
m = 8
assert sum(range(1, m + 1)) == 36
assert m * (m + 1) // 4 == 18
assert m * (m + 1) * (2 * m + 1) == 51 * 24


def tail(threshold):
    return sum(1 for mask in range(1 << m) if sum(i + 1 for i in range(m) if mask >> i & 1) >= threshold)


assert tail(28) == 25
assert tail(36) == 1
assert 2 * tail(28) == 50
sign_tail = sum(comb(m, k) for k in range(7, 9))
assert sign_tail == 9
assert tail(35) == 2

# Your turn: +3, +1, drop 0, -2, +4. Negative rank 2, W+ = 8, three subsets of four.
turn = sum(1 for mask in range(16) if sum(i + 1 for i in range(4) if mask >> i & 1) >= 8)
assert turn == 3

z = 10 / sqrt(51)
z_c = (27.5 - 18) / sqrt(51)
assert abs(1 - stats.norm.cdf(z) - 0.0807) < 5e-4
assert abs(1 - stats.norm.cdf(z_c) - 0.0917) < 5e-4

# Walsh averages, i <= j. Median of 36 values is the average of the 18th and 19th.
vals = []
for i in range(m):
    for j in range(i, m):
        vals.append((d[i] + d[j]) / 2)
vals.sort()
assert len(vals) == 36
assert vals[17] == vals[18] == 3.5
assert vals[3] == -4.5 and vals[32] == 6.0
def at_most(limit):
    return sum(1 for mask in range(1 << m) if sum(i + 1 for i in range(m) if mask >> i & 1) <= limit)


assert at_most(3) == 5
assert at_most(4) == 7

md = (ROOT / "research" / "content" / "wilcoxon-signed-rank-test.md").read_text(encoding="utf-8")
for token in ("25/256", "9/256", "2/256", "3/16", "246/256", "Your turn", "## Check yourself"):
    assert token in md, token
assert "Details" not in md
answers = re.findall(r'collapse="true" title="Answer"\}(.*?)(?=\n:{3,})', md, re.S)
assert len(answers) >= 4
assert all("{{cite:" not in answer for answer in answers)

page = (ROOT / "articles" / "wilcoxon-signed-rank-test.qmd").read_text(encoding="utf-8")
assert "## Check yourself {#check-yourself}" in page
assert "Your turn" in page
assert page.count('class="cite-ref"') >= 5
print("wilcoxon-signed-rank-test: all recomputed claims and generated-text checks passed")
