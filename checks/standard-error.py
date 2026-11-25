"""Recompute the standard-error page's printed numeric examples."""

from math import isclose, sqrt
from pathlib import Path


if __name__ == "__main__":
    root = Path(__file__).resolve().parents[1]
    prose = (root / "research/content/standard-error.md").read_text()
    for printed in ("20 grams", "2 grams", "10/\\sqrt{25}=2.0", "2.064", "45.87", "54.13", "2.83", "1.41", "-5.99", "68.3%"):
        assert printed in prose, f"Worked value missing from article source: {printed}"
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
    generated = root / "articles/standard-error.qmd"
    if generated.exists():
        page = generated.read_text()
        definition = page.split("## Definition {#definition}", 1)[1].split("\n## ", 1)[0]
        chapter_import = definition.split("::: {.mainarticle}", 1)[0]
        for printed in (
            "hypothetical comparison of rod lengths", "Two independent groups of 25 rods",
            "divisor $n-1$", "94-100=-6",
            r"s_p^2=(24\times8^2+24\times6^2)/48=50",
            r"\sqrt{50(1/25+1/25)}=2",
        ):
            assert printed in chapter_import, f"Worked value missing from chapter import: {printed}"
        for leaked in ("91-108=-17", "14.20/5=2.84", r"-17\pm2.84"):
            assert leaked not in chapter_import, f"Exercise solution leaked into chapter import: {leaked}"
        for printed in ("0.683", "0.954"):
            assert printed in page, f"Earlier value missing from generated page: {printed}"
    assert round(50 - 2.064 * 2, 2) == 45.87
    assert round(50 + 2.064 * 2, 2) == 54.13
    assert round(sqrt(8), 2) == 2.83
    assert round(4 / sqrt(8), 2) == 1.41
    print(f"standard-error arithmetic: {len(checks)} checks passed")
