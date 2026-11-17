from pathlib import Path
import json,re
ROOT=Path(__file__).resolve().parents[1]
from statistics import mean,median
x=[2,3,3,4,5];z=x[:-1]+[50]
assert mean(x)==3.4 and median(x)==3 and max(x)-min(x)==3
assert mean(z)==12.4 and median(z)==3 and max(z)-min(z)==48
assert mean(x[:-1]+[8])==4 and median(x[:-1]+[8])==3
assert mean(x[:-1]+[500])==102.4
printed=['3.4','12.4','48','102.4']

# Deepened research calculations.
vals = [2, 3, 3, 4, 9]
assert sum(vals)/len(vals) == 4.2
ordered = sorted(vals)
assert ordered[len(ordered)//2] == 3

article=(ROOT/"articles"/"exploratory-data-analysis.qmd").read_text()
for token in printed:
    assert token in article,("exploratory-data-analysis",token)
questions=json.loads((ROOT/"research/self-checks.json").read_text())["exploratory-data-analysis"]
assert len(questions) in (2,3)
assert article.count("## Check yourself {#check-yourself}") == 1
assert "Your turn" in article
print("exploratory-data-analysis: numerical examples, self-checks and generated text verified")
