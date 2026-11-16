"""Arithmetic printed in the predictive distributions article."""
import math


def test_printed_values():
    a, b, successes, failures = 2, 2, 7, 3
    post_a, post_b = a + successes, b + failures
    assert (post_a, post_b) == (9, 5)
    assert a / (a + b) == 0.5
    assert math.isclose(post_a / (post_a + post_b), 0.64286, abs_tol=0.000005)
    joint = post_a * (post_a + 1) / ((post_a + post_b) * (post_a + post_b + 1))
    assert math.isclose(joint, 3 / 7)
    assert math.isclose(joint, 0.42857, abs_tol=0.000005)
    assert math.isclose((9 / 14) ** 2, 0.41327, abs_tol=0.000005)
    assert a * (a + 1) / ((a + b) * (a + b + 1)) == 0.3
    a, b, successes, failures = 1, 1, 3, 1
    post_a, post_b = a + successes, b + failures
    assert (post_a, post_b) == (4, 2)
    assert a / (a + b) == 0.5
    assert post_a / (post_a + post_b) == 2 / 3
    joint = post_a * (post_a + 1) / ((post_a + post_b) * (post_a + post_b + 1))
    assert math.isclose(joint, 10 / 21)
    assert math.isclose(joint, 0.47619, abs_tol=0.000005)
    assert math.isclose((2 / 3) ** 2, 4 / 9)


if __name__ == "__main__":
    test_printed_values()
