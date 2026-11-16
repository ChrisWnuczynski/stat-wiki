"""Arithmetic checks for the five-number summary article."""

from pathlib import Path

root = Path(__file__).resolve().parents[1]
prose = (root / "research/content/five-number-summary-and-boxplot.md").read_text(encoding="utf-8")
article = root / "articles/five-number-summary-and-boxplot.qmd"
built = article.read_text(encoding="utf-8") if article.is_file() else ""
page = built if "Your turn" in built else prose


def require(text: str) -> None:
    assert text in prose, text
    assert text in page, text


xs = [4, 7, 8, 9, 12, 15, 40]
n = len(xs)

def quartile(j):
    pos = j * (n + 1) / 4
    i = int(pos)
    k = pos - i
    if k == 0:
        return xs[i - 1]
    return xs[i - 1] + k * (xs[i] - xs[i - 1])

assert [quartile(j) for j in (1, 2, 3)] == [7, 9, 15]
iqr = 15 - 7
assert iqr == 8
assert 15 + 1.5 * iqr == 27
assert 7 - 1.5 * iqr == -5
assert 40 > 27

ys = [2, 5, 6, 8, 9, 11, 30]
assert ys[1] == 5 and ys[3] == 8 and ys[5] == 11
assert 11 - 5 == 6 and 11 + 9 == 20 and 30 > 20

# Hinge quartiles of the ten cartons, as in the bank answer.
cartons = sorted([1.035, 1.019, 1.068, 1.084, 1.077, 0.998, 1.041, 1.037, 1.051, 1.102])
assert abs((cartons[4] + cartons[5]) / 2 - 1.046) < 1e-12
assert cartons[2] == 1.035 and cartons[7] == 1.077

for text in ("$4,7,9,15,40$", "$15-7=8$", "$15+1.5\\times 8=27$", "$2,5,8,11,30$", "$11+9=20$", "1.046", "1.035", "1.077", "4.4", "1.6"):
    require(text)
print("five-number-summary-and-boxplot checks passed")
