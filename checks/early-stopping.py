"""Printed values for the early-stopping article."""

from pathlib import Path

root = Path(__file__).resolve().parents[1]
page = (root / "articles" / "early-stopping.qmd").read_text(encoding="utf-8")
body = page.split("## See also", 1)[0]

train = [0.50, 0.32, 0.21, 0.14, 0.09]
val = [0.48, 0.30, 0.27, 0.29, 0.36]
assert val.index(min(val)) == 2
assert train[-1] < train[0]
second = [0.42, 0.35, 0.28, 0.33, 0.34]
assert second.index(min(second)) == 2
mono = [0.40, 0.33, 0.29, 0.27, 0.26]
assert mono.index(min(mono)) == 4
assert 0.27 < 0.29

for printed in ("0.50", "0.32", "0.21", "0.14", "0.09", "0.48", "0.30",
                "0.27", "0.29", "0.36", "0.42", "0.35", "0.28", "0.33",
                "0.40", "0.26"):
    assert printed in body, printed
assert "**Your turn.**" in body
assert body.count('collapse="true" title="Answer"') == 3
assert "## Check yourself" in body
print("early stopping checks passed")
