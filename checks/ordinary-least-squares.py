"""Check OLS algebra and all substantive numerical calculations on the article."""

from pathlib import Path

import numpy as np
from scipy.stats import t
from sympy import Matrix, Rational

root = Path(__file__).resolve().parents[1]
page = (root / "articles/ordinary-least-squares.qmd").read_text()
body = page.split("## See also", 1)[0]

def fit(x, y):
    X = Matrix([[1, v] for v in x])
    Y = Matrix(y)
    beta = (X.T * X).inv() * X.T * Y
    fitted = X * beta
    residual = Y - fitted
    sse = (residual.T * residual)[0]
    assert X.T * residual == Matrix([0, 0])
    return X, beta, fitted, residual, sse

X3, b3, f3, e3, sse3 = fit([0, 1, 2], [1, 2, 2])
assert b3 == Matrix([Rational(7, 6), Rational(1, 2)])
assert f3 == Matrix([Rational(7, 6), Rational(5, 3), Rational(13, 6)])
assert e3 == Matrix([Rational(-1, 6), Rational(1, 3), Rational(-1, 6)])
assert sse3 == Rational(1, 6)
assert sum(e3) == 0 and sse3 / (3 - 2) == Rational(1, 6)

X4, b4, f4, e4, sse4 = fit([0, 1, 2, 3], [1, 2, 2, 4])
assert b4 == Matrix([Rational(9, 10), Rational(9, 10)])
assert f4 == Matrix([Rational(9, 10), Rational(9, 5), Rational(27, 10), Rational(18, 5)])
assert e4 == Matrix([Rational(1, 10), Rational(1, 5), Rational(-7, 10), Rational(2, 5)])
assert sse4 == Rational(7, 10) and sse4 / (4 - 2) == Rational(7, 20)

H = X4 * (X4.T * X4).inv() * X4.T
assert H.T == H and H * H == H and H.trace() == 2
candidate = b4 + Matrix([1, -1])
lhs = ((X4 * candidate - Matrix([1, 2, 2, 4])).T *
       (X4 * candidate - Matrix([1, 2, 2, 4])))[0]
rhs = sse4 + ((candidate - b4).T * X4.T * X4 * (candidate - b4))[0]
assert lhs == rhs

# Inherited eight-point regression and Bayesian predictive numbers.
x8 = np.arange(1, 9, dtype=float)
y8 = np.array([2.05, 3.40, 4.55, 5.10, 7.20, 8.05, 9.60, 10.80])
A = np.column_stack((np.ones(8), x8))
C = np.linalg.inv(A.T @ A)
b = C @ A.T @ y8
SSE = np.sum((y8 - A @ b) ** 2)
s2 = SSE / 6
assert round(float(y8.sum()), 2) == 50.75
assert round(float(x8 @ y8), 2) == 280.80
assert round(float(y8 @ y8), 4) == 387.9175
assert np.allclose(A.T @ A, [[8, 36], [36, 204]])
assert round(float(np.linalg.det(A.T @ A))) == 336
assert np.allclose(b, [0.7267857142857143, 1.2482142857142857])
assert round(float(SSE), 6) == 0.534554
assert round(float(s2), 6) == 0.089092
assert round(float(SSE / 2), 6) == 0.267277
assert round(float((SSE / 2) / 2), 6) == 0.133638
assert round(float((SSE / 2) / 4), 6) == 0.066819
q6 = t.ppf(0.975, 6)
assert round(q6, 3) == 2.447
intervals = [(b[j] - q6 * np.sqrt(s2 * C[j, j]), b[j] + q6 * np.sqrt(s2 * C[j, j])) for j in range(2)]
assert [tuple(round(float(v), 3) for v in pair) for pair in intervals] == [(0.158, 1.296), (1.136, 1.361)]
for xstar, hprint, center, scale in [(4.5, 0.125, 6.34375, 0.317), (10, 0.845, 13.209, 0.405)]:
    z = np.array([1, xstar])
    h = float(z @ C @ z)
    assert round(h, 3) == hprint
    assert round(float(z @ b), 5 if xstar == 4.5 else 3) == center
    assert round(float(np.sqrt(s2 * (1 + h))), 3) == scale

# Inherited ten-point Bayesian example.
q8 = t.ppf(0.975, 8)
assert round(q8, 3) == 2.306
assert round(8 / (4 - 1), 4) == 2.6667
assert round(q8 * np.sqrt(2 / 40), 4) == 0.5156
assert tuple(round(v, 3) for v in (2 - q8 * np.sqrt(2 / 40), 2 + q8 * np.sqrt(2 / 40))) == (1.484, 2.516)
assert round(q8 * np.sqrt(0.2), 4) == 1.0313
assert round(q8 * np.sqrt(2.2), 4) == 3.4204
assert round(np.sqrt(2.2), 4) == 1.4832
assert round(np.sqrt(3), 4) == 1.7321

for printed in ("0.726786", "1.248214", "0.534554", "0.089092", "0.133638",
                "0.066819", "6.34375", "13.209", "0.125", "0.845", "0.317",
                "0.405", "2.6667", "0.5156", "1.0313", "3.4204", "1.4832",
                "1.7321", "7/6", "5/3", "13/6", "1/6", "0.70", "0.35"):
    assert printed in body, f"missing printed number: {printed}"
assert body.count('title="Proof"') == 1
assert "## Motivating example" in body and "## Key results" in body
assert "**Your turn.**" in body and 'title="Answer"' in body
assert "### When it fails" in body and "## Common misconceptions" in body
assert "part1-fig-09-regression-bands.png" in body
for qid in ("ex-inf-normal-equations", "ex-inf-line-through-origin", "ex-inf-advertising-r2"):
    assert f"../questions/{qid}.qmd" in body
    assert "Worked answer" in (root / f"questions/{qid}.qmd").read_text()
print("ordinary least squares algebra, numbers and structure passed")
