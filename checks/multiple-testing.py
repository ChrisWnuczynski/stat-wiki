"""Arithmetic checks for the multiple-testing article."""
from pathlib import Path

root = Path(__file__).resolve().parents[1]
text = (root / "research/content/multiple-testing.md").read_text()
body = (root / "articles/multiple-testing.qmd").read_text().split("## See also", 1)[0]
assert round(1 - 0.95 ** 20, 4) == 0.6415
assert round(0.95 ** 5, 5) == 0.77378
assert round(1 - 0.95 ** 5, 5) == 0.22622
ps = [0.004, 0.018, 0.040, 0.200]
thr = [0.10 * k / 4 for k in range(1, 5)]
assert [round(t, 3) for t in thr] == [0.025, 0.050, 0.075, 0.100]
k = max((i for i, (p, t) in enumerate(zip(ps, thr), 1) if p <= t), default=0)
assert k == 3
assert abs(0.10 / 4 - 0.025) < 1e-12
assert abs(0.05 / 20 - 0.0025) < 1e-12
for printed in ("0.6415", "0.77378", "0.22622", "0.004", "0.018", "0.040",
                "0.200", "0.025", "0.050", "0.075", "0.100", "0.0025"):
    assert printed in text, printed
    assert printed in body, printed
assert "**Your turn.**" in body and 'title="Proof"' in body
print("multiple testing checks passed")
