"""Arithmetic checks for the dummy-variable-coding article."""

from pathlib import Path

import numpy as np

root = Path(__file__).resolve().parents[1]
prose = (root / "research/content/dummy-variable-coding.md").read_text(encoding="utf-8")
article = root / "articles/dummy-variable-coding.qmd"
built = article.read_text(encoding="utf-8") if article.is_file() else ""
page = built if "Your turn" in built else prose


def require(text: str) -> None:
    assert text in prose, text
    assert text in page, text


y = np.array([10.0, 12.0, 14.0, 16.0, 20.0, 22.0])
# Reference A: intercept, I_B, I_C.
X = np.array([
    [1, 0, 0],
    [1, 0, 0],
    [1, 1, 0],
    [1, 1, 0],
    [1, 0, 1],
    [1, 0, 1],
], float)
beta = np.linalg.solve(X.T @ X, X.T @ y)
assert np.allclose(beta, [11, 4, 10])
assert np.allclose(X @ beta, [11, 11, 15, 15, 21, 21])

# Reference C.
Xc = np.array([
    [1, 1, 0],
    [1, 1, 0],
    [1, 0, 1],
    [1, 0, 1],
    [1, 0, 0],
    [1, 0, 0],
], float)
betac = np.linalg.solve(Xc.T @ Xc, Xc.T @ y)
assert np.allclose(betac, [21, -10, -6])

# Interaction residuals from the bank question.
cells = np.array([[3.0, 5.0], [4.0, 10.0]])
row = cells.mean(axis=1)
col = cells.mean(axis=0)
grand = cells.mean()
resid = cells - row[:, None] - col[None, :] + grand
assert np.allclose(resid, [[1, -1], [-1, 1]])
assert abs(np.sum(resid ** 2) - 4) < 1e-12
assert abs((10 + 4 - 2 + 3) - 15) < 1e-12

require(r"\hat\beta_0=11")
require(r"\hat\beta_B=4")
require(r"\hat\beta_C=10")
require("11-21=-10")
require("15-21=-6")
require("$11-15=-4$")
print("dummy-variable-coding checks passed")
