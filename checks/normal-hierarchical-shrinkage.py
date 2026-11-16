"""Check printed normal hierarchical shrinkage examples and the bank addition."""
import math


def close(actual, printed, places=2):
    assert math.isclose(actual, printed, abs_tol=0.5 * 10 ** -places)


def update(mu, sigma2, tau2, n, ybar):
    weight = n * tau2 / (sigma2 + n * tau2)
    mean = weight * ybar + (1 - weight) * mu
    variance = sigma2 * tau2 / (sigma2 + n * tau2)
    return weight, mean, variance


def test_printed_values():
    # Preserved large and small tutorial-class example.
    w, m, v = update(70, 100, 25, 100, 75)
    assert math.isclose(w, 25 / 26)
    close(w, 0.962, 3)
    close(m, 74.81)
    w, m, v = update(70, 100, 25, 2, 95)
    assert math.isclose(w, 1 / 3)
    close(m, 78.33)
    # Preserved rat-tumour beta-binomial example.
    assert (2 + 4) / (2 + 8 + 10) == 0.3
    close((2 + 40) / (2 + 8 + 100), 0.3818, 4)
    assert 10 / 20 == 1 / 2
    assert 10 / 110 == 1 / 11
    # New laboratory worked example.
    w, m, v = update(50, 144, 36, 4, 62)
    assert (w, m, v) == (0.5, 56, 18)
    w, m, v = update(50, 144, 36, 36, 62)
    assert math.isclose(w, 0.9)
    assert math.isclose(m, 60.8)
    assert math.isclose(v, 3.6)
    # Your turn.
    assert update(100, 400, 100, 4, 130) == (0.5, 115, 50)
    w, m, v = update(100, 400, 100, 16, 130)
    assert math.isclose(w, 0.8)
    assert math.isclose(m, 124)
    assert math.isclose(v, 20)
    # Proposed bank item: total variance over two hyperparameter regimes.
    means = [5, 9]
    marginal_mean = sum(means) / 2
    between = sum((m - marginal_mean) ** 2 for m in means) / 2
    assert marginal_mean == 7
    assert between == 4
    assert 1 + between == 5


if __name__ == "__main__":
    test_printed_values()
