"""Recompute the worked calculations and inspect the generated article."""
from pathlib import Path
import re
root = Path(__file__).resolve().parents[1]
source = (root / "research" / "content" / (Path(__file__).stem + ".md")).read_text()
article = (root / "articles" / (Path(__file__).stem + ".qmd")).read_text()
body = article.split("## See also", 1)[0]
assert len(re.findall(r"\{\{cite:", source)) >= 5
assert len(set(re.findall(r"\{\{cite:([^}]+)", source))) >= 2
assert "Your turn" in body and 'collapse="true"' in body

from math import log, exp
ages=[71, 158, 128, 2, 1, 1, 61, 37, 113, 59, 82, 148, 18, 1, 168, 1, 78, 175, 80, 27, 22, 105, 96, 131, 15, 9, 8, 100, 4, 151, 31, 125, 130, 112, 140, 93, 1, 52, 20, 91, 73, 35, 143, 61, 97, 139, 136, 131, 121, 177, 68, 9, 139, 2, 140, 72, 2, 120, 51, 102, 130, 114, 81, 118, 118, 17, 195, 159, 18, 15, 158, 127, 87, 206, 11, 178, 157, 26, 120, 42, 36]
y=[0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0]
assert len(y)==81 and sum(y)==17 and len(y)-sum(y)==64
assert min(ages)==1 and max(ages)==206
p=sum(y)/len(y)
eta=log(p/(1-p))
assert abs(p-.20987654320987653)<1e-14
assert abs(eta+1.3256697393034558)<1e-14
assert abs(exp(eta)-.265625)<1e-14
assert abs(exp(eta)/(1+exp(eta))-p)<1e-14
assert abs(17/p-64/(1-p))<1e-12
for number in ['17','64','0.209877','-1.325670','206','0.265625']:
    assert number in body

print("kyphosis-data checks passed")
