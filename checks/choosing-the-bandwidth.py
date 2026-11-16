"""Check bandwidth selection calculations and preservation of the source page."""

import json
import math
from pathlib import Path

root = Path(__file__).resolve().parents[1]
page = (root / "articles/choosing-the-bandwidth.qmd").read_text()
body = page.split("## See also", 1)[0]
pending = json.loads((root / "research/pending/choosing-the-bandwidth.json").read_text())


def kernel(u):
    return math.exp(-u * u / 2) / math.sqrt(2 * math.pi)


def loo(data, h):
    densities = [sum(kernel((x - y) / h) for j, y in enumerate(data) if j != i) / ((len(data) - 1) * h) for i, x in enumerate(data)]
    return densities, sum(math.log(v) for v in densities) / len(densities)


data = (0, 1, 2)
expected = {
    0.5: (0.054125, 0.107982, -2.686239),
    1: (0.147981, 0.241971, -1.746761),
    2: (0.148509, 0.176033, -1.850435),
}
for h, (endpoint, middle, score) in expected.items():
    densities, actual_score = loo(data, h)
    assert round(densities[0], 6) == endpoint
    assert round(densities[1], 6) == middle
    assert round(densities[2], 6) == endpoint
    assert round(actual_score, 6) == score
    for printed in (str(h), f"{endpoint:.6f}", f"{middle:.6f}", f"{score:.6f}"):
        assert printed in body, printed

for h, printed in ((1, "-3.379386"), (2, "-2.439908")):
    _, scaled_score = loo((0, 2, 4), h)
    assert round(scaled_score, 6) == float(printed)
    assert printed in body
    _, original_score = loo(data, h / 2)
    assert math.isclose(scaled_score, original_score - math.log(2))

for n in (10, 100, 1000):
    A, B = 3.0, 5.0
    optimal = (B / (4 * A * n)) ** (1 / 5)
    derivative = 4 * A * optimal**3 - B / (n * optimal**2)
    assert math.isclose(derivative, 0, abs_tol=1e-12)
assert math.isclose((1000 / 10) ** (-1 / 5), 100 ** (-1 / 5))
assert 3 * (3 + 1) / 2 == 6
for literal in ("$p(p+1)/2$", "$n^{-1/5}$", "$n^{-4/5}$", "1956", "1962", "h=0.5", "h=1", "h=2"):
    assert literal in body, literal

assert body.count('title="Proof"') == 1
assert "## Motivating example" in body and "## Worked example" in body
assert "**Your turn.**" in body and 'title="Answer"' in body
assert page.count("![") >= json.loads((root / "research/baseline.json").read_text())["choosing-the-bandwidth"]["figures"]
for key in ("silverman1986", "wasserman_lecture26", "hansen_larsson2026_density", "rstats_bandwidth2026"):
    assert f'data-cite-key="{key}"' in body, key
for unread in ("rosenblatt1956", "parzen1962"):
    assert f'data-cite-key="{unread}"' not in body
assert pending["self_checks"] == ["ex-sl-07-3", "ex-sl-07-4", "ex-sl-07-6"]
for slug in pending["self_checks"]:
    assert "## Worked answer" in (root / "questions" / f"{slug}.qmd").read_text()
    assert f"{slug}.qmd" in page
print("bandwidth CV arithmetic, AMISE algebra and preservation passed")
