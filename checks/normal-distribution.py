"""Check displayed normal probabilities and the article's source keys."""

import re
from math import isclose, pi, log
from pathlib import Path
from statistics import NormalDist


if __name__ == "__main__":
    page = (Path(__file__).resolve().parents[1] / "articles" / "normal-distribution.qmd").read_text()
    printed = (
        r"$0.683$", r"$0.954$", r"$0.997$",
        r"1-\Phi(1.875)=0.030",
        r"P(Z>1)\approx0.1587",
        r"\Phi(1.3)\approx 0.9032",
        r"\Phi(1.4)\approx 0.9192",
        r"\Phi(0.5)\approx 0.6915",
        r"\Phi(1)\approx 0.8413",
        r"0.6915-0.1587=0.5328",
        r"\operatorname{diag}(1/\sigma^2,2/\sigma^2)",
        r"\tfrac12\log(2\pi e\sigma^2)",
        r"P(X<496)=\Phi(-1)\approx0.1587",
        r"1-\Phi(\sqrt2)\approx0.07865",
        r"1-\Phi(2)\approx0.02275",
    )
    for value in printed:
        assert value in page, f"Value missing from generated article: {value}"
    assert re.search(
        r"\\begin\{aligned\}\s*"
        r"&\\mathbb\{P\}\(90<X\\le110\)\\\\\s*"
        r"&=\\Phi\(0\.625\)-\\Phi\(-0\.625\)\\\\\s*"
        r"&=2\\Phi\(0\.625\)-1\\\\\s*"
        r"&=0\.468\.\s*"
        r"\\end\{aligned\}",
        page,
    ), "Stepped IQ probability missing from generated article"
    normal = NormalDist()
    assert round(normal.cdf(1)-normal.cdf(-1), 3) == 0.683
    assert round(normal.cdf(2)-normal.cdf(-2), 3) == 0.954
    assert round(normal.cdf(3)-normal.cdf(-3), 3) == 0.997
    assert round(2*normal.cdf(0.625)-1, 3) == 0.468
    assert round(1-normal.cdf(1.875), 3) == 0.030
    assert round(1-normal.cdf(1), 4) == 0.1587
    for z, expected in ((1.3, 0.9032), (1.4, 0.9192), (0.5, 0.6915), (1, 0.8413)):
        assert isclose(normal.cdf(z), expected, abs_tol=0.00005)
    assert round(normal.cdf(0.5) - (1-normal.cdf(1)), 4) == 0.5328
    assert round(1-normal.cdf(2**0.5), 5) == 0.07865
    assert round(1-normal.cdf(2), 5) == 0.02275
    assert isclose(0.5*log(2*pi*2.718281828459045), 0.5*log(2*pi)+0.5)
    keys = set(re.findall(r'data-cite-key="([^"]+)"', page.split('## References')[0]))
    opened = {
        "siegrist2022_normal_distribution", "siegrist2022_lognormal_distribution",
        "siegrist2022_binomial_distribution", "siegrist2022_normals",
        "gelman_bda2013", "raiffa_schlaifer1961", "hoff2013_bayes_estimators",
        "box_muller1958", "gelfand_smith1990",
        "daw1966_normal_history", "oliveira2022_probability_history",
    }
    assert "gelfand_smith1990" in keys
    assert keys <= opened, f"Normal article cites sources not checked for this pass: {keys-opened}"
    for line in page.splitlines():
        if '<li id="cite_note-' in line:
            assert 'cite-backlink' in line, f"Uncited bibliography entry: {line[:100]}"
    print("normal-distribution arithmetic, printed values, and source keys passed")
