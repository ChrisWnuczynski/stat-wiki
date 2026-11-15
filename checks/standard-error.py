"""Recompute the standard-error page's new and retained numeric examples."""

from math import isclose, sqrt


if __name__ == "__main__":
    checks = [
        isclose(20 / sqrt(100), 2),
        isclose(10 / sqrt(25), 2),
        isclose(2.064 * 2, 4.128),
        isclose(50 - 2.064 * 2, 45.872),
        isclose(50 + 2.064 * 2, 54.128),
        isclose(sqrt(2**2 + 2**2), sqrt(8)),
        isclose(4 / sqrt(8), sqrt(2)),
        isclose(sqrt((14.1**2 + 14.3**2) / 2), 14.200352108310556),
        isclose(sqrt((14.1**2 + 14.3**2) / 2) / 5, 2.840070421662111),
        isclose(-17 / 2.84, -5.985915492957747),
        isclose(2 * 0.8413447460685429 - 1, 0.6826894921370859),
        isclose(2 * 0.9772498680518208 - 1, 0.9544997361036416),
    ]
    assert all(checks)
    print(f"standard-error arithmetic: {len(checks)} checks passed")
