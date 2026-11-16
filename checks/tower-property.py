"""Printed values for the tower-property article."""

from pathlib import Path

root = Path(__file__).resolve().parents[1]
page = (root / "articles" / "tower-property.qmd").read_text(encoding="utf-8")
body = page.split("## See also", 1)[0]

p = {(0, 1): 0.2, (0, 2): 0.3, (1, 1): 0.4, (1, 2): 0.1}
assert abs(sum(p.values()) - 1) < 1e-12
ey0 = (0.2 * 1 + 0.3 * 2) / 0.5
ey1 = (0.4 * 1 + 0.1 * 2) / 0.5
assert abs(ey0 - 1.6) < 1e-12 and abs(ey1 - 1.2) < 1e-12
assert abs(ey0 * 0.5 + ey1 * 0.5 - 1.4) < 1e-12
assert abs(1 * (0.2 + 0.4) + 2 * (0.3 + 0.1) - 1.4) < 1e-12
ey2_0 = (0.2 * 1 + 0.3 * 4) / 0.5
ey2_1 = (0.4 * 1 + 0.1 * 4) / 0.5
assert abs(ey2_0 - 2.8) < 1e-12 and abs(ey2_1 - 1.6) < 1e-12
assert abs(ey2_0 * 0.5 + ey2_1 * 0.5 - 2.2) < 1e-12
assert abs(1 * (0.2 + 0.4) + 4 * (0.3 + 0.1) - 2.2) < 1e-12
assert 0 * 0.5 + 1 * 0.5 == 0.5
assert 1 * 0.6 + 2 * 0.4 == 1.4

for printed in ("1.6", "1.2", "1.4", "2.8", "2.2", "0.5", "0.6", "0.4"):
    assert printed in body, printed
assert 'title="Proof"' in body
assert "**Your turn.**" in body
assert body.count('collapse="true" title="Answer"') >= 3
print("tower property checks passed")
