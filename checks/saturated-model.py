"""Verify all new numeric claims and retained links on saturated model."""

import json
import math
from pathlib import Path

root = Path(__file__).resolve().parents[1]
page = (root / "articles/saturated-model.qmd").read_text()
body = page.split("## See also", 1)[0]
pending = {'self_checks': json.loads((root / 'research/self-checks.json').read_text())['saturated-model']}

def poisson_d(y, mu):
    return 2 * (y * math.log(y / mu) - (y - mu)) if y else 2 * mu

assert [poisson_d(y, 2) for y in (0, 2, 4)] == [4, 0, 8 * math.log(2) - 4]
assert round(sum(poisson_d(y, 2) for y in (0, 2, 4)), 4) == 5.5452
assert round(poisson_d(4, 2), 4) == 1.5452
assert round(poisson_d(1, 2), 4) == .6137
assert round(poisson_d(3, 2), 4) == .4328
assert round(poisson_d(1, 2) + poisson_d(3, 2), 4) == 1.0465
for printed in ("(0,2,4)", "(1,3)", "5.5452", "1.5452", "0.6137", "0.4328", "1.0465"):
    assert printed in body, printed
assert body.count('title="Proof"') == 1
assert "## Motivating example" in body and "## Worked example" in body
assert "**Your turn.**" in body and 'title="Answer"' in body
assert pending["self_checks"] == ["q-34", "c-29"]
for q in pending["self_checks"]:
    assert (root / "questions" / f"{q}.qmd").exists()
for q in ("q-34", "ex-fish-poisson", "c-29"):
    assert f"../questions/{q}.qmd" in page
for source in ("nelder_wedderburn1972", "rstats_glm2026", "rstats_family2026"):
    assert f'data-cite-key="{source}"' in body
assert json.loads((root / "research/baseline.json").read_text())["saturated-model"]["figures"] == 0
print("saturated-model calculations and preservation passed")
