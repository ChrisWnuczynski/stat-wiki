"""Arithmetic for the baseline-category logit depth pass."""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tools.shown import shown
from math import exp

root = Path(__file__).resolve().parents[1]
prose = (root / "research/content/baseline-category-logit-model.md").read_text(encoding="utf-8")
prose = shown(prose, "baseline-category-logit-model")
page = root / "articles/baseline-category-logit-model.qmd"
assert page.is_file(), "generate articles before this check"
body = page.read_text(encoding="utf-8").split("## See also", 1)[0]

e1, e2 = exp(0.5), exp(1.0)
den = 1 + e1 + e2
ps = [1 / den, e1 / den, e2 / den]
assert abs(sum(ps) - 1) < 1e-12
assert abs(e1 - 1.6487212707001282) < 1e-12
assert round(e1, 4) == 1.6487
assert round(e2, 4) == 2.7183
assert round(den, 4) == 5.3670
assert [round(p, 4) for p in ps] == [0.1863, 0.3072, 0.5065]
assert abs(ps[2] / ps[1] - e1) < 1e-12
assert round(0.1863 + 0.3072 + 0.5065, 4) == 1.0
assert [1 / 5, 1 / 5, 3 / 5] == [0.2, 0.2, 0.6]

for printed in ("1.6487", "2.7183", "5.3670", "0.1863", "0.3072", "0.5065", "0.2", "0.6"):
    assert printed in prose, printed
    assert printed in body, printed
assert prose.count('title="Proof"') == 1
assert "**Your turn.**" in prose and "## Check yourself" in prose
assert prose.count('title="Answer"') == 4
assert "{{cite:hastie_esl2009}}" in prose
print("baseline-category-logit-model arithmetic passed")
