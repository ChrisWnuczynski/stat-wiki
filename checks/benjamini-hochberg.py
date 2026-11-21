"""Checks for the Benjamini–Hochberg article."""

import sys
import json
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tools.shown import shown


import numpy as np

root = Path(__file__).resolve().parents[1]
prose = (root / "research/content/benjamini-hochberg.md").read_text(encoding="utf-8")
prose = shown(prose, "benjamini-hochberg")
article = root / "articles/benjamini-hochberg.qmd"
target = article.read_text(encoding="utf-8").split("## See also", 1)[0] if article.is_file() else prose

def largest(ps, q):
    ps = np.asarray(ps, dtype=float)
    thr = np.arange(1, len(ps) + 1) * q / len(ps)
    ok = np.where(ps <= thr + 1e-15)[0]
    strict = np.where(ps < thr - 1e-15)[0]
    return (int(ok.max()) + 1 if len(ok) else 0,
            int(strict.max()) + 1 if len(strict) else 0,
            thr)

ps = [0.001, 0.012, 0.020, 0.039, 0.30]
k_closed, k_strict, thr = largest(ps, 0.05)
assert np.allclose(thr, [0.01, 0.02, 0.03, 0.04, 0.05])
assert k_closed == 4 and k_strict == 4
k2, _, thr2 = largest(ps, 0.02)
assert np.allclose(thr2, [0.004, 0.008, 0.012, 0.016, 0.020])
assert k2 == 1
tie = [0.001, 0.012, 0.030, 0.20, 0.40]
assert largest(tie, 0.05)[:2] == (3, 2)
assert largest([0.04, 0.20, 0.30, 0.40, 0.50], 0.05)[0] == 0

# A failed first comparison does not stop a step-up procedure.
step_up = [0.015, 0.019, 0.30, 0.40, 0.50]
closed, strict, thresholds = largest(step_up, 0.05)
assert step_up[0] > thresholds[0] and step_up[1] < thresholds[1]
assert closed == strict == 2
none = np.asarray([0.04, 0.20, 0.30, 0.40, 0.50])
assert np.all(none > thresholds)
questions = {q["id"]: q for q in json.loads((root / "sources/depth-questions.json").read_text(encoding="utf-8"))}
q1 = questions["depth-benjamini-hochberg-q1"]
q2 = questions["depth-benjamini-hochberg-q2"]
assert r"q^*=\alpha=0.05" in q1["body"]
assert "$k=3$" in q1["answer"] and "$k=2$" in q1["answer"]
for comparison in ("0.04>0.01", "0.20>0.02", "0.30>0.03", "0.40>0.04", "0.50>0.05"):
    assert comparison in q2["answer"], comparison
assert "$k=0$" in q2["answer"]
assert "earlier failed comparison can still be included if a later comparison succeeds" in q2["answer"]
assert "No later comparison can create an earlier success" not in q2["answer"]

for printed in ("0.001", "0.012", "0.039", "0.30", "0.01", "0.04", "0.004", "0.008"):
    assert printed in target, printed
assert "**Your turn.**" in prose and prose.count('title="Answer"') >= 3
assert r"q^*=\alpha=0.05" in target
assert "0.50>0.05" in target and "earlier failed comparison" in target
print("benjamini-hochberg checks passed")
