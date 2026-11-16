"""Verify contrast weights, worked arithmetic, and preserved corn examples."""

import json
import math
from pathlib import Path

from scipy.stats import f

root = Path(__file__).resolve().parents[1]
page = (root / "articles/contrast.qmd").read_text()
body = page.split("## See also", 1)[0]
pending = json.loads((root / "research/pending/contrast.json").read_text())


def estimate(means, weights, ns, mse):
    assert sum(weights) == 0
    c = sum(a * m for a, m in zip(weights, means))
    multiplier = sum(a * a / n for a, n in zip(weights, ns))
    se = math.sqrt(mse * multiplier)
    return c, multiplier, se, c / se


means = [48.93, 55.07, 59.80, 48.30, 51.93]
c, mult, se, t = estimate(means, [0.25, 0.25, -1, 0.25, 0.25], [3] * 5, 10.57)
assert math.isclose(c, -8.7425) and math.isclose(mult, 5 / 12)
assert round(t * t, 1) == 17.4 and round(f.sf(t * t, 1, 10), 3) == 0.002
c2, m2, _, t2 = estimate(means, [-0.5, 1, 0, -0.5, 0], [3] * 5, 10.57)
assert math.isclose(c2, 6.455) and m2 == 0.5
assert round(t2 * t2, 2) == 7.88 and round(f.sf(t2 * t2, 1, 10), 3) == 0.019
c3, m3, se3, t3 = estimate([12, 15, 18], [-0.5, -0.5, 1], [4] * 3, 9)
assert (c3, m3) == (4.5, 0.375)
assert round(se3, 4) == 1.8371 and round(t3, 4) == 2.4495
assert round(t3 * t3, 4) == 6 and 12 - 3 == 9
c4, m4, se4, t4 = estimate([12, 15, 18], [-1, 1, 0], [4] * 3, 9)
assert (c4, m4) == (3, 0.5)
assert round(se4, 4) == 2.1213 and round(t4, 4) == 1.4142
for printed in ("48.93", "55.07", "59.80", "48.30", "51.93", "-8.74", "0.4167", "17.4", "0.002", "6.45", "83.2", "7.87", "0.019", "12", "15", "18", "4.5", "0.375", "1.8371", "2.4495", "1.4142", "2.1213"):
    assert printed in body, printed
assert body.count('title="Proof"') == 1
assert "## Motivating example" in body and "## Worked example" in body
assert "**Your turn.**" in body and 'title="Answer"' in body
assert "ex-inf-corn-contrast.qmd" in page and "ex-inf-contrast-cell.qmd" in page
assert page.count("![") >= json.loads((root / "research/baseline.json").read_text())["contrast"]["figures"]
for key in ("nist_contrasts2002", "nist_scheffe2002", "dodge2008", "scheffe1959", "tukey1949"):
    assert f'data-cite-key="{key}"' in body, key
assert pending["self_checks"] == ["ex-inf-corn-contrast", "ex-inf-anova-two-groups"]
for slug in pending["self_checks"]:
    assert "## Worked answer" in (root / "questions" / f"{slug}.qmd").read_text()
print("contrast arithmetic and preservation passed")
