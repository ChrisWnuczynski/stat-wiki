"""Check Student t moments and tails."""
from pathlib import Path
from scipy.stats import t, norm
root = Path(__file__).resolve().parents[1]
body = (root / "articles/student-t-distribution.qmd").read_text().split("## See also", 1)[0]
assert abs(5/3 - 1.6667) < 5e-5
assert abs(2*(1-t.cdf(2, 5)) - 0.1019) < 5e-5
assert abs(2*(1-norm.cdf(2)) - 0.0455) < 5e-5
assert abs(8/6 - 1.3333) < 5e-5
assert abs(t.ppf(0.975, 8) - 2.30600) < 5e-6
assert abs(norm.ppf(0.975) - 1.95996) < 5e-6
assert 3/(3-2) == 3
for s in ("1.6667", "0.1019", "0.0455", "1.3333", "2.30600", "1.95996"):
    assert s in body, s
assert "**Your turn.**" in body and "Check yourself" in body
assert 'data-cite-key="dodge2008"' in body
assert 'data-cite-key="student1908"' in body
assert body.count('title="Proof"') == 1
print("student t passed")
