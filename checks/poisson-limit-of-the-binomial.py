"""Compare exact binomial masses with the Poisson limit and verify its factorisation."""
from pathlib import Path
from math import exp,factorial,prod,isclose
from scipy.stats import binom,poisson
import re
root=Path(__file__).resolve().parents[1]
for n in [100,1000]:
    for k in range(6):
        p=2/n
        factored=2**k/factorial(k)*prod(1-j/n for j in range(k))*(1-p)**n*(1-p)**(-k)
        assert isclose(factored,binom.pmf(k,n,p),rel_tol=1e-11)
assert round(binom.pmf(0,100,.02),6)==.132620
assert round(poisson.pmf(0,2),6)==.135335
assert round(binom.pmf(3,100,.02),6)==.182276
assert round(poisson.pmf(3,2),6)==.180447
assert round(binom.pmf(0,1000,.002),6)==.135065
assert abs(binom.pmf(0,1000,.002)-exp(-2))<abs(binom.pmf(0,100,.02)-exp(-2))
assert 3600/100==36
groups=1_000_000//3;rate=groups/365**2
assert groups==333333 and isclose(rate,2.5020304,rel_tol=1e-7)
assert round(1-(1-1/365**2)**groups,2)==.92
assert round(1-exp(-2.5),3)==.918
body=(root/"articles/poisson-limit-of-the-binomial.qmd").read_text().split("## See also",1)[0]
for text in ["0.132620","0.135335","0.182276","0.180447","0.135065","Your turn"]:
    assert text in body,text
assert 'title="Proof"' in body and len(re.findall('class="cite-ref"',body))>=5
assert "## Check yourself {#check-yourself}" in body
for q in ["ex-prob-radioactive","ex-prob-brisbane-groups"]:
    assert f"../questions/{q}.qmd" in body
print("poisson-limit-of-the-binomial: mass factorisation, approximations and article checks passed")
