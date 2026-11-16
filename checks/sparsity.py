"""Arithmetic checks for the sparsity article."""

from pathlib import Path

import numpy as np

root = Path(__file__).resolve().parents[1]
prose = (root / "research/content/sparsity.md").read_text(encoding="utf-8")
article = root / "articles/sparsity.qmd"
built = article.read_text(encoding="utf-8") if article.is_file() else ""
page = built if "Your turn" in built else prose


def require(text: str) -> None:
    assert text in prose and text in page, text


def soft(y, lam=2):
    if abs(y) <= lam / 2:
        return 0
    return y - lam / 2 if y > 0 else y + lam / 2


assert soft(3) == 2 and soft(0.4) == 0 and soft(-4) == -3
assert soft(-0.5) == 0 and soft(1) == 0

X = np.array([[1.0, 1.0], [1.0, 1.0]])
xtx = X.T @ X
eig = np.linalg.eigvalsh(xtx)
assert np.allclose(sorted(eig), [0, 4])
y = np.array([1.0, 3.0])
beta = np.linalg.solve(xtx + np.eye(2), X.T @ y)
assert np.allclose(beta, [0.8, 0.8])

require("=2$")
require(r"\hat\beta=0")
require("=-3")
require("(0.8,0.8)")
require("at most $3$")
print("sparsity checks passed")
