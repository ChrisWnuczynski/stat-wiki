"""Check scatterplot example arithmetic and baseline preservation."""

import json
import math
from pathlib import Path

root = Path(__file__).resolve().parents[1]
page = (root / "articles/scatterplot.qmd").read_text()
body = page.split("## See also", 1)[0]
pending = json.loads((root / "research/pending/scatterplot.json").read_text())


def sums(xs, ys):
    mx = sum(xs) / len(xs)
    my = sum(ys) / len(ys)
    cross = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    sx = sum((x - mx) ** 2 for x in xs)
    sy = sum((y - my) ** 2 for y in ys)
    return mx, my, cross, sx, sy, cross / math.sqrt(sx * sy)


assert sums([-2, -1, 0, 1, 2], [4, 1, 0, 1, 4]) == (0, 2, 0, 10, 14, 0)
assert sums([1, 2, 3, 4, 5], [3, 5, 7, 9, 11]) == (3, 7, 20, 10, 40, 1)
changed = sums([1, 2, 3, 4, 5], [3, 5, 7, 9, 21])
assert changed[:5] == (3, 9, 40, 10, 200)
assert round(changed[5], 4) == 0.8944
assert sums([1, 2, 3, 4, 5], [1, 4, 9, 16, 25])[:2] == (3, 11)
for printed in ("-2,-1,0,1,2", "4,1,0,1,4", "-4+1+0-1+4=0", "10", "14", "20", "40", "200", "0.8944", "21", "11"):
    assert printed in body, printed
assert body.count('title="Proof"') == 1
assert "## Motivating example" in body and "## Worked example" in body
assert "**Your turn.**" in body and 'title="Answer"' in body
assert page.count("![") >= json.loads((root / "research/baseline.json").read_text())["scatterplot"]["figures"]
for key in ("dodge2008", "nist_scatterplot2002"):
    assert f'data-cite-key="{key}"' in body, key
for unread in ("galton1886", "chambers1983_gmda", "wasserman2004"):
    assert f'data-cite-key="{unread}"' not in body
assert "ex-fish-poisson.qmd" in page
assert pending["self_checks"] == ["ex-da-correlation-reading", "depth-scatterplot-curve", "depth-scatterplot-overplotting"]
assert "## Worked answer" in (root / "questions/ex-da-correlation-reading.qmd").read_text()
assert len(pending["new_bank_questions"]) == 2
assert all(q["answer"] and q["topic_code"] == "D2" for q in pending["new_bank_questions"])
print("scatterplot arithmetic and preservation passed")
