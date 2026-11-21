"""Arithmetic for the baseline-category logit depth pass."""

import sys
import json
import re
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

# The independent exercise must not repeat the visible worked scores or odds.
questions = json.loads((root / "sources/depth-questions.json").read_text(encoding="utf-8"))
question = next(q for q in questions if q["id"] == "depth-baseline-category-logit-model-q2")
scores = dict((int(k), float(v)) for k, v in re.findall(r"\\eta_([012])=([0-9.]+)", question["body"]))
assert [scores[k] for k in range(3)] == [0, 0.3, 1.2]
normalizer = sum(exp(scores[k]) for k in range(3))
exercise_odds = (exp(scores[2]) / normalizer) / (exp(scores[1]) / normalizer)
assert abs(exercise_odds - exp(scores[2] - scores[1])) < 1e-12
assert round(exercise_odds, 6) == 2.459603
assert "e^{0.9}\\approx 2.459603" in question["answer"]
assert "denominator cancels" in question["answer"]
assert "2.459603" in prose and "2.459603" in body
authored = (root / "research/content/baseline-category-logit-model.md").read_text(encoding="utf-8")
assert "2.459603" not in authored and "\\eta_1=0.3" not in authored
assert 1e-6 < abs(0.5065 / 0.3072 - exp(0.5)) < 5e-5
assert "$0.5065/0.3072$ is only an approximation" in authored
print("baseline-category-logit-model arithmetic passed")
