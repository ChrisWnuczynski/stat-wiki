"""Verify Iris table counts, new examples and inherited summary values."""

from pathlib import Path
import numpy as np
from sklearn.datasets import load_iris

root = Path(__file__).resolve().parents[1]
page = (root / "articles/iris-data.qmd").read_text()
body = page.split("## See also", 1)[0]
iris = load_iris()
x, y = iris.data, iris.target
assert x.shape == (150, 4) and len(y) == 150
assert np.bincount(y).tolist() == [50, 50, 50]
means = np.array([x[y == g].mean(axis=0) for g in range(3)])
assert np.allclose(means[:, 2], [1.462, 4.260, 5.552])
assert round(means[1, 2] - means[0, 2], 3) == 2.798
assert round(means[2, 2] - means[1, 2], 3) == 1.292
assert [(x[y == g, 2].min(), x[y == g, 2].max()) for g in range(3)] == [
    (1.0, 1.9), (3.0, 5.1), (4.5, 6.9)]
pred = x[:, 2] < 2.0
assert np.all(pred == (y == 0)) and pred.sum() == 50
assert np.allclose(np.cov(x, rowvar=False)[0], [.686, -.042, 1.274, .516], atol=.0005)
assert np.allclose(np.cov(x[y == 0], rowvar=False)[0], [.124, .099, .016, .010], atol=.0005)

for printed in ("150", "50", "1.462", "4.260", "5.552", "1.0", "1.9",
                "3.0", "4.5", "2.0", "100", "150/150", "100\\%",
                "2.798", "1.292", "0.686", "-0.042", "1.274", "0.516"):
    assert printed in body, printed
assert body.count('title="Proof"') == 1
assert "## Motivating example" in body and "## Worked example" in body
assert "**Your turn.**" in body and 'title="Answer"' in body
assert 'data-cite-key="r_iris_doc2026"' in body
print("Iris counts, summaries and practice passed")
