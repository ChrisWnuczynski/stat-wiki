"""Independent numerical and symbolic checks, including generated article content."""
from pathlib import Path
import re
import math
import numpy as np
import sympy as s
ROOT=Path(__file__).resolve().parents[1]
assert 40+22==62 and 2000-(62-1)==1939
assert abs(40/62-.645161)<5e-7
assert abs(8/62-.129032)<5e-7
assert 2000*.05==100
# An explicit centred matrix attains the n-1 upper bound.
X=np.array([[1,0,0,2,0,1],[0,1,0,0,2,1],[0,0,1,1,1,2],[0,0,0,0,0,0]],float)
X-=X.mean(axis=0)
assert np.linalg.matrix_rank(X)==3
assert np.linalg.matrix_rank(X.T@X)==3
assert np.count_nonzero(np.linalg.eigvalsh(X.T@X)<1e-10)==3
# Recompute descriptive counts and coefficient ranking for the reported list;
# the underlying fit is separately recorded as not yet reproducible.
genes=np.array([14,249,377,493,576,625,792,1360,1473,1582,1679,1772,1843,1924])
coef=np.array([-.111,-.081,-.588,-.275,.136,.118,-.116,.089,.113,.085,.141,.302,-.207,-.141])
assert len(genes)==len(coef)==14
assert genes[np.argmax(abs(coef))]==377 and genes[np.argmin(abs(coef))]==249
assert genes[np.argsort(abs(coef))[-2]]==1772
third={1635,493,625,765,1511,1634,1153,992,1293,1002,1959,609}
assert set(genes)&third=={493,625}
overlap={14,249,377,493,625,1473,1582,1679,1772,1843,1924}
assert len(overlap)==11 and overlap<=set(genes) and len(overlap-{249})==10
source=(ROOT/"research/content/alon-colon-cancer-data.md").read_text()
article=(ROOT/"articles/alon-colon-cancer-data.qmd").read_text().split("## See also",1)[0]
for needle in ['1939', '0.645161', '0.129032']:
    assert needle in source and needle in article,needle
assert len(re.findall(r"\{\{cite:[^}]+\}\}",source))>=5
assert len(set(re.findall(r"\{\{cite:([^}]+)\}\}",source)))>=2
assert "Your turn" in article and 'collapse="true" title="Answer"' in article
assert "## Check yourself {#check-yourself}" in article
print("alon-colon-cancer-data: calculations and article checks passed")
