"""Check the printed nearest-neighbour distances and votes."""
import math
from pathlib import Path


def test_printed_values():
    page = (Path(__file__).resolve().parents[1] / "articles" / "nearest-neighbours.qmd").read_text()
    assert "{#worked-example}" in page and "Your turn" in page
    labels = ['A', 'B', 'B', 'A', 'A']
    positions = [1, 3, 5, 8, 9]
    responses = [10, 20, 24, 30, 40]
    distances = [abs(x - 4) for x in positions]
    assert distances == [3, 1, 1, 4, 5]
    selected = sorted(range(5), key=lambda i: (distances[i], i))[:3]
    assert selected == [1, 2, 0]
    assert [labels[i] for i in selected] == ['B', 'B', 'A']
    assert sum(labels[i] == 'B' for i in selected) / 3 == 2 / 3
    assert sum(responses[i] for i in selected) / 3 == 18
    assert labels.count('A') / 5 == 3 / 5
    assert sum(responses) == 124
    assert sum(responses) / 5 == 24.8
    # Your turn and the original two-coordinate training example.
    positions = [2, 5, 7, 10, 12]
    labels = ['A', 'B', 'B', 'A', 'A']
    distances = [abs(x - 6) for x in positions]
    assert distances == [4, 1, 1, 4, 6]
    selected = sorted(range(5), key=lambda i: (distances[i], i))[:3]
    assert [labels[i] for i in selected] == ['B', 'B', 'A']
    assert sum(labels[i] == 'B' for i in selected) / 3 == 2 / 3
    assert labels.count('A') == 3
    assert math.isclose(math.sqrt(101), 10.05, abs_tol=0.005)
    assert math.isclose(math.sqrt(10), 3.16, abs_tol=0.005)
    assert math.isclose(math.sqrt(2), 1.41, abs_tol=0.005)
    assert math.isclose(math.sqrt(9.01), 3.00, abs_tol=0.005)
    # Baseline soft vote and idealized Bernoulli variance example.
    assert sum([1, 1, 2][i] == 1 for i in range(3)) / 3 == 2 / 3
    tau, k = 2 / 3, 3
    assert math.isclose(tau * (1 - tau) / k, 2 / 27)


if __name__ == "__main__":
    test_printed_values()
