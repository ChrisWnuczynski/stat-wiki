"""Arithmetic checks for Tukey intervals."""

import json
import re
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tools.shown import shown


from scipy.stats import studentized_range

root = Path(__file__).resolve().parents[1]
source = (root / "research/content/tukey-intervals.md").read_text(encoding="utf-8")
prose = shown(source, "tukey-intervals")
article = root / "articles/tukey-intervals.qmd"
assert article.is_file(), "generate articles before this check"
target = article.read_text(encoding="utf-8").split("## See also", 1)[0]

corn = studentized_range.ppf(0.95, 5, 10)
assert round(corn, 3) == 4.654
k, r = 3, 4
df = k * (r - 1)
assert df == 9
q = studentized_range.ppf(0.95, k, df)
assert round(q, 6) == 3.948492
half = q * (6.25 ** 0.5) / (r ** 0.5)
assert round(half, 3) == 4.936
# Rounding the quantile to three decimals before computing the width is wrong.
assert round(round(q, 3) * (6.25 / r) ** 0.5, 3) != round(half, 3)
intervals = {difference: (round(difference - half, 3), round(difference + half, 3))
             for difference in (8, 4, 6, 0)}
assert intervals == {8: (3.064, 12.936), 4: (-0.936, 8.936),
                     6: (1.064, 10.936), 0: (-4.936, 4.936)}
assert intervals[8][0] > 0 and intervals[6][0] > 0
assert intervals[4][0] < 0 < intervals[4][1]
assert intervals[0][0] < 0 < intervals[0][1]
wide = q * (25 / r) ** 0.5
assert round(wide, 3) == 9.871

questions = {item["id"]: item for item in json.loads(
    (root / "sources/depth-questions.json").read_text(encoding="utf-8"))}
selected = json.loads((root / "research/self-checks.json").read_text(encoding="utf-8"))["tukey-intervals"]
assert selected == ["depth-tukey-intervals-q1", "depth-tukey-intervals-q2"]
bank_text = "\n".join(questions[key][field] for key in selected
                      for field in ("title", "body", "answer"))
for text in (source, target, questions[selected[1]]["body"]):
    assert "$k=3$" in text and "$r=4$" in text
    assert r"$\nu=k(r-1)=9$" in text
    assert "unrounded" in text
    assert r"Q\approx 3.948492" in text
for text in (source, target, bank_text):
    for stale in ("4.041", "5.051", "2.949", "13.051", "-1.051", "9.051",
                  "0.949", "11.051", "10.103", r"\nu=8"):
        assert stale not in text, stale
for difference in (8, 4, 6):
    low, high = intervals[difference]
    assert f"({low:.3f},\\ {high:.3f})" in source
assert "approximately" in questions[selected[0]]["answer"]
assert "(-4.936,\\ 4.936)" in questions[selected[0]]["answer"]
assert r"Q\times 5/2\approx 9.871" in questions[selected[1]]["answer"]
assert "5% marginal noncoverage" in source and "need not be independent" in source

for printed in ("3.948492", "4.936", "3.064", "12.936", "-0.936", "8.936",
                "1.064", "10.936", "9.871", "6.25"):
    assert printed in target, printed
assert 'title="Proof"' in prose and "**Your turn.**" in prose
assert prose.count('title="Answer"') >= 3
answer_blocks = re.findall(r'::: \{\.callout-tip collapse="true" title="Answer"\}\n(.*?)\n:::',
                          target, flags=re.S)
assert len(answer_blocks) == 3
assert all("{{cite:" not in answer and 'class="cite-ref"' not in answer
           for answer in answer_blocks)
print("tukey-intervals checks passed")
