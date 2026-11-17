"""Arithmetic checks for the identity-link article."""

from pathlib import Path

import numpy as np
from scipy.stats import laplace, norm

root = Path(__file__).resolve().parents[1]
prose = (root / "research/content/identity-link.md").read_text(encoding="utf-8")
article = root / "articles/identity-link.qmd"
built = article.read_text(encoding="utf-8") if article.is_file() else ""
page = built if "Your turn" in built else prose


def require(text: str) -> None:
    assert text in prose, text
    assert text in page, text


X = np.array([[1.0, 0.0], [1.0, 1.0], [1.0, 1.0]])
y = np.array([1.0, 2.0, 5.0])
beta = np.linalg.solve(X.T @ X, X.T @ y)
fitted = X @ beta
rss = float(np.sum((y - fitted) ** 2))
assert np.allclose(beta, [1.0, 2.5])
assert np.allclose(fitted, [1.0, 3.5, 3.5])
assert abs(rss - 4.5) < 1e-12

X2 = np.array([[1.0, 0.0], [1.0, 0.0], [1.0, 1.0]])
y2 = np.array([2.0, 4.0, 6.0])
beta2 = np.linalg.solve(X2.T @ X2, X2.T @ y2)
assert np.allclose(beta2, [3.0, 3.0])
assert abs(float(np.sum((y2 - X2 @ beta2) ** 2)) - 2.0) < 1e-12

# A linear mean and common variance alone do not imply Gaussian likelihood.
# Independent normal and Laplace responses both have variance two here.
X3 = np.array([[1.0, 0.0], [1.0, 1.0], [1.0, 2.0]])
y3 = np.array([1.0, 2.0, 5.0])
ols = np.linalg.solve(X3.T @ X3, X3.T @ y3)
alternative = np.array([1.0, 2.0])
assert np.allclose(ols, [2 / 3, 2])
assert np.isclose(norm.var(scale=np.sqrt(2)), 2)
assert laplace.var(scale=1) == 2
normal_gain = norm.logpdf(y3, loc=X3 @ ols, scale=np.sqrt(2)).sum() - norm.logpdf(
    y3, loc=X3 @ alternative, scale=np.sqrt(2)
).sum()
laplace_gain = laplace.logpdf(y3, loc=X3 @ alternative, scale=1).sum() - laplace.logpdf(
    y3, loc=X3 @ ols, scale=1
).sum()
assert np.isclose(normal_gain, 1 / 12)
assert np.isclose(laplace_gain, 1 / 3)
assert "independent normal responses" in prose
require(r"$\sigma^2>0$")
assert "; accepted links)" not in prose and "; accepted links)" not in page

for text in ("2.5", "3.5", "4.5", "(3,3)", "$1+1+0=2$"):
    require(text)
print("identity-link checks passed")
