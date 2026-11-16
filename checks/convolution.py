"""Arithmetic checks for the convolution article."""
from pathlib import Path

root = Path(__file__).resolve().parents[1]
text = (root / "research/content/convolution.md").read_text()
body = (root / "articles/convolution.qmd").read_text().split("## See also", 1)[0]
assert 6 / 36 == 1 / 6
assert 4 / 36 == 1 / 9
assert 1 / 36 == 1 / 36
# overlap length of two unit intervals at sum 1.5
assert min(1, 1.5) - max(0, 0.5) == 0.5
for printed in ("6/36", "1/6", "1/36", "4/36", "1/9", "0.5"):
    assert printed in text, printed
    assert printed in body, printed
assert "**Your turn.**" in body and 'title="Proof"' in body
print("convolution checks passed")
